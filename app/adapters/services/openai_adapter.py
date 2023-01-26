import openai
from typing import Optional

from .base_service_adapter import BaseServiceAdapter

from app.domain.models import NoteProgression, Key, Note, Scale


class OpenAIAdapter(BaseServiceAdapter):
  
  def __init__(cls, token: str, model: str, temperature: int = 1, request_tokens: int = 10) -> None:
    cls._model = model
    cls._temperature = temperature
    cls._request_tokens = request_tokens
    openai.api_key = token
    super().__init__()


  def get_note_progression(cls, key: Key, scale: Scale, base_key: Optional[Key] = Key.E) -> NoteProgression:
    try:
      prompt = cls.generate_ai_prompt(
        progression_type='notes',
        key=key, 
        scale=scale, 
        base_key=base_key
      )

      response = openai.Completion.create(
        model = cls._model,
        max_tokens = cls._request_tokens,
        temperature = cls._temperature,
        prompt=prompt,
        stop='\n',
      )
      raw_progression = response['choices'][0]['text'].replace('\n', '').replace('#', '').split(',')
      progression = [Note.parse_str(note) for note in raw_progression]

      return NoteProgression(
        scale=scale,
        key=key,
        progression=progression
      )
    except Exception as e:
      raise e


  def get_chord_progression(cls, key: Key, scale: Scale, base_key: Key = Key.E):
    pass


  def generate_ai_prompt(cls, progression_type: str, key: Key, scale: Scale, base_key: Optional[Key] = Key.E):
    return 'Create a progression of 4 {0}, comma separated, with scientific pitch notation using the {1} scale of {2} with {3} as the base note'.format(progression_type, str(scale), str(key), str(base_key))
