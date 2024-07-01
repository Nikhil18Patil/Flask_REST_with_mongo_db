import os

class Config:
    MONGO_DB_NAME = 'person_db'
    MONGO_URI = 'mongodb://localhost:27017/person_db'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Nikhil_patil'
