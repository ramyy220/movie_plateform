import os
from dotenv import load_dotenv  # type: ignore

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "autre-cle-secrete-pour-jwt")
    JWT_ACCESS_TOKEN_EXPIRES = 3600
