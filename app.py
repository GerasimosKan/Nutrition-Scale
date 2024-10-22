import os

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request
from requests.auth import HTTPBasicAuth

# Load environment variables
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

app = Flask(__name__)


def get_access_token():
    token_url = "https://oauth.fatsecret.com/connect/token"
    data = {"grant_type": "client_credentials", "scope": "basic"}

    response = requests.post(
        token_url, data=data, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    )

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("Error getting token:", response.status_code, response.text)
        return None


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    nutrition_info = None  # To hold nutritional information

    if request.method == "POST":
        search_term = request.form.get("search_term")

        # Get access token
        access_token = get_access_token()

        if access_token:
            headers = {"Authorization": f"Bearer {access_token}"}
            search_url = "https://platform.fatsecret.com/rest/server.api"
            params = {
                "method": "foods.search",
                "search_expression": search_term,
                "format": "json",
            }

            response = requests.get(search_url, headers=headers, params=params)
            if response.status_code == 200:
                results = response.json().get("foods", {}).get("food", [])
            else:
                print("Error:", response.status_code, response.text)

        # If a food_id and weight are provided, calculate nutrition
        food_id = request.form.get("food_id")
        weight = request.form.get("weight")

        if food_id and weight:
            weight = float(weight)
            detail_url = "https://platform.fatsecret.com/rest/server.api"
            params = {
                "method": "food.get",
                "food_id": food_id,
                "format": "json",
            }

            response = requests.get(detail_url, headers=headers, params=params)
            if response.status_code == 200:
                food_detail = response.json().get("food", {})
                print("Food detail response:", food_detail)  # Debug print

                # Accessing the servings data
                servings = food_detail.get("servings", {}).get("serving", [])
                if servings:
                    # Assuming we take the first serving as default
                    serving = servings[0]  # You can modify this logic as needed

                    # Now extract the nutritional data from the serving
                    calories = float(serving.get("calories", 0))
                    fat = float(serving.get("fat", 0))
                    carbs = float(
                        serving.get("carbohydrate", 0)
                    )  # Correct key for carbohydrates
                    protein = float(serving.get("protein", 0))

                    # Calculate nutrition based on the weight
                    calories = (
                        calories / float(serving.get("metric_serving_amount", 100))
                    ) * weight
                    fat = (
                        fat / float(serving.get("metric_serving_amount", 100))
                    ) * weight
                    carbs = (
                        carbs / float(serving.get("metric_serving_amount", 100))
                    ) * weight
                    protein = (
                        protein / float(serving.get("metric_serving_amount", 100))
                    ) * weight

                    nutrition_info = {
                        "food_name": food_detail.get("food_name"),
                        "calories": round(
                            calories, 2
                        ),  # Rounding for better presentation
                        "fat": round(fat, 2),
                        "carbs": round(carbs, 2),
                        "protein": round(protein, 2),
                    }
                else:
                    print("No servings found for this food item.")
            else:
                print(
                    "Error getting food details:", response.status_code, response.text
                )

    return render_template("index.html", results=results, nutrition_info=nutrition_info)


if __name__ == "__main__":
    app.run(debug=True)
