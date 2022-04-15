

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Tasks_categories():
    
    __tablename__ = 'tasks_categories'
    
    id = Column(Integer, primary_key=True)
    
    task_id = Column(Integer, ForeignKey('tasks.id'))
    
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    
    task = relationship("Tasks", backref="tasks_categories")
    
    category = relationship("Categories", backref="tasks_categories")
