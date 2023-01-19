from app.adapters import BaseAdapter
from app.domain.models import Scale, Key

def generate_note_progression(adapter: BaseAdapter, key: Key, scale: Scale):
  return adapter.get_note_progression(key=key, scale=scale)
