import datetime as dt
import copy
import pymysql


class ShortTermWeatherData:
    base_datetime: str
    fcst_datetime: str
    nx: int
    ny: int
    temperature: float
    max_temperature: float
    min_temperature: float
    u_wind: float
    v_wind: float
    wind_direction: float
    wind_speed: float
    sky_condition: float
    precipitation_type: float
    probability_of_precipitation: float
    wave_height: float
    precipitation_amount: str
    relative_humidity: float
    snowfall_amount: str

    def __init__(self) -> None:
        self.base_datetime = ""
        self.fcst_datetime = ""
        self.nx = 0
        self.ny = 0
        self.temperature = 0.0
        self.max_temperature = 0.0
        self.min_temperature = 0.0
        self.u_wind = 0.0
        self.v_wind = 0.0
        self.wind_direction = 0.0
        self.wind_speed = 0.0
        self.sky_condition = 0.0
        self.precipitation_type = 0.0
        self.probability_of_precipitation = 0.0
        self.wave_height = 0.0
        self.precipitation_amount = ""
        self.relative_humidity = 0.0
        self.snowfall_amount = ""

    def print_data(self):
        print(self.base_datetime)
        print(self.fcst_datetime)
        print(self.nx)
        print(self.ny)
        print(self.temperature)
        print(self.max_temperature)
        print(self.min_temperature)
        print(self.u_wind)
        print(self.v_wind)
        print(self.wind_direction)
        print(self.wind_speed)
        print(self.sky_condition)
        print(self.precipitation_type)
        print(self.probability_of_precipitation)
        print(self.wave_height)
        print(self.precipitation_amount)
        print(self.relative_humidity)
        print(self.snowfall_amount)


class ShortTermForecastItem:

    def data_parsing(self, parse) -> list:
        short_term_weather_datas = []
        stwd = ShortTermWeatherData()

        for item in parse:
            stwd.base_datetime = item.get("baseDate") + item.get("baseTime")
            fcst_datetime = item.get("fcstDate") + item.get("fcstTime")
            if stwd.fcst_datetime == "":
                stwd.nx = item.get("nx")
                stwd.ny = item.get("ny")
                stwd.fcst_datetime = fcst_datetime

                # self.weather_data[self.switch_case.get(
                #     category.lower())] = data["fcstValue"]
            elif stwd.fcst_datetime != fcst_datetime:
                short_term_weather_datas.append(stwd)
                stwd = ShortTermWeatherData()

            if item.get("category").lower() == 'tmp':
                stwd.temperature = item.get("fcstValue")
            elif item.get("category").lower() == 'tmx':
                stwd.max_temperature = item.get("fcstValue")
            elif item.get("category").lower() == 'tmn':
                stwd.min_temperature = item.get("fcstValue")
            elif item.get("category").lower() == 'uuu':
                stwd.u_wind = item.get("fcstValue")
            elif item.get("category").lower() == 'vvv':
                stwd.v_wind = item.get("fcstValue")
            elif item.get("category").lower() == 'vec':
                stwd.wind_direction = item.get("fcstValue")
            elif item.get("category").lower() == 'wsd':
                stwd.wind_speed = item.get("fcstValue")
            elif item.get("category").lower() == 'sky':
                stwd.sky_condition = item.get("fcstValue")
            elif item.get("category").lower() == 'pty':
                stwd.precipitation_type = item.get("fcstValue")
            elif item.get("category").lower() == 'pop':
                stwd.probability_of_precipitation = item.get("fcstValue")
            elif item.get("category").lower() == 'wav':
                stwd.wave_height = item.get("fcstValue")
            elif item.get("category").lower() == 'pcp':
                stwd.precipitation_amount = item.get("fcstValue")
            elif item.get("category").lower() == 'reh':
                stwd.relative_humidity = item.get("fcstValue")
            elif item.get("category").lower() == 'sno':
                stwd.snowfall_amount = item.get("fcstValue")

        return short_term_weather_datas
