import requests


def make_request(url, payload, headers):
    response = requests.post(url, payload, headers)

    print(response.json())


def main():
    url = "https://indiecampers.com/api/v3/availability"

    payload = {
        "booking": {
            "checkin_city": "orlando",
            "checkout_city": "orlando",
            "checkin_datetime": "2023-09-04T16:30:00+00:00",
            "checkout_datetime": "2023-10-16T11:00:00+00:00",
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

    headers = {
        "Content-Type": "application/json",
        "Content-Length": "570",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://indiecampers.co.uk",
        "Referer": "https://indiecampers.co.uk/",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwbGF0Zm9ybSIsImF1ZCI6InBsYXRmb3JtIiwiZXhwIjoxNjk0NTE1NDU2LCJqdGkiOiJhNzk0NTU5YS1kZjgxLTRiZmUtODY1Ny0zMjYzZjQyMjc5ODMiLCJjbGllbnRfYWNjb3VudCI6eyJlbWFpbCI6InBlYWNlLm9zY2FyQGdtYWlsLmNvbSIsIm5hbWUiOiJPc2NhciBQZWFjZSIsImFsbG93X3Bhc3N3b3JkX2NoYW5nZSI6ZmFsc2UsImNvbmZpcm1lZF9hdCI6IjIwMjMtMDEtMjMgMjE6MjA6NTQgKzAwMDAiLCJjcmVhdGVkX2F0IjoiMjAyMy0wMS0yMyAyMToyMDo1NCArMDAwMCIsInNjb3BlIjpbInVzZXIiXX19.MTzHgZLTPgTCJpToEw8iqnfS7Y4Wq4nLGIb2mOCe6oY",
    }

    make_request(url, payload, headers)


if __name__ == "__main__":
    main()
