import datetime as dt
import copy
import pymysql


class ShortTermForecastItem:
    forecast: dict
    fcst_datetime: dt
    category_value: dict

    def __init__(self):
        self.forecast = {}
        self.category_value = {
            "PCP": "",  # 1시간 강수량 (mm)
            "POP": "",  # 강수 확률 (%)
            "PTY": "",  # 강수 형태 (코드값)
            "REH": "",  # 습도 (%)
            "SKY": "",  # 하늘 상태 (코드값)
            "SNO": "",  # 1시간 신적설 (cm)
            "TMN": "",  # 일 최저기온 (℃)
            "TMP": "",  # 1시간 기온 (℃)
            "TMX": "",  # 일 최고기온 (℃)
            "UUU": "",  # 풍속(동서성분) (m/s)
            "VEC": "",  # 풍향 (deg)
            "VVV": "",  # 풍속(남북성분) (m/s)
            "WAV": "",  # 파고 (M)
            "WSD": ""  # 풍속 (m/s)
        }

    def items_parsing(self, items):
        # print(items)
        for item in items:
            fcst_date = item["fcstDate"]
            fcst_time = item["fcstTime"]

            try:
                # fcst_datetime = dt.datetime.strptime(
                # fcst_date + fcst_time, "%Y%m%d%H%M")
                fcst_datetime = fcst_date + fcst_time
                if fcst_datetime in self.forecast.keys():
                    self.forecast[fcst_datetime][item["category"]
                                                 ] = item["fcstValue"]
                else:
                    self.forecast[fcst_datetime] = copy.deepcopy(
                        self.category_value)
                    self.forecast[fcst_datetime][item["category"]
                                                 ] = item["fcstValue"]
            except ValueError as ve:
                print(f"ValueError: {ve}")

        # for key, val in self.forecast.items():
        #     print(f"{key} : {val}")
