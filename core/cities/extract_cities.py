import json


def extract_cities(city_data):
    # city_ids = [
    #     data["id"]
    #     for data in city_data["city_card"]
    #     if data["links"]["country"]["uid"] == "usa"
    # ]

    city_ids = []

    for city_key in city_data["city_card"]:
        if city_data["city_card"][city_key]["links"]["country"]["uid"] == "usa":
            city_ids.append(city_data["city_card"][city_key]["id"])

    return city_ids


if __name__ == "__main__":
    cities = extract_cities()

    with open("cities.json", "w", encoding="utf-8") as f:
        json.dump(cities, f, ensure_ascii=False, indent=4)
