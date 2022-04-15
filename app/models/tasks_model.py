from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey, TEXT
from sqlalchemy.orm import relationship

@dataclass
class Tasks(db.Model):
    
    id: int
    name: str
    descripiton: str
    duration: int
    importance: int
    urgency: int
    
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    descripiton = Column(TEXT, nullable=False)
    duration = Column(Integer, nullable=False)
    importance = Column(Integer, nullable=False)
    urgency = Column(Integer, nullable=False)
    eisenhower_id = Column(Integer, ForeignKey('eisenhower.id'))
    
    eisenhower = relationship("Eisenhower", backref="tasks")
