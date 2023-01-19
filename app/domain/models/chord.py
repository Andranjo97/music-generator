from enum import Enum
from pydantic import BaseModel
from typing import Optional

from .note import Note


class ChordType(Enum):
  minor = 'minor'
  major = 'major'
  diminished = 'diminished'
  augmented = 'augmented'


class Chord(BaseModel):
  note: Note
  type: ChordType
