from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///C:\\dev\\strava_app_db\\strava.db', echo=True)

Base = declarative_base()

Base.metadata.create_all(engine)