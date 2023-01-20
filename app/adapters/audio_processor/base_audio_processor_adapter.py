from abc import abstractmethod

class BaseAudioProcessorAdapter:

  @abstractmethod
  def merge_note_audio_files(cls, **kwargs):
    raise NotImplementedError()