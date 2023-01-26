import pytest
import unittest.mock

from app.adapters import BaseServiceAdapter, OpenAIAdapter
from app.domain.models import NoteProgression, Key, Note, Scale


def test__should_be_instance_of_base_adapter():
  openai_adapter = OpenAIAdapter(model='test-ai-model', token='some-token')
  assert isinstance(openai_adapter, BaseServiceAdapter)


def test__should_generate_valid_prompt_if_strings():
  openai_adapter = OpenAIAdapter(model='test-ai-model', token='some-token')
  expected_prompt = 'Create a progression of 4 notes, comma separated, with scientific pitch notation using the chromatic scale of G with E as the base note'

  result = openai_adapter.generate_ai_prompt('notes', 'G', 'chromatic', 'E')

  assert result == expected_prompt


def test__should_generate_valid_prompt_if_enums():
  openai_adapter = OpenAIAdapter(model='test-ai-model', token='some-token')
  expected_prompt = 'Create a progression of 4 notes, comma separated, with scientific pitch notation using the chromatic scale of G with E as the base note'

  result = openai_adapter.generate_ai_prompt('notes', Key.G, Scale.chromatic, 'E')

  assert result == expected_prompt


def random_shuffle(list):
  list = [Note(key=Key.E), Note(key=Key.G), Note(key=Key.D)]

@unittest.mock.patch('openai.Completion')
@unittest.mock.patch('random.shuffle', random_shuffle)
def test__should_return_note_progression(mock_openai_completion):
  mock_openai_completion.create.return_value = {
    'choices': [
      {
        'text': '\nE, G, D'
      }
    ]
  }
  
  openai_adapter = OpenAIAdapter(model='test-ai-model', token='some-token')
  expected_note_progression = NoteProgression(
    scale='major',
    key='E',
    progression=[Note(key=Key.E), Note(key=Key.G), Note(key=Key.D)]
  )

  result = openai_adapter.get_note_progression(key='E', scale='major')

  assert expected_note_progression == result
  mock_openai_completion.create.assert_called_once_with(
    model='test-ai-model',
    max_tokens=10,
    temperature=1,
    prompt='Create a progression of 4 notes, comma separated, with scientific pitch notation using the major scale of E with E as the base note'
  )
