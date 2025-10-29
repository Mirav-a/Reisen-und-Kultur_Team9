# services/weather-service/weather_service.py
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/weather/{city}")
def get_weather(city: str):
    return {
        "city": city,
        "weather": random.choice(["sunny", "rainy", "cloudy", "snowy"]),
        "temperature": random.randint(5, 25)
    }
