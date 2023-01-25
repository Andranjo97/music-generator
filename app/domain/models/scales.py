from enum import Enum

class Scale(Enum):
  major = 'major'
  minor = 'minor'
  chromatic = 'chromatic'

  def __str__(self) -> str:
    return self.value
