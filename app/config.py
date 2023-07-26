from fastapi import FastAPI
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str ='localhost'
    database_port: str = '5432'
    database_password: str = 'root'
    database_username: str ='postgres'
    database_name: str   ='fastapi'
    secret_key: str = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
    algoritham: str ='HS256'
    access_token_expire_minutes: int = 30
    class Config:
        env_file= ".env"


settings = Settings()
   