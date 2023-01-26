import pytest

@pytest.fixture
def valid_note():
  return {
    'key': 'E',
    'pitch': 0,
  }

@pytest.fixture
def valid_sharp_note():
  return {
    'key': 'C#',
    'pitch': 2,
  }

@pytest.fixture
def note_key_no_pitch():
  return {
    'key': 'E',
  }

@pytest.fixture
def invalid_note_key():
  return {
    'key': 1,
    'pitch': 0,
  }
