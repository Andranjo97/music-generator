from unittest.mock import create_autospec

from app.adapters import BaseServiceAdapter, BaseAudioProcessorAdapter
from app.domain.models import NoteProgression, NoteProgressionResponse, Key, Note, Scale
from app.domain.use_cases.progression_use_cases import ProgressionUseCases

mock_service_adapter = create_autospec(BaseServiceAdapter)
mock_audio_adapter = create_autospec(BaseAudioProcessorAdapter)
use_cases = ProgressionUseCases(
  service=mock_service_adapter, 
  audio_processor=mock_audio_adapter,
)


def test__should_generate_note_progression():
  key = Key.E
  base_key = Key.E
  scale = Scale.major
  progression = [Note(key=Key.E), Note(key=Key.F_sharp)]
  url = '/test/url'
  expected_response = NoteProgressionResponse(
    scale=scale,
    key=key,
    progression=progression,
    url=url,
  )

  mock_service_adapter.get_note_progression.return_value = NoteProgression(
    scale=scale,
    key=key,
    progression=progression
  )
  mock_audio_adapter.merge_note_audio_files.return_value = '/test/url'

  result = use_cases.generate_note_progression(key=key, scale=scale, base_key=base_key)

  assert expected_response == result
  mock_service_adapter.get_note_progression.assert_called_once_with(key=key, scale=scale, base_key=base_key)
  mock_audio_adapter.merge_note_audio_files.assert_called_once_with(progression=progression)

