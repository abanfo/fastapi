
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi',user = 'postgres',password='root', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Database connection was succesful!!!!')
#         break
#     except Exception as error:
#         print('connection failed')
#         print(f'The error was {error}')
#         time.sleep(2)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost/fastapi"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
