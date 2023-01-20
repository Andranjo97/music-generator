from .base_adapter import BaseAdapter

from app.domain.models import NoteProgression, Key, Note, Scale

class OpenAIAdapter(BaseAdapter):
  
  def get_note_progression(cls, key: Key, scale: Scale) -> NoteProgression:
    # TODO remove hard-coded return model

    return NoteProgression(
      scale=scale,
      key=key,
      progression=[Note(key=Key.E), Note(key=Key.F_sharp)]
    )

  def get_chord_progression(cls, key: Key, scale: Scale):
    pass
