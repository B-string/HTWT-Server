from pydantic import BaseModel
from datetime import datetime


class ShortBase(BaseModel):
    id: int
    base_datetime: datetime
    fcst_datetime: datetime
    nx: int
    ny: int


class ShortTermForecast(ShortBase):
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
