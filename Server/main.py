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


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/getShortTermForecast/", response_model=schemas.ShortTermForecast)
def transport_short_term_forecast(nx: int, ny: int, db: Session = Depends(get_db)):
    data = crud.get_short(db, nx, ny)
    return data
