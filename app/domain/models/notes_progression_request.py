from pydantic import BaseModel

from app.domain.models import Key, Scale

class NotesProgressionRequest(BaseModel):
  key: Key
  scale: Scale
