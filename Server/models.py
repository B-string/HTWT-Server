from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from database import Base


class ShortTermForecast(Base):
    __tablename__ = "short_term_weather_data"

    id = Column(Integer, primary_key=True)
    base_datetime = Column(DateTime)
    fcst_datetime = Column(DateTime)
    nx = Column(Integer)
    ny = Column(Integer)
    temperature = Column(Float)
    max_temperature = Column(Float)
    min_temperature = Column(Float)
    u_wind = Column(Float)
    v_wind = Column(Float)
    wind_direction = Column(Float)
    wind_speed = Column(Float)
    sky_condition = Column(Float)
    precipitation_type = Column(Float)
    probability_of_precipitation = Column(Float)
    wave_height = Column(Float)
    precipitation_amount = Column(String)
    relative_humidity = Column(Float)
    snowfall_amount = Column(String)


class MidTermTemperature(Base):

    __tablename__ = "mid_term_temperature"

    id = Column(Integer, primary_key=True)
    base_datetime = Column(DateTime)
    reg_id = Column(String)

    taMax3 = Column(Integer)
    taMax3High = Column(Integer)
    taMax3Low = Column(Integer)
    taMax4 = Column(Integer)
    taMax4High = Column(Integer)
    taMax4Low = Column(Integer)
    taMax5 = Column(Integer)
    taMax5High = Column(Integer)
    taMax5Low = Column(Integer)
    taMax6 = Column(Integer)
    taMax6High = Column(Integer)
    taMax6Low = Column(Integer)
    taMax7 = Column(Integer)
    taMax7High = Column(Integer)
    taMax7Low = Column(Integer)
    taMax8 = Column(Integer)
    taMax8High = Column(Integer)
    taMax8Low = Column(Integer)
    taMax9 = Column(Integer)
    taMax9High = Column(Integer)
    taMax9Low = Column(Integer)
    taMax10 = Column(Integer)
    taMax10High = Column(Integer)
    taMax10Low = Column(Integer)

    taMin3 = Column(Integer)
    taMin3High = Column(Integer)
    taMin3Low = Column(Integer)
    taMin4 = Column(Integer)
    taMin4High = Column(Integer)
    taMin4Low = Column(Integer)
    taMin5 = Column(Integer)
    taMin5High = Column(Integer)
    taMin5Low = Column(Integer)
    taMin6 = Column(Integer)
    taMin6High = Column(Integer)
    taMin6Low = Column(Integer)
    taMin7 = Column(Integer)
    taMin7High = Column(Integer)
    taMin7Low = Column(Integer)
    taMin8 = Column(Integer)
    taMin8High = Column(Integer)
    taMin8Low = Column(Integer)
    taMin9 = Column(Integer)
    taMin9High = Column(Integer)
    taMin9Low = Column(Integer)
    taMin10 = Column(Integer)
    taMin10High = Column(Integer)
    taMin10Low = Column(Integer)


class MidTermOutlook(Base):
    __tablename__ = "mid_term_outlook"

    id = Column(Integer, primary_key=True)
    base_datetime = Column(DateTime)
    stn_id = Column(Integer)
    wf_sv = Column(String)
