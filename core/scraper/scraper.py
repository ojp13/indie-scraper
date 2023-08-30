import json
from datetime import datetime
from pathlib import Path

import requests

from core.cities.extract_cities import extract_cities
from core.cities.get_cities import get_cities
from core.utils.utils import generate_months, generate_payloads, get_token


def check_availability(url, payload, headers):
    checkin_city = payload["booking"]["checkin_city"]
    checkout_city = payload["booking"]["checkout_city"]
    checkin_date = payload["booking"]["checkin_datetime"]
    checkout_date = payload["booking"]["checkout_datetime"]

    print(
        f"Checking availability for {checkin_city} to {checkout_city} from {checkin_date} to {checkout_date}."
    )

    response = requests.post(url=url, json=payload, headers=headers)

    if response.status_code != 200:
        print(f"Issue with request, received status code {response.status_code} \n")
        return []

    data = json.loads(response.content.decode("utf-8"))

    options = []

    for option in data.get("data", {}).get("availability", []):
        if option["available"]:
            options.append(
                {
                    "van": option["van_category"],
                    "total_price": option["total_cost"],
                    "start_date": option["criteria"]["checkin_datetime"],
                    "end_date": option["criteria"]["checkout_datetime"],
                    "start_city": option["criteria"]["checkin_city"],
                    "end_city": option["criteria"]["checkout_city"],
                }
            )

    if len(options) == 0:
        print("No options found \n")
    else:
        print(f"Found options: {options} \n")

    return options


def main():
    url = "https://indiecampers.com/api/v3/availability"

    weeks = generate_months([2023, 2024])

    token = get_token()

    headers = {
        "Content-Type": "application/json",
        "Content-Length": "570",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Origin": "https://indiecampers.co.uk",
        "Referer": "https://indiecampers.co.uk/",
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }

    cities = extract_cities(get_cities())

    payloads = generate_payloads(cities, weeks)

    options = []

    for payload in payloads:
        new_options = check_availability(url, payload, headers)

        for option in new_options:
            options.append(option)

    json_object = json.dumps(options, indent=4)

    filename = f"results_{datetime.strftime(datetime.today(), '%Y%m%dT%H%M%S')}.json"

    results_folder_path = Path(".") / "results"

    with open(results_folder_path / filename, "w") as outfile:
        outfile.write(json_object)


if __name__ == "__main__":
    main()
