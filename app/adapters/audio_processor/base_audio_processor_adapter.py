from abc import abstractmethod
from typing import List

from app.domain.models import Note

class BaseAudioProcessorAdapter:
  @abstractmethod
  def merge_note_audio_files(cls, progression: List[Note]) -> str:
    raise NotImplementedError()
