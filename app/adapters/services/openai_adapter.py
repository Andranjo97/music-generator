import openai

from .base_service_adapter import BaseServiceAdapter

from app.domain.models import NoteProgression, Key, Note, Scale


class OpenAIAdapter(BaseServiceAdapter):
  
  def __init__(cls, token: str, model: str, temperature: int = 2, request_tokens: int = 10) -> None:
    cls._model = model
    cls._temperature = temperature
    cls._request_tokens = request_tokens
    openai.api_key = token
    super().__init__()


  def get_note_progression(cls, key: Key, scale: Scale) -> NoteProgression:
    try:
      prompt = cls.generate_ai_prompt('notes', key, scale)
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


  def get_chord_progression(cls, key: Key, scale: Scale):
    pass


  def generate_ai_prompt(cls, progression_type: str, key: Key, scale: Scale):
    return 'Create a progression of 4 {0}, comma separated, with scientific pitch notation using the {1} scale of {2} with E as the base note'.format(progression_type, str(scale), str(key))
