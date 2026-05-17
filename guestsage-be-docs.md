# GuestSage Booking Engine Integration Notes

## 1. Booking engine link

https://be.guestsage.com/pl/0bf0dc4c-089f-42f4-8bf0-3ea22a76ad8a

## 2. How to redirect to a different language version of the engine

It's best and cleanest if your website has separate subpages for different language versions, e.g., /pl/, /en/, /de/, etc. In this case, simply set the appropriate language code in the link to the booking engine, matching the website version.

Example: Polish website (/pl/) - https://be.guestsage.com/pl/{YOUR_HASH}

We recommend that on each language version of your website, the link (or iframe) leads to the booking engine with the same language code as the page they're on. This way, the user will immediately see the offer in their chosen language.

## 3. Adding URL Parameters (Dates, People, Rooms, etc.)

To redirect guests to specific dates, offers, or rooms, we need to use additional parameters, which are added to the base URL.

### Available parameters

- arrivalDate – arrival date (start of booking), entered in the YYYY-MM-DD format, e.g., arrivalDate=2025-04-17
- departureDate – departure date (end of booking), entered in the YYYY-MM-DD format, e.g., departureDate=2025-04-19
- personsCount – number of adults, e.g., personsCount=2
- ageCategoryCounts – number of children in specific age groups, e.g., ageCategoryCounts=[{"ageCategoryId":70,"count":1}], where ageCategoryId is the age group ID and count is the number of people in a given category. featuredRatePlanId – the specific rate plan to be displayed, e.g.: featuredRatePlanId=4635
- featuredRoomTypeId – the specific room to be displayed, e.g.: featuredRoomTypeId=8739
- discountCodeName – the discount code, e.g.: discountCodeName=KOD30
- filterCategoryId – the category filter

### How to use this?

To add parameters to the link, we use the following rule:

Added to the base link: /offers?

This indicates that we will be searching for specific offers. Then, we enter the first parameter, e.g., the arrival date of April 17, 2025:

```text
https://be.guestsage.com/pl/{YOUR_HASH}/offers?arrivalDate=2025-04-17
```

To enter the next parameter, we need to separate it with the ampersand (&). This will be done the same way for each subsequent parameter. So let's add two new parameters: departure date and number of people.

```text
https://be.guestsage.com/pl/{TWÓJ_HASH}/offers?arrivalDate=2025-04-17&departureDate=2025-04-19&personsCount=3
```

Note: If you decide to use additional parameters, your link must include at least the arrival date, departure date, and number of people.

Where to find room IDs, rate plans, or age groups—ASK THE USER!

## Examples Use

```text
https://be.guestsage.com/pl/{HASH}/offers?arrivalDate=2025-04-17&departureDate=2025-04-19&personsCount=3
```

```text
https://be.guestsage.com/pl/{HASH}/offers?arrivalDate=2025-04-17&departureDate=2025-04-19&personsCount=3&featuredRoomTypeId=8739
```

```text
https://be.guestsage.com/pl/{HASH}/offers?arrivalDate=2025-04-17&departureDate=2025-04-19&personsCount=3&featuredRatePlanId=4635
```

```text
h ttps://be.guestsage.com/pl/{HASH}/offers?arrivalDate=2025-04-17&departureDate=2025-04-19&personsCount=3&featuredRoomTypeId=8739&featuredRatePlanId=4635
```

```text
https://be.guestsage.com/pl/{HASH}/offers?arrivalDate=2025-04-17&departureDate=2025-04-19&personsCount=1&featuredRoo mTypeId=8739&featuredRatePlanId=4635&ageCategoryCounts=[{"ageCategoryId":21,"count":1},{"ageCategoryId":1,"count":1}]
```
