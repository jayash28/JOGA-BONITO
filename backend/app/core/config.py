from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    database_url: str

    gemini_api_key: str = ""

    reddit_client_id: str = ""

    reddit_client_secret: str = ""

    kafka_bootstrap_servers: str = "localhost:9092"

    environment: str = "development"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()