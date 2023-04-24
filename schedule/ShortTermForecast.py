import datetime as dt


class ShortTermForecastItem:
    forecast: dict
    fcst_datetime: dt
    category_value: dict

    def __init__(self):
        self.forecast = {}
        self.category_value = {
            "PCP": "",
            "POP": "",
            "PTY": "",
            "REH": "",
            "SKY": "",
            "SNO": "",
            "TMN": "",
            "TMP": "",
            "TMX": "",
            "UUU": "",
            "VEC": "",
            "VVV": "",
            "WAV": "",
            "WSD": ""
        }

    def items_parsing(self, items):
        # print(items)
        for item in items:
            print(item)
            fcst_date = item["fcstDate"]
            fcst_time = item["fcstTime"]

            try:
                fcst_datetime = dt.datetime.strptime(
                    fcst_date + fcst_time, "%Y%m%d%H%M")

                if fcst_datetime in self.forecast.keys():
                    self.category_value[item["category"]] = item["fcstValue"]
                else:
                    self.forecast[fcst_datetime] = self.category_value
                    self.category_value[item["category"]] = item["fcstValue"]
            except ValueError as ve:
                print(f"ValueError: {ve}")

        for i in self.forecast.values():
            print(i)
