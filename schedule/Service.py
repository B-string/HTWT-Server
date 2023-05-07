import requests
import datetime as dt
import asyncio
import ScheduleConstant as Constant
import json
from ShortTermForecastItem import ShortTermForecastItem
from MidTermTemForecast import MidTermForecastItem
from DatabaseManager import DatabaseManager


class ForecastService:
    short_term_weather_item: ShortTermForecastItem
    mid_term_forecast_item: MidTermForecastItem

    manager: DatabaseManager

    def __init__(self) -> None:
        self.short_term_forecast_item = ShortTermForecastItem()
        self.mid_term_forecast_item = MidTermForecastItem()

        self.manager = DatabaseManager()
        self.manager.database_connecting(
            Constant.host,
            Constant.port,
            Constant.user,
            Constant.passwd,
            Constant.db
        )
        self.manager.init_table()
        # self.manager.database_closing()

    def insert_forecast(self) -> None:
        self.short_term_forecast()
        self.mid_term_forecast()

    def short_term_forecast(self):
        url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
        page_no = 1
        num_of_rows = 1000
        data_type = "JSON"
        (base_date, base_time) = self.short_term_forecast_time()

        # 현재 기준 : 양재동
        nx = 61
        ny = 125

        params = {
            "ServiceKey": Constant.api_key,
            "pageNo": page_no,
            "numOfRows": num_of_rows,
            "dataType": data_type,
            "base_date": base_date,
            "base_time": base_time,
            "nx": nx,
            "ny": ny
        }

        res = requests.get(url=url, params=params)
        datas = res.json()

        parse: list = datas["response"]["body"]["items"]["item"]
        today = base_date + base_time
        items = self.short_term_forecast_item.data_parsing(parse)

        self.manager.insert_short_term_forecast(items)

    def mid_term_forecast(self):
        self.mid_term_forecast_outlook()
        self.mid_term_forecast_temperature()

    def mid_term_forecast_outlook(self):
        url = "http://apis.data.go.kr/1360000/MidFcstInfoService/getMidFcst"
        page_no = 1
        num_of_rows = 1000
        data_type = "JSON"
        tm_fc = self.mid_term_forecast_time()

        # 현재 기준: 서울
        stn_id = "109"

        params = {
            "ServiceKey": Constant.api_key,
            "pageNo": page_no,
            "numOfRows": num_of_rows,
            "dataType": data_type,
            "stnId": stn_id,
            "tmFc": tm_fc
        }

        res = requests.get(url=url, params=params)
        datas = res.json()
        parse = datas["response"]["body"]["items"]["item"]
        item = self.mid_term_forecast_item.mid_term_outlook_item_parsing(
            tm_fc, stn_id, parse)
        self.manager.insert_mid_term_outlook(item)

    def mid_term_forecast_temperature(self):
        url = "http://apis.data.go.kr/1360000/MidFcstInfoService/getMidTa"
        page_no = 1
        num_of_rows = 1000
        data_type = "JSON"
        tm_fc = self.mid_term_forecast_time()
        reg_id = "11B10101"
        params = {
            "ServiceKey": Constant.api_key,
            "pageNo": page_no,
            "numOfRows": num_of_rows,
            "dataType": data_type,
            "regId": reg_id,
            "tmFc": tm_fc
        }
        res = requests.get(url=url, params=params)
        datas = res.json()
        parse = datas["response"]["body"]["items"]["item"][0]
        item = self.mid_term_forecast_item.mid_term_temperature_item_parsing(
            tm_fc, parse)

        self.manager.insert_mid_term_temperature(item)

    def short_term_forecast_time(self) -> tuple:
        today = dt.datetime.now()
        today_date = today.strftime("%Y%m%d")
        hour = int(today.strftime("%H"))
        today_time: str
        if hour >= 5 and hour <= 8:
            today_time = "0500"
        elif hour >= 2 and hour <= 5:
            today_time = "0200"
        else:
            today_time = "0200"
        return (today_date, today_time)

    def mid_term_forecast_time(self) -> str:
        today = dt.datetime.now()
        today_date = today.strftime("%Y%m%d")
        hour = int(today.strftime("%H"))
        today_time: str
        if hour >= 6 and hour < 18:
            today_time = "0600"
        else:
            today_time = "1800"
        return f"{today_date}{today_time}"

    def cut_list(self, data: list, count: int) -> list:
        new_data: list = []
        for i in range(0, count):
            new_data.append(data.pop(0))
        return new_data

    def __del__(self):
        self.manager.database_closing()


def main():
    print("Hello World")
    forecast_service = ForecastService()
    forecast_service.insert_forecast()
    # test.short_term_forecast()
    # test.mid_term_forecast()


if __name__ == "__main__":
    main()
