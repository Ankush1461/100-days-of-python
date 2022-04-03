# Workout Tracker Program

from datetime import datetime

import requests

GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 169
AGE = 21

APP_ID = "YOUR_APP_ID"
API_KEY = "YOUR_API_KEY"

sheety_endpoint = "YOUR_SHEETY_ENDPOINT"
TOKEN = "Bearer 'YOUR_TOKEN'"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Bearer Token Authentication
bearer_headers = {
    "Authorization": TOKEN
}

nutri_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

input_data = input("Tell me what exercises you did: ")

query_params = {
    "query": input_data,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=nutri_exercise_endpoint, json=query_params, headers=headers)
result = response.json()

print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
