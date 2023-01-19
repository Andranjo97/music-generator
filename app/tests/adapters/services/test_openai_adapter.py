import pytest

from app.adapters import BaseAdapter, OpenAIAdapter

def test_should_be_instance_of_base_adapter():
  openai_adapter = OpenAIAdapter()
  assert isinstance(openai_adapter, BaseAdapter)
