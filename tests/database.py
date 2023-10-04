from fastapi.testclient import TestClient
from app.main import app
from fastapi import status
import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from db.database import get_db
from db.database import Base
import pytest
# SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:root@localhost:5432/fastapi_test'
# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)





@pytest.fixture
def session():
    # clear all the tables at the beginning 
    Base.metadata.drop_all(bind=engine) 
    # creat all the tables
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)