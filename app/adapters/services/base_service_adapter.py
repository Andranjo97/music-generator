from abc import abstractmethod

from app.domain.models import NoteProgression, Key, Scale

class BaseServiceAdapter:
  
  @abstractmethod
  def get_note_progression(cls, key: Key, scale: Scale, base_key: Key = Key.E) -> NoteProgression:
    raise NotImplementedError()


  @abstractmethod
  def get_chord_progression(cls, key: Key, scale: Scale, base_key: Key = Key.E):
    raise NotImplementedError()

