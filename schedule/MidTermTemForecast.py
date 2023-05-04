import datetime as dt
import copy


class MidTermOutlook:
    base_datetime: str
    stn_id: int
    wf_sv: str


class MidTermTemperature:
    base_datetime: str
    reg_id: str
    ta_min: dict
    ta_min_low: dict
    ta_min_high: dict
    ta_max: dict
    ta_max_low: dict
    ta_max_high: dict

    def __init__(self) -> None:
        self.ta_min = {}
        self.ta_min_low = {}
        self.ta_min_high = {}
        self.ta_max = {}
        self.ta_max_low = {}
        self.ta_max_high = {}


class MidTermForecastItem:
    mid_term_outlook: MidTermOutlook
    mid_term_temperature: MidTermTemperature

    def __init__(self) -> None:
        self.mid_term_outlook = MidTermOutlook()
        self.mid_term_temperature = MidTermTemperature()

    def mid_term_outlook_item_parsing(self, base_datetime, stn_id, parse) -> MidTermOutlook:
        self.mid_term_outlook.base_datetime = base_datetime
        self.mid_term_outlook.stn_id = stn_id
        self.mid_term_outlook.wf_sv = parse[0]["wfSv"]
        return self.mid_term_outlook

    def mid_term_temperature_item_parsing(self, base_datetime, parse: dict) -> MidTermTemperature:
        self.mid_term_temperature.base_datetime = base_datetime
        self.mid_term_temperature.reg_id = parse.pop("regId")

        for key, val in parse.items():
            if "Min" in key and "Low" in key:
                self.mid_term_temperature.ta_min_low[key] = val
            elif "Min" in key and "High" in key:
                self.mid_term_temperature.ta_min_high[key] = val
            elif "Max" in key and "Low" in key:
                self.mid_term_temperature.ta_max_low[key] = val
            elif "Max" in key and "High" in key:
                self.mid_term_temperature.ta_max_high[key] = val
            elif "Max" in key:
                self.mid_term_temperature.ta_max[key] = val
            elif "Min" in key:
                self.mid_term_temperature.ta_min[key] = val
        print(self.mid_term_temperature.ta_max)
        print(self.mid_term_temperature.ta_min)
        print(self.mid_term_temperature.ta_max_low)
        print(self.mid_term_temperature.ta_min_low)
        print(self.mid_term_temperature.ta_max_high)
        print(self.mid_term_temperature.ta_min_high)

        return self.mid_term_temperature
