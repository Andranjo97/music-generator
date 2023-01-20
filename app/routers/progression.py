from fastapi import APIRouter

from app.adapters import OpenAIAdapter
from app.domain.models import NoteProgression, NotesProgressionRequest
from app.domain.use_cases import ProgressionUseCases

adapter = OpenAIAdapter()

progressions = APIRouter()
use_cases = ProgressionUseCases(adapter)


@progressions.post('/notes', name='generate_notes_progression', response_model=NoteProgression)
async def generate_notes_progression(request: NotesProgressionRequest):
  return use_cases.generate_note_progression(key=request.key, scale=request.scale)
