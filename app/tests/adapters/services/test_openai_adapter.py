import pytest

from app.adapters import BaseServiceAdapter, OpenAIAdapter
from app.domain.models import NoteProgression, Key, Note, Scale


def test_should_be_instance_of_base_adapter():
  openai_adapter = OpenAIAdapter(model='test-ai-model', token='some-token')
  assert isinstance(openai_adapter, BaseServiceAdapter)


def test_should_generate_valid_prompt_if_strings():
  openai_adapter = OpenAIAdapter(model='test-ai-model', token='some-token')
  expected_prompt = 'Create a progression of 4 notes, comma separated, with scientific pitch notation using the chromatic scale of G with E as the base note'

  result = openai_adapter.generate_ai_prompt('notes', 'G', 'chromatic')

  assert result == expected_prompt


def test_should_generate_valid_prompt_if_enums():
  openai_adapter = OpenAIAdapter(model='test-ai-model', token='some-token')
  expected_prompt = 'Create a progression of 4 notes, comma separated, with scientific pitch notation using the chromatic scale of G with E as the base note'

  result = openai_adapter.generate_ai_prompt('notes', Key.G, Scale.chromatic)

  assert result == expected_prompt


def test_should_return_note_progression():
  openai_adapter = OpenAIAdapter(model='test-ai-model', token='some-token')
  expected_note_progression = NoteProgression(
    scale='major',
    key='E',
    progression=[Note(key=Key.E), Note(key=Key.F_sharp)]
  )

  result = openai_adapter.get_note_progression(key='E', scale='major')

  assert expected_note_progression == result
