import datetime as dt
import copy


class MediumTermForecastItem:
    forecast: dict
    ta_data: dict
    land_data: dict

    def __init__(self):
        self.forecast = {}
        self.ta_data = {
            "taMin3": "",
            "taMax3": "",
            "taMin4": "",
            "taMax4": "",
            "taMin5": "",
            "taMax5": "",
            "taMin6": "",
            "taMax6": "",
            "taMin7": "",
            "taMax7": "",
            "taMin8": "",
            "taMax8": "",
            "taMin9": "",
            "taMax9": "",
            "taMin10": "",
            "taMax10": ""
        }

    def items_parsing(self, type: str, items: dict):

        if type == "ta":
            forecast_day = 3
            for key, val in items.items():
                if key == f"taMin{forecast_day}":
                    self.ta_data[f"taMin{forecast_day}"] = val
                    continue
                if key == f"taMax{forecast_day}":
                    self.ta_data[f"taMax{forecast_day}"] = val
                    forecast_day += 1
            today = dt.datetime.now().strftime("%Y%m%d%H%M")
            self.forecast[type] = {today: ""}
            self.forecast[type][today] = copy.deepcopy(self.ta_data)
        elif type == "ld":
            pass
        elif type == "sea":
            pass
        else:
            pass
