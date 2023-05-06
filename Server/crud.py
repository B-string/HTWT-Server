from sqlalchemy.orm import Session

import models


def get_short(db: Session, nx: int, ny: int):
    return db.query(models.ShortTermForecast).filter(models.ShortTermForecast.nx == nx, models.ShortTermForecast.ny == ny).first()
