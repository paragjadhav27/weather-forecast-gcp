import requests
import os
import json
from google.cloud import pubsub_v1
from datetime import datetime

# Get API key and project ID from environment variables
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
GCP_PROJECT = os.environ.get("GCP_PROJECT")

# List of cities you want to monitor
CITIES = ["Mumbai", "New York", "London"]

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    return {
        "city": city,
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "timestamp": datetime.utcnow().isoformat()
    }

def fetch_weather(request):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(GCP_PROJECT, "weather-topic")

    for city in CITIES:
        weather_data = get_weather(city)
        message = json.dumps(weather_data).encode("utf-8")
        publisher.publish(topic_path, message)

    return "Weather data published successfully."