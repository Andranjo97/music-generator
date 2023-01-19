from abc import ABC, abstractmethod

from app.domain.models import NoteProgression, Key, Scale

class BaseAdapter(ABC):
  
  @abstractmethod
  def get_note_progression(cls, key: Key, scale: Scale) -> NoteProgression:
    raise NotImplementedError()


  @abstractmethod
  def get_chord_progression(cls, key: Key, scale: Scale):
    raise NotImplementedError()

