from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey, TEXT
from app.configs.database import db


@dataclass
class Categories(db.Model):
    __tablename__ = 'categories'
    
    id: int
    name: str
    description: str
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(TEXT, nullable=False)
    