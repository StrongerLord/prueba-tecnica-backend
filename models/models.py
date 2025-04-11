from datetime import datetime
from utils.db import db

class Priority(db.Model):
    __tablename__ = 'Priority'
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20), nullable=False, unique=True)
    tasks = db.relationship('Task', backref='priority_ref', lazy=True)
    
    def __repr__(self):
        return f'<Priority {self.description}>'

class State(db.Model):
    __tablename__ = 'States'
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(15), nullable=False, unique=True)
    tasks = db.relationship('Task', backref='state_ref', lazy=True)
    
    def __repr__(self):
        return f'<State {self.description}>'

class Task(db.Model):
    __tablename__ = 'Tasks'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    priority = db.Column(db.Integer, db.ForeignKey('Priority.id'), nullable=False)
    status = db.Column(db.Integer, db.ForeignKey('States.id'), nullable=False)
    creation_time = db.Column(db.DateTime, nullable=False)
    expiration_time = db.Column(db.DateTime, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority_ref.description if self.priority_ref else None,
            'status': self.state_ref.description if self.state_ref else None,
            'creation_time': self.creation_time.isoformat(),
            'expiration_time': self.expiration_time.isoformat()
        }
    
    def __init__(self, title, description, priority, status, expiration_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.expiration_time = expiration_date