import datetime as dt
import copy
import pymysql


class ShortTermWeatherData:

    weather_data: dict
    switch_case: dict
    """
    base_datetime DATETIME NOT NULL,
    fcst_datetime DATETIME NOT NULL,
    location POINT NOT NULL,
    temperature INT,
    max_temperature FLOAT,
    min_temperature FLOAT,
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
        self.weather_data = {
            "base_datetime": "",
            "fcst_datetime": "",
            "nx": 0,
            "ny": 0,
            "temperature": 0.0,  # tmp
            "max_temperature": 0.0,  # tmx
            "min_temperature": 0.0,  # tmn
            "u_wind": 0.0,  # uuu
            "v_wind": 0.0,  # vvv
            "wind_direction": 0,  # vec
            "wind_speed": 0.0,  # wsd
            "sky_condition": 0,  # sky
            "precipitation_type": 0,  # pty
            "probability_of_precipitation": 0,  # pop
            "wave_height": 0,  # wav
            "precipitation_amount": "",  # pcp
            "relative_humidity": 0,  # reh
            "snowfall_amount": ""  # sno
        }

        self.switch_case = {
            "tmp": "temperature",
            "tmx": "max_temperature",
            "tmn": "min_temperature",
            "uuu": "u_wind",  # uuu
            "vvv": "v_wind",  # vvv
            "vec": "wind_direction",  # vec
            "wsd": "wind_speed",  # wsd
            "sky": "sky_condition",  # sky
            "pty": "precipitation_type",  # pty
            "pop": "probability_of_precipitation",  # pop
            "wav": "wave_height",  # wav
            "pcp": "precipitation_amount",  # pcp
            "reh": "relative_humidity",  # reh
            "sno": "snowfall_amount"  # sno
        }

    def data_parsing(self, base_datetime, parse) -> list:
        forecast = []
        self.weather_data["base_datetime"] = base_datetime

        for data in parse:
            fcst_datetime = data["fcstDate"] + data["fcstTime"]

            if self.weather_data["fcst_datetime"] == "":
                self.weather_data["fcst_datetime"] = fcst_datetime
                self.weather_data["nx"] = data["nx"]
                self.weather_data["ny"] = data["ny"]
                category: str = data["category"]
                self.weather_data[self.switch_case.get(
                    category.lower())] = data["fcstValue"]
            else:
                if self.weather_data["fcst_datetime"] == fcst_datetime:
                    category: str = data["category"]
                    self.weather_data[self.switch_case.get(
                        category.lower())] = data["fcstValue"]
                    print(type(data["fcstValue"]))
                else:

                    forecast.append(copy.deepcopy(self.weather_data))
                    self.weather_data["fcst_datetime"] = fcst_datetime

        return forecast
