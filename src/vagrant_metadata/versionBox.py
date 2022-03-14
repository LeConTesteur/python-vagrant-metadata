from ast import Slice
from collections import UserList
from dataclasses import dataclass, field
from typing import Iterable, List, Union
from dataclasses_json import dataclass_json
from packaging import version as packagingVersion

from .provider import Provider, ProviderList

@dataclass_json
@dataclass(eq=True, order=True)
class VersionBox:
  version: str = field(compare=True)
  status: str = field(compare=False, default="active")
  description_html: str = field(compare=False, default="")
  description_markdown: str = field(compare=False, default="")
  providers: ProviderList = field(default_factory=ProviderList, compare=False)
  _version: str = field(init=False, default='', compare=False)

  def have_provider(self, provider: str) -> bool:
    return any(self._filter_provider(provider))

  def provider(self, provider: str) -> Provider:
    try:
      return self.providers[provider]
    except IndexError:
      return None

  def _filter_provider(self, provider: str) -> Iterable:
    return filter(lambda p:p.name == provider, self.providers)

  @property
  def version(self):
    return self._version

  @version.setter
  def version(self, v):
    self._version = packagingVersion.Version(v)

class VersionBoxList:
  def __init__(self, data) -> None:
      self.data = data

  def __getitem__(self, v: Union[ str, packagingVersion.Version]) -> VersionBox:
    if isinstance(v, str):
      v = packagingVersion.Version(v)
    try:
      return next(self._filter_version(v))
    except StopIteration:
      raise IndexError(f'No versionBox with version: "{v}"')
  
  def _filter_version(self, version: packagingVersion.Version) -> Iterable:
    return filter(lambda v:v.version == version, self.data)

  def youngest(self) -> VersionBox:
    return sorted(self.data, reverse=True)[0]