from typing import Union
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
# from . import crud, models, schemas
from database import SessionLocal, engine
import crud
import schemas
import models
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/getShortTermForecast/", response_model=schemas.ShortTermForecastList)
def transport_short_term_forecast(nx: int, ny: int, db: Session = Depends(get_db)):
    data = crud.get_short(db, nx, ny)

    return data


@app.get("/getMidTermTemperature/", response_model=schemas.MidTermTemperature)
def transport_mid_term_temperature(reg_id: str, db: Session = Depends(get_db)):
    data = crud.get_mid_temperature(db, reg_id)

    return data


@app.get("/getMidTermOutlook/", response_model=schemas.MidTermOutlook)
def transport_mid_term_outlook(stn_id: int, db: Session = Depends(get_db)):
    data = crud.get_mid_outlook(db, stn_id)

    return data
