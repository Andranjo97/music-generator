from app.adapters import BaseAdapter
from app.domain.models import Scale, Key, NoteProgression


class ProgressionUseCases:
  def __init__(cls, adapter: BaseAdapter) -> None:
    cls.adapter = adapter

  def generate_note_progression(cls, key: Key, scale: Scale) -> NoteProgression:
    note_progression = cls.adapter.get_note_progression(key=key, scale=scale)

    return note_progression

