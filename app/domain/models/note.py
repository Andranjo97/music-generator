import re
from pydantic import Field, BaseModel, validator
from typing import Optional

from .key import Key


class Note(BaseModel):
  key: Key
  pitch: Optional[int] = Field(3, ge=-1, le=10)


  @validator('key')
  def set_key(cls, key):
    return Key[key.replace('#', '_sharp')] if isinstance(key, str) and Key.is_sharp(key) else key


  @validator('pitch')
  def set_pitch(cls, pitch):
    return pitch if pitch != None else 3


  @classmethod
  def parse_str(cls, string_note: str) -> 'Note':
    raw_str = string_note.strip()
    pitch = int(re.sub('\D', '', raw_str) or '3')
    key = re.sub('\d', '', raw_str)

    return Note(
      key=key,
      pitch=pitch
    )


  def __str__(cls) -> str:
    return '{0}{1}'.format(cls.key.value, cls.pitch)

