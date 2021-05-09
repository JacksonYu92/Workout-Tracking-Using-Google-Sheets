import os
import requests
from datetime import datetime

application_id = os.environ['APP_ID']
application_keys = os.environ['APP_KEYS']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
token = os.environ['TOKEN']

workout = input("Tell me which exercises you did: ").lower()

nutritionix_endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"
workouts_endpoints = os.environ["SHEETY_ENDPOINTS"]

parameters = {
    "query": workout,
    "gender": "male",
    "weight_kg": 68.0,
    "height_cm": 174.5,
    "age": 29
}

headers = {
    "x-app-id": application_id,
    "x-app-key": application_keys,
}

response = requests.post(url=nutritionix_endpoints, json=parameters, headers=headers)
nutrition_result = response.json()
print(nutrition_result)

for exercise in nutrition_result["exercises"]:
    data = {"workout":
        {
        "date": datetime.today().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%X"),
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
    }}

    sheety_headers = {
        "Authorization": f"Bearer {token}",
    }

    # workout_response = requests.get(url=workouts_endpoints)
    # workout_response.raise_for_status()
    # print(workout_response.json())


    post_workout = requests.post(url=workouts_endpoints, json=data, headers=sheety_headers)
    print(post_workout.text)