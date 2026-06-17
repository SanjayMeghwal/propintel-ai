from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    
    # Add these three lines to handle the security variables:
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int  # Notice this is an int, not a str!

    class Config:
        env_file = ".env"
        extra = "ignore"  # This tells Pydantic not to crash if extra variables exist

settings = Settings()