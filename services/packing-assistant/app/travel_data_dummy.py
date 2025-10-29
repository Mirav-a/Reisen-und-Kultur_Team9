dummy_data = {
    "Barcelona": {
        "temperature": 22,
        "weather": "sonnig",
        "season": "Frühling"
    },
    "Berlin": {
        "temperature": 16,
        "weather": "regnerisch",
        "season": "Herbst"
    },
    "Oslo": {
        "temperature": 3,
        "weather": "kalt",
        "season": "Winter"
    }
}

def get_travel_data(city: str) -> dict:
    return dummy_data.get(city, {
        "temperature": 20,
        "weather": "wechselhaft",
        "season": "unbekannt"
    })
