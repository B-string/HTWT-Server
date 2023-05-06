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
