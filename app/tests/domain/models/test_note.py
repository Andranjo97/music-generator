import pytest
from pydantic import ValidationError

from app.domain.models.note import Note
from app.tests.fixtures.note_fixture import valid_note, note_key_no_pitch, invalid_note_key


def test__should_return_music_note(valid_note):
  expected_note = Note(key='E', pitch=0)
  assert expected_note == Note(key=valid_note.get('key'), pitch=valid_note.get('pitch'))


def test__should_return_music_note_with_default_pitch(note_key_no_pitch):
  expected_note = Note(key='E', pitch=1)
  assert expected_note == Note(key=note_key_no_pitch.get('key'), pitch=note_key_no_pitch.get('pitch'))


def test__should_raise_error_music_note_invalid(invalid_note_key):
  with pytest.raises(ValidationError):
    Note(key=invalid_note_key.get('key'), pitch=invalid_note_key.get('pitch'))
