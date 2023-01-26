from app.domain.models import Scale

def test__should_return_string_scale():
  assert str(Scale.chromatic) == 'chromatic'
