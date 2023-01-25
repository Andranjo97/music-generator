from app.domain.models import Key

def test_should_return_string_key():
  assert str(Key.E) == 'E'
