from typing import Optional

from app.adapters import BaseServiceAdapter, BaseAudioProcessorAdapter
from app.domain.models import Scale, Key, NoteProgressionResponse


class ProgressionUseCases:
  def __init__(cls, service: BaseServiceAdapter, audio_processor: BaseAudioProcessorAdapter) -> None:
    cls.service = service
    cls.audio_processor = audio_processor

  def generate_note_progression(cls, key: Key, scale: Scale, base_key: Optional[Key]) -> NoteProgressionResponse:
    note_progression = cls.service.get_note_progression(key=key, scale=scale, base_key=base_key)
    progression_url = cls.audio_processor.merge_note_audio_files(note_progression.progression)

    return NoteProgressionResponse(
      scale=note_progression.scale,
      key=note_progression.key,
      progression=note_progression.progression,
      url=progression_url
    )

