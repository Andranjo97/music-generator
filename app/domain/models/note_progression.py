from typing import List
from pydantic import BaseModel

from .scales import Scale
from .key import Key
from .note import Note


class NoteProgression(BaseModel):
  scale: Scale
  key: Key
  progression: List[Note]
