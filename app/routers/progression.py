from fastapi import APIRouter

from app.adapters import OpenAIAdapter, PydubAdapter
from app.config.env_manager import get_settings
from app.domain.models import NoteProgressionResponse, NotesProgressionRequest
from app.domain.use_cases import ProgressionUseCases

EnvManager = get_settings()

service = OpenAIAdapter(
  token=EnvManager.OPENAI_API_KEY,
  model=EnvManager.OPENAI_MODEL,
)
audio_processor = PydubAdapter(
  input_url=EnvManager.AUDIO_FILES_URL,
  output_url=EnvManager.PROGRESSIONS_URL,
)

progressions = APIRouter()
use_cases = ProgressionUseCases(service, audio_processor)


@progressions.post('/notes', name='generate_notes_progression', response_model=NoteProgressionResponse)
async def generate_notes_progression(request: NotesProgressionRequest):
  return use_cases.generate_note_progression(key=request.key, scale=request.scale, base_key=request.base_key)
