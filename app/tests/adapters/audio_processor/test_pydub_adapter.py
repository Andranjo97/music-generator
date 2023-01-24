# type: ignore
import pydub
import unittest.mock

from app.adapters import PydubAdapter, BaseAudioProcessorAdapter
from app.domain.models import Note


def test_should_be_instance_of_base_audio_processor_adapter():
  audio_adapter = PydubAdapter(input_url='test_input/', output_url='test_output/')
  assert isinstance(audio_adapter, BaseAudioProcessorAdapter)
  assert audio_adapter.input_url == 'test_input/'
  assert audio_adapter.output_url == 'test_output/'

@unittest.mock.patch('pydub.AudioSegment.empty')
@unittest.mock.patch('pydub.AudioSegment.from_wav')
def test_should_return_url_from_generated_progression(mock_segment_empty, mock_segment_from_wav):
  mock_segment_empty.export.return_value = ''
  mock_segment_from_wav.return_value = 'from_wav'
  audio_adapter = PydubAdapter(input_url='test_input/', output_url='test_output/')
  progression = [
    Note(
      key='A'
    ),
    Note(
      key='E'
    )
  ]
  expected_url = 'test_output/A3_E3_progression.wav'
  
  result = audio_adapter.merge_note_audio_files(progression)

  assert result == expected_url


