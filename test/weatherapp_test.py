
from app.weatherapp import get_weather_info, display_forecast, main


def test_get_weather_info():
    result = get_weather_info("20057")
    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], dict)
   

