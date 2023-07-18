from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for the models
Base = declarative_base()

# Create class Strava actities record database
class StravaActivities(Base):  
    # Setting the table name 
    __tablename__ = 'strava_activities'

    # The autoincremented primaty key 
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Row update datetime
    updated_at = Column(DateTime, default=func.now())

    # Row creation datetime
    created_at = Column(DateTime, default=func.now())


    def __repr__(self):
        return f"""
            id: {self.id}
        """