from unittest.mock import create_autospec

from app.adapters import BaseServiceAdapter
from app.domain.models import NoteProgression, Key, Note, Scale
from app.domain.use_cases.progression_use_cases import ProgressionUseCases

mock_adapter = create_autospec(BaseServiceAdapter)
use_cases = ProgressionUseCases(mock_adapter)

def test__should_generate_note_progression():
  base_key = Key.E
  scale = Scale.major
  expected_response = NoteProgression(
    scale=scale,
    key=base_key,
    progression=[Note(key=Key.E), Note(key=Key.F_sharp)]
  )

  mock_adapter.get_note_progression.return_value = expected_response

  result = use_cases.generate_note_progression(key=base_key, scale=scale)

  assert expected_response == result
  mock_adapter.get_note_progression.assert_called_once_with(key=base_key, scale=scale)

