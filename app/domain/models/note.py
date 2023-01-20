from pydantic import Field, BaseModel, validator
from typing import Optional

from .key import Key

class Note(BaseModel):
  key: Key
  pitch: Optional[int] = Field(None, ge=-1, le=10)

  @validator('pitch')
  def set_pitch(cls, pitch):
    return pitch if pitch != None else 3

  def __str__(cls) -> str:
    return '{0}{1}'.format(cls.key.value, cls.pitch)
