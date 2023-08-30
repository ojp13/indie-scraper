from datetime import datetime, timedelta
from typing import List


def generate_weeks(years: List[int]):
    # Generate weekly slices of data, with the start of the week as the first monday and
    # the end of the week as the next Monday

    weeks = []

    for year in years:
        # Find first monday of year
        first_day = find_first_monday(year)

        weeks_in_year = [
            {
                "start_day": datetime.strftime(
                    first_day + i * timedelta(7), "%Y-%m-%dT16:30:00+00:00"
                ),
                "end_day": datetime.strftime(
                    first_day + (i + 1) * timedelta(7), "%Y-%m-%dT11:00:00+00:00"
                ),
            }
            for i in range(0, 52)
        ]

        weeks.append(weeks_in_year)

    return [dates for year in weeks for dates in year]


def find_first_monday(year):
    d = datetime(year, 1, 1)
    offset = 0 - d.weekday()  # weekday = 0 means monday
    if offset < 0:
        offset += 7
    return d + timedelta(offset)


def generate_payloads(cities, weeks):
    base_payload = {
        "booking": {
            "page": 1,
            "locale": "gb",
            "van_categories": [
                "sierra",
                "conquest",
                "ovation",
                "applause",
                "nomad-pop-top",
                "four-winds",
                "marco-polo",
                "vw-california-premium",
                "atlas-5",
                "california",
                "solis-air",
                "sporty",
                "atlas",
                "nomad-ivy",
                "nomad",
                "metris",
                "etrusco",
                "active-plus",
                "wrangler",
                "tellaro",
                "rebel",
                "solis",
                "vw-grand-california",
                "california-manual",
                "dawn-patrol",
                "urban",
                "explorer",
            ],
        },
        "meta": {"current_route": "rent-an-rv-search"},
    }

    cities_subpayload = [
        {
            "checkin_city": city,
            "checkout_city": city,
        }
        for city in cities
    ]

    dates_subpayload = [
        {
            "checkin_datetime": week["start_day"],
            "checkout_datetime": week["end_day"],
        }
        for week in weeks
    ]

    payloads = [
        {
            "booking": {
                **base_payload["booking"],
                **city_subpayload,
                **date_subpayload,
            },
            "meta": {**base_payload["meta"]},
        }
        for city_subpayload in cities_subpayload
        for date_subpayload in dates_subpayload
    ]

    return payloads


def get_token():
    with open("token.txt", "r") as file:
        token = file.read()

    return token
