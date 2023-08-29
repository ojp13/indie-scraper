import requests

from core.cities.extract_cities import extract_cities
from core.cities.get_cities import get_cities
from core.utils.utils import generate_payloads, generate_weeks


def check_availability(url, payload, headers):
    checkin_city = payload["booking"]["checkin_city"]
    checkout_city = payload["booking"]["checkout_city"]
    checkin_date = payload["booking"]["checkin_datetime"]
    checkout_date = payload["booking"]["checkout_datetime"]

    print(
        f"Checking availability for {checkin_city} to {checkout_city} from {checkin_date} to {checkout_date}."
    )

    response = requests.post(url=url, json=payload, headers=headers)

    options = []

    for option in response.json().get("data", {}).get("availability", []):
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

    weeks = generate_weeks([2024])

    headers = {
        "Content-Type": "application/json",
        "Content-Length": "570",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://indiecampers.co.uk",
        "Referer": "https://indiecampers.co.uk/",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwbGF0Zm9ybSIsImF1ZCI6InBsYXRmb3JtIiwiZXhwIjoxNjk0NTE1NDU2LCJqdGkiOiJhNzk0NTU5YS1kZjgxLTRiZmUtODY1Ny0zMjYzZjQyMjc5ODMiLCJjbGllbnRfYWNjb3VudCI6eyJlbWFpbCI6InBlYWNlLm9zY2FyQGdtYWlsLmNvbSIsIm5hbWUiOiJPc2NhciBQZWFjZSIsImFsbG93X3Bhc3N3b3JkX2NoYW5nZSI6ZmFsc2UsImNvbmZpcm1lZF9hdCI6IjIwMjMtMDEtMjMgMjE6MjA6NTQgKzAwMDAiLCJjcmVhdGVkX2F0IjoiMjAyMy0wMS0yMyAyMToyMDo1NCArMDAwMCIsInNjb3BlIjpbInVzZXIiXX19.MTzHgZLTPgTCJpToEw8iqnfS7Y4Wq4nLGIb2mOCe6oY",
    }

    cities = extract_cities(get_cities())

    payloads = generate_payloads(cities, weeks)

    options = []

    for payload in payloads:
        options.append(check_availability(url, payload, headers))

    print(options)


if __name__ == "__main__":
    main()
