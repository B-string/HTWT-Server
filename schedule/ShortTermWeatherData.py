import datetime as dt
import copy
import pymysql


class ShortTermWeatherData:

    weather_data: dict
    """
    base_datetime DATETIME NOT NULL,
    fcst_datetime DATETIME NOT NULL,
    location POINT NOT NULL,
    temperature INT,
    u_wind FLOAT,
    v_wind FLOAT,
    wind_direction INT,
    wind_speed FLOAT,
    sky_condition INT,
    precipitation_type INT,
    probability_of_precipitation INT,
    wave_height INT,
    precipitation_amount VARCHAR(10),
    relative_humidity INT,
    snowfall_amount VARCHAR(10)
    """

    def __init__(self) -> None:
        self.weather_data = {}

    def data_parsing(self, base_datetime, parse) -> dict:
        self.weather_data["base_datetime"] = base_datetime

        for data in parse:
            self.weather_data
            for key, val in data.items():
                print(key)
                print(val)

        return {}
