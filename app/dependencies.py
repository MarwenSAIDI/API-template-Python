""" In the dependencies section we add the database session managment and other related to the API"""
from sqlmodel import Session, create_engine, SQLModel, select

# Database setup
DATABASE_URL = "sqlite:///./db/database.db"
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