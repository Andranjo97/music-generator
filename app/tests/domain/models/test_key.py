import pytest

from app.domain.models import Key, NotFlatKeyException


def test__should_get_correct_key():
  assert Key['E'] == Key.E


def test__should_get_correct_key_sharp():
  assert Key['C#'] == Key.C_sharp


def test__should_get_correct_key_equivalent_if_flat():
  assert Key['Db'] == Key.C_sharp


def test__should_return_string_key():
  assert str(Key.E) == 'E'


def test__should_return_sharp_from_flat_key():
  assert Key.turn_flat_to_sharp('Eb') == Key.D_sharp


def test__should_raise_not_flat_key_exception():
  with pytest.raises(NotFlatKeyException) as e_info:
    Key.turn_flat_to_sharp('C')
    
    assert str(e_info) == 'Key cannot be converted to sharp'


def test__should_return_true_if_is_key():
  assert Key.is_key('E7#')
  assert Key.is_key('Gb')
  assert Key.is_key('A')


def test__should_return_false_if_is_not_key():
  assert not Key.is_key('K')
  assert not Key.is_key('Pb')
  assert not Key.is_key('L#')


def test__should_return_true_if_is_flat():
  assert Key.is_flat('B flat')
  assert Key.is_flat('Bb')
  assert Key.is_flat('B♭')


def test__should_return_false_if_is_not_flat():
  assert not Key.is_flat('B#')
  assert not Key.is_flat('B')
  assert not Key.is_flat('K')


def test__should_return_true_if_is_sharp():
  assert Key.is_sharp('B #')
  assert Key.is_sharp('B sharp')
  assert Key.is_sharp('B♯')


def test__should_return_false_if_is_not_sharp():
  assert not Key.is_sharp('Bb')
  assert not Key.is_sharp('B')
  assert not Key.is_sharp('K')
