from enum import Enum

class Key(Enum):
  C = 'C'
  C_sharp = 'C#'
  D = 'D'
  D_sharp = 'D#'
  E = 'E'
  F = 'F'
  F_sharp = 'F#'
  G = 'G'
  G_sharp = 'G#'
  A = 'A'
  A_sharp = 'A#'
  B = 'B'

  def __str__(self) -> str:
    return self.value
