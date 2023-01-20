from pydantic import Field, BaseModel, validator
from typing import Optional

from .key import Key

class Note(BaseModel):
  key: Key
  pitch: Optional[int] = Field(3, ge=-1, le=10)

  @validator('pitch')
  def set_pitch(cls, pitch):
    return pitch or 3
