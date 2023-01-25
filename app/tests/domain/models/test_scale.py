from app.domain.models import Scale

def test_should_return_string_scale():
  assert str(Scale.chromatic) == 'chromatic'
