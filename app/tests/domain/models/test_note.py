import pytest
from pydantic import ValidationError

from app.domain.models.note import Note, Key
from app.tests.fixtures.note_fixture import valid_note, valid_sharp_note, note_key_no_pitch, invalid_note_key


def test__should_return_music_note(valid_note):
  expected_note = Note(key='E', pitch=0)
  assert expected_note == Note(key=valid_note.get('key'), pitch=valid_note.get('pitch'))
  assert expected_note.key == Key.E
  assert expected_note.pitch == 0


def test__should_return_music_note_sharp(valid_sharp_note):
  expected_note = Note(key='C#', pitch=2)
  assert expected_note == Note(key=valid_sharp_note.get('key'), pitch=valid_sharp_note.get('pitch'))
  assert expected_note.key == Key.C_sharp
  assert expected_note.pitch == 2


def test__should_return_string_note():
  note = Note(key='E', pitch=0)
  assert str(note) == 'E0'


def test__should_return_music_note_with_default_pitch(note_key_no_pitch):
  expected_note = Note(key='E', pitch=3)
  assert expected_note == Note(key=note_key_no_pitch.get('key'))


def test__should_raise_error_music_note_invalid(invalid_note_key):
  with pytest.raises(ValidationError):
    Note(key=invalid_note_key.get('key'), pitch=invalid_note_key.get('pitch'))


def test__should_return_parsed_note_from_string():
  expected_note = Note(key='E', pitch=3)
  
  result = Note.parse_str('E3')

  assert result == expected_note


def test__should_return_parsed_note_from_string_sharp():
  expected_note = Note(key='A#', pitch=5)
  
  result = Note.parse_str('A#5')

  assert result == expected_note


def test__should_return_parsed_note_from_string_with_space():
  expected_note = Note(key='A#', pitch=5)
  
  result = Note.parse_str(' A#5')

  assert result == expected_note
