#!/usr/bin/env python3
"""Crawl all PL pages and fill content stubs with real text from the live site."""

import json
import re
import subprocess
import sys
from pathlib import Path

try:
    from bs4 import BeautifulSoup, Comment, Tag
except ImportError:
    print("ERROR: beautifulsoup4 not installed. Run: pip3 install beautifulsoup4 lxml")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).parent.parent
URL_MAP = PROJECT_ROOT / "src/data/url-map.json"

HEADING_TAGS = {"h1", "h2", "h3", "h4"}
BLOCK_TAGS = {"p", "li"}
CTA_TAGS = {"a"}

# Classes/IDs to remove from within the content area
INNER_SKIP_CLASS_FRAGMENTS = [
    "cookie", "gdpr", "consent", "popup", "modal", "rezForm", "rezform",
    "bookingform", "booking-form", "offers-main", "offersMain",
]


def fetch_html(url: str) -> str | None:
    """Fetch URL with curl, return HTML string or None on error."""
    try:
        result = subprocess.run(
            [
                "curl", "--silent", "--location", "--compressed",
                "--max-time", "30",
                "--user-agent", "Mozilla/5.0 (compatible; ZaciszeCrawler/1.0)",
                url,
            ],
            capture_output=True,
            text=True,
            timeout=35,
        )
        if result.returncode != 0:
            return None
        return result.stdout
    except subprocess.TimeoutExpired:
        return None
    except Exception:
        return None


def clean_text(text: str) -> str:
    """Strip extra whitespace."""
    return re.sub(r"\s+", " ", text).strip()


def extract_markdown(html: str) -> str:
    """Parse HTML, extract visible content as Markdown from article.articleContent."""
    soup = BeautifulSoup(html, "lxml")

    # Remove comments
    for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()

    # Remove scripts/styles globally
    for tag_name in ["script", "style", "noscript", "iframe", "svg"]:
        for el in soup.find_all(tag_name):
            el.decompose()

    # Try to find the main content area: article.articleContent is used by this CMS
    content_root = soup.find("article", class_=lambda c: c and "articleContent" in c)
    if not content_root:
        # Fallback: try <main>, then <body>
        content_root = soup.find("main") or soup.find("body") or soup

    # Within content root, remove inner noise
    to_remove = []
    for el in content_root.find_all(True):
        if not isinstance(el, Tag) or el.attrs is None:
            continue
        classes = " ".join(el.get("class", [])).lower()
        tag_id = (el.get("id") or "").lower()
        combined = classes + " " + tag_id
        for fragment in INNER_SKIP_CLASS_FRAGMENTS:
            if fragment in combined:
                to_remove.append(el)
                break
    for el in to_remove:
        el.decompose()

    lines: list[str] = []
    seen: set[str] = set()

    for tag in content_root.find_all(True):
        if not isinstance(tag, Tag) or tag.attrs is None:
            continue
        if tag.name not in (HEADING_TAGS | BLOCK_TAGS | CTA_TAGS):
            continue
        text = clean_text(tag.get_text())
        if not text or len(text) < 3:
            continue
        if text in seen:
            continue
        seen.add(text)

        if tag.name in HEADING_TAGS:
            level = int(tag.name[1])
            line = f"{'#' * level} {text}"
        elif tag.name == "li":
            line = f"- {text}"
        elif tag.name in CTA_TAGS:
            href = tag.get("href", "")
            if href and not href.startswith("#") and not href.startswith("javascript"):
                line = f"[{text}]({href})"
            else:
                line = text
        else:
            line = text

        lines.append(line)

    # Deduplicate consecutive identical lines
    result_lines: list[str] = []
    prev = None
    for line in lines:
        if line != prev:
            result_lines.append(line)
            prev = line

    return "\n\n".join(result_lines)


def read_frontmatter_end(path: Path) -> int:
    """Return the line index (0-based) just after the closing --- of frontmatter."""
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return 0
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return i + 1  # line after closing ---
    return 0


def has_body(path: Path) -> bool:
    """Return True if the file already has content below the frontmatter."""
    content = path.read_text(encoding="utf-8")
    # Find second ---
    idx = content.find("---", 3)
    if idx == -1:
        return False
    after = content[idx + 3:].strip()
    return bool(after)


def append_body(path: Path, markdown: str) -> None:
    """Append extracted markdown after the frontmatter --- of the stub."""
    content = path.read_text(encoding="utf-8")
    # Ensure exactly one trailing newline after frontmatter closing ---
    # then add body
    if "---" in content[3:]:
        fm_end = content.find("---", 3) + 3
        new_content = content[:fm_end].rstrip() + "\n\n" + markdown + "\n"
    else:
        new_content = content.rstrip() + "\n\n" + markdown + "\n"
    path.write_text(new_content, encoding="utf-8")


def main():
    url_map = json.loads(URL_MAP.read_text(encoding="utf-8"))

    targets = [
        entry for entry in url_map
        if entry.get("locale") == "pl"
        and entry.get("status") == "captured"
        and entry.get("contentFile") is not None
    ]

    print(f"Found {len(targets)} PL pages to crawl.\n")
    success = 0
    skipped = 0
    errors = 0

    for i, entry in enumerate(targets, start=1):
        url = entry["sourceUrl"]
        content_file = PROJECT_ROOT / entry["contentFile"]
        path_label = entry["canonicalPath"]

        print(f"[{i:02d}/{len(targets)}] {path_label}")
        print(f"         → {url}")

        if not content_file.exists():
            print(f"  ERROR: content file not found: {content_file}")
            errors += 1
            continue

        if has_body(content_file):
            print(f"  SKIP: body already present")
            skipped += 1
            continue

        html = fetch_html(url)
        if not html:
            print(f"  ERROR: fetch failed")
            errors += 1
            continue

        markdown = extract_markdown(html)
        if not markdown.strip():
            print(f"  WARN: no content extracted (empty body written)")
        else:
            word_count = len(markdown.split())
            print(f"  OK: {word_count} words extracted")

        append_body(content_file, markdown)
        success += 1

    print(f"\n{'='*50}")
    print(f"Done. Success: {success}  Skipped: {skipped}  Errors: {errors}")


if __name__ == "__main__":
    main()
