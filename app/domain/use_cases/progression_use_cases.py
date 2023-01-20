from app.adapters import BaseServiceAdapter, BaseAudioProcessorAdapter
from app.domain.models import Scale, Key, NoteProgression


class ProgressionUseCases:
  def __init__(cls, service: BaseServiceAdapter, audio_processor: BaseAudioProcessorAdapter) -> None:
    cls.service = service
    cls.audio_processor = audio_processor

  def generate_note_progression(cls, key: Key, scale: Scale) -> NoteProgression:
    note_progression = cls.service.get_note_progression(key=key, scale=scale)

    return note_progression

