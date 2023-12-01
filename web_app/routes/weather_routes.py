
from flask import Blueprint, request, render_template, redirect, flash
from app.weatherapp import get_weather_info, display_forecast,main

weather_routes = Blueprint("weather_routes", __name__)

# Routes for weather functionality
@weather_routes.route("/weather/form")
def weather_form():
    print("WEATHER FORM...")
    return render_template("weather_form.html")


@weather_routes.route("/weather/dashboard", methods=["GET", "POST"])
def weather_dashboard():
    print("WEATHER DASHBOARD...")

    if request.method == "POST":
        zip_code = request.form.get("zip_code") or "06510"
        #zip_code = dict(request.form)
        #print("FORM DATA:", request_data)
    else:
        zip_code = request.args.get("zip_code") or "06510"
        #zip_code = dict(request.args)
        #print("URL PARAMS:", zip_code)

    try:
        periods = get_weather_info(zip_code)
        # Process weather data and prepare for rendering in template
        
        flash("Fetched Weather Forecast!", "success")
        return render_template("weather_dashboard.html", 
                               zip_code = zip_code,
                               periods = periods
                               )
    except Exception as err:
        print('OOPS', err)
        flash("Weather Data Error. Please try again!", "danger")
        return redirect("/weather/form")

# API route for weather information
@weather_routes.route("/api/weather.json")
def weather_api():
    zip_code = request.args.get("zip_code") or "06510"

    try:
        periods = get_weather_info(zip_code)
        # Prepare weather data for JSON response

        return {"zip_code": zip_code, "periods": periods }
    except Exception as err:
        print('OOPS', err)
        return {"message":"Weather Data Error. Please try again."}, 404
