import ServerConstant as Constant

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = f"mysql+pymysql://{Constant.user}:{Constant.passwd}@{Constant.host}:3306/htwt"
SQLALCHEMY_DATABASE_URL = url

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
