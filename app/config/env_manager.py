from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
  ENV: str = 'DEV'
  OPENAI_API_KEY: str
  OPENAI_MODEL: str
  AUDIO_FILES_URL: str
  PROGRESSIONS_URL: str
  ALLOW_ORIGIN_REGEX: Optional[str]

  class Config:
    env_file = './.env'
    env_file_encoding = 'utf-8'

    @classmethod
    def customise_sources(cls, init_settings, env_settings, file_secret_settings):
      return (
        init_settings,
        env_settings,
        file_secret_settings,
      )

  def get(self, key, default=None):
    return self.dict().get(key, default)

  def is_dev(self):
    return self.ENV.upper() == 'DEV'

  def is_secure_deployment(self):
    return self.ENV.upper() in ('STAGE', 'PROD')


@lru_cache
def get_settings() -> Settings:
  return Settings()


@lru_cache
def get_env_name() -> str:
  return get_settings().ENV
