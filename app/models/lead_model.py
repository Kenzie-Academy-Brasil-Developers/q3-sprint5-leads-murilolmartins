from dataclasses import dataclass
from email.policy import default
from app.configs.database import db
from sqlalchemy import CheckConstraint, Column, Integer, String, DateTime
from datetime import datetime as dt

@dataclass
class LeadModel(db.Model):

    id: int 
    name: str
    email: str
    phone: str
    creation_date: str
    last_visit: str
    visits: str

    __tablename__ = "leads"
    __table_args__ = (CheckConstraint("phone ~ '^\([1-9]{2}\)[0-9]{5}\-[0-9]{4}$'"),)

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email= Column(String,nullable=False,unique=True)
    phone= Column(String,nullable=False,unique=True)
    creation_date= Column(String,default=str(dt.now()))
    last_visit= Column(String,default=str(dt.now()))
    visits=Column(Integer,default=1)

   
