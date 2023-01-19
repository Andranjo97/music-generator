from unittest.mock import create_autospec

from app.adapters import BaseAdapter
from app.domain.models import NoteProgression, Key, Note, Scale
from app.domain.use_cases.generate_note_progression import generate_note_progression

def test__should_generate_note_progression():
  base_key = Key.E
  scale = Scale.major
  expected_response = NoteProgression(
    scale=scale,
    key=base_key,
    progression=[Note(key=Key.E), Note(key=Key.F_sharp)]
  )
  mock_adapter = create_autospec(BaseAdapter)
  mock_adapter.get_note_progression.return_value = expected_response

  result = generate_note_progression(adapter=mock_adapter, key=base_key, scale=scale)

  assert expected_response == result
  mock_adapter.get_note_progression.assert_called_once_with(key=base_key, scale=scale)

