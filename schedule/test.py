import requests
import datetime as dt
import asyncio
import Constant


class ForecastService:

    def short_term_forecast(self):
        url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
        page_no = 1
        num_of_rows = 1000
        data_type = "JSON"
        today = dt.datetime.now()
        (base_date, base_time) = ForecastService.forecast_time(today)
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
        data = res.json()
        print(data)

    def forecast_time(today: dt) -> tuple:
        today = dt.datetime.now()
        today_date = today.strftime("%Y%m%d")
        hour = int(today.strftime("%H"))
        today_hour: str
        if hour >= 14 and hour <= 17:
            today_hour = "1400"
        elif hour >= 5 and hour <= 8:
            today_hour = "0500"
        else:
            today_hour = "0500"
        return (today_date, today_hour)


def main():
    print("Hello World")
    test = ForecastService()
    test.short_term_forecast()


if __name__ == "__main__":
    main()
