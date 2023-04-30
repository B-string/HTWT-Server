import datetime as dt
import copy


class MediumTermForecastItem:
    forecast: dict
    ta_data: dict
    land_data: dict

    def __init__(self):
        self.forecast = {}

    def items_parsing(self, type: str, items: dict, tm_fc: str):

        if type == "ta":

            # self.forecast["type"] = type
            # self.forecast["date"] = tm_fc
            # self.forecast["data"] =
            pass
        elif type == "ld":
            pass
        elif type == "sea":
            pass
        else:
            pass
