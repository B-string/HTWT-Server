import requests
import datetime as dt
import asyncio
import Constant
import json
from ShortTermForecast import ShortTermForecastItem
from DatabaseManager import DatabaseManager


class ForecastService:
    short_term_forecas_item = ShortTermForecastItem()

    manager = DatabaseManager()

    def short_term_forecast(self):
        url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
        page_no = 1
        num_of_rows = 1000
        data_type = "JSON"
        (base_date, base_time) = self.short_term_forecast_time()
        print(base_date, base_time)

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

        items = datas["response"]["body"]["items"]["item"]
        self.short_term_forecas_item.items_parsing(items)

        self.manager.database_connecting(
            Constant.host,
            Constant.port,
            Constant.user,
            Constant.passwd,
            Constant.db
        )
        for key, val in self.short_term_forecas_item.forecast.items():
            self.manager.insert_short_term_forecast(
                table="kr_seoul_61_125", key=key, val=val
            )

        self.manager.database_closing()

    def medium_term_tem_forecast(self):
        url = "http://apis.data.go.kr/1360000/MidFcstInfoService/getMidTa"
        page_no = 1
        num_of_rows = 1000
        data_type = "JSON"
        tm_fc = self.medium_term_forecast_time()

        # 현재 기준: 서울
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
        print(datas)

    def short_term_forecast_time(self) -> tuple:
        today = dt.datetime.now()
        today_date = today.strftime("%Y%m%d")
        hour = int(today.strftime("%H"))
        today_time: str
        if hour >= 14 and hour <= 17:
            today_time = "1400"
        elif hour >= 5 and hour <= 8:
            today_time = "0500"
        else:
            today_time = "0500"
        return (today_date, today_time)

    def medium_term_forecast_time(self) -> str:
        today = dt.datetime.now()
        today_date = today.strftime("%Y%m%d")
        hour = int(today.strftime("%H"))
        today_time: str
        if hour >= 6 and hour < 18:
            today_time = "0600"
        else:
            today_time = "1800"
        return f"{today_date}{today_time}"


def main():
    print("Hello World")
    test = ForecastService()
    # test.short_term_forecast()
    test.medium_term_tem_forecast()


if __name__ == "__main__":
    main()
