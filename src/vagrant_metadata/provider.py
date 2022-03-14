from ast import Slice
from collections import UserList
from dataclasses import dataclass, field
from typing import Iterable, Union
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Provider:
  name: str
  url: str
  checksum_type: str = field(default="")
  checksum: str = field(default="")

class ProviderList(UserList):
  def __getattr__(self, name: str) -> Provider:
    try:
      return next(self._filter_provider(name))
    except StopIteration:
      raise AttributeError(f'No Provider with name: "{name}"')
  
  def __getitem__(self, p: str) -> Provider:
    try:
      return next(self._filter_provider(p))
    except StopIteration:
      raise IndexError(f'No ProviderList with name: "{p}"')

  def _filter_provider(self, provider: str) -> Iterable:
    return filter(lambda p: p.name == provider, self.data)