from pydub import AudioSegment # type: ignore
from typing import List

from app.domain.models import Note
from .base_audio_processor_adapter import BaseAudioProcessorAdapter

class PydubAdapter(BaseAudioProcessorAdapter):

  def __init__(cls, input_url : str, output_url : str) -> None:
    cls.input_url = input_url
    cls.output_url = output_url
    super().__init__()


  def merge_note_audio_files(cls, progression: List[Note]) -> str:
    filename = ''
    note_progression_audio = AudioSegment.empty()
    for note in progression:
      note_progression_audio += AudioSegment.from_wav(cls.input_url + str(note) + '.wav')
      filename += str(note) + '_' if progression[:1] != note else str(note)
    filename += 'progression.wav'

    note_progression_audio.export(cls.output_url + filename, format='wav')
    return cls.output_url + filename
