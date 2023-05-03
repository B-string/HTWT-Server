import datetime as dt
import copy


class MidTermOutlook:
    weather_data: dict

    def __init__(self) -> None:
        self.weather_data = {
            "base_datetime": "",
            "stn_id": 0,
            "wf_sv": ""
        }


class MidTermForecastItem:
    mid_term_outlook: MidTermOutlook

    def __init__(self) -> None:
        self.mid_term_outlook = MidTermOutlook()

    def mid_term_outlook_item_parsing(self, base_datetime, stn_id, parse) -> dict:
        self.mid_term_outlook.weather_data["base_datetime"] = base_datetime
        self.mid_term_outlook.weather_data["stn_id"] = stn_id
        self.mid_term_outlook.weather_data["wf_sv"] = parse[0]["wfSv"]
        return self.mid_term_outlook.weather_data
