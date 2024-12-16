""" In the dependencies section we add the database session managment and other related to the API"""
import os
from sqlmodel import Session, create_engine, SQLModel, select
from dotenv import load_dotenv

# Database setup
load_dotenv('.env')
DATABASE_URL = os.getenv('DATABASE_URL', None)
engine = create_engine(
    DATABASE_URL,
    connect_args={
        'check_same_thread': False
    }
)

# Dependency
def get_session():
    with Session(engine) as session:
        yield session