from sqlalchemy.orm import Session

import models
import schemas


def get_short(db: Session, nx: int, ny: int):
    # forecasts = db.query(models.ShortTermForecast).filter(
    #     models.ShortTermForecast.nx == nx, models.ShortTermForecast.ny == ny).all()

    forecasts = db.query(models.ShortTermForecast).all()
    print(forecasts[0].id)
    for row in forecasts:
        print(type(row.id))
    return schemas.ShortTermForecastList(forecasts=forecasts)


def get_mid_temperature(db: Session, reg_id: str):
    forecasts = db.query(models.MidTermTemperature).filter(
        models.MidTermTemperature.reg_id == reg_id).first()

    return forecasts


def get_mid_outlook(db: Session, stn_id: int):
    forecasts = db.query(models.MidTermOutlook).filter(
        models.MidTermOutlook.stn_id == stn_id).first()

    return forecasts
