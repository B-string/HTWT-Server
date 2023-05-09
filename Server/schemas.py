from typing import List
from pydantic import BaseModel
from datetime import datetime


class ShortTermForecast(BaseModel):
    id: int
    base_datetime: datetime
    fcst_datetime: datetime
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

    class Config:
        orm_mode = True


class ShortTermForecastList(BaseModel):
    forecasts: List[ShortTermForecast]


class MidTermTemperature(BaseModel):
    id: int
    base_datetime: datetime
    reg_id: str

    taMax3: int
    taMax3High: int
    taMax3Low: int
    taMax4: int
    taMax4High: int
    taMax4Low: int
    taMax5: int
    taMax5High: int
    taMax5Low: int
    taMax6: int
    taMax6High: int
    taMax6Low: int
    taMax7: int
    taMax7High: int
    taMax7Low: int
    taMax8: int
    taMax8High: int
    taMax8Low: int
    taMax9: int
    taMax9High: int
    taMax9Low: int
    taMax10: int
    taMax10High: int
    taMax10Low: int

    taMin3: int
    taMin3High: int
    taMin3Low: int
    taMin4: int
    taMin4High: int
    taMin4Low: int
    taMin5: int
    taMin5High: int
    taMin5Low: int
    taMin6: int
    taMin6High: int
    taMin6Low: int
    taMin7: int
    taMin7High: int
    taMin7Low: int
    taMin8: int
    taMin8High: int
    taMin8Low: int
    taMin9: int
    taMin9High: int
    taMin9Low: int
    taMin10: int
    taMin10High: int
    taMin10Low: int

    class Config:
        orm_mode = True


class MidTermOutlook(BaseModel):
    id: int
    base_datetime: datetime
    stn_id: int
    wf_sv: str

    class Config:
        orm_mode = True
