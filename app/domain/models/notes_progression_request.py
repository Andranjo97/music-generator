from pydantic import BaseModel
from typing import Optional

from app.domain.models import Key, Scale

class NotesProgressionRequest(BaseModel):
  key: Key
  scale: Scale
  base_key: Optional[Key]
