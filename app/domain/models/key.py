import re
from enum import Enum, EnumMeta

class NotFlatKeyException(Exception):
  pass


class KeyEnumMeta(EnumMeta):
  def __getitem__(self, name: str):
    symbol = '#' if '#' in name else '♯'

    if Key.is_flat(name):
      return Key.turn_flat_to_sharp(name)

    return super().__getitem__(name.replace(symbol, '_sharp'))


class Key(Enum, metaclass=KeyEnumMeta):
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


  @classmethod
  def is_key(cls, key_str: str):
    return bool(re.match(r'\b[CDEFGAB](?:[0-9])?(?:#{1,2}|b{1,2})?(?:maj7?|min7?|sus2?)?\b', key_str))


  @classmethod
  def is_flat(cls, key_str: str):
    return cls.is_key(key_str) and ('b' in key_str or 'flat' in key_str or '♭' in key_str)


  @classmethod
  def is_sharp(cls, key_str: str):
    return cls.is_key(key_str) and ('#' in key_str or 'sharp' in key_str or '♯' in key_str)


  @classmethod
  def turn_flat_to_sharp(cls, key_with_flat: str) -> 'Key':
    white_list = [Key.D, Key.E, Key.G, Key.A, Key.B]

    trimmed_key_str = key_with_flat[0]

    if Key[trimmed_key_str] not in white_list:
      raise NotFlatKeyException('Key cannot be converted to sharp')

    list_of_keys = [member.name for member in Key]
    found_key = list_of_keys[list_of_keys.index(trimmed_key_str) - 1]
    return Key[found_key]


  def __str__(self) -> str:
    return self.value
