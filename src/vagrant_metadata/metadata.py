from collections import OrderedDict
from typing import Union
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from packaging import version as packagingVersion
from collections import OrderedDict

from .versionBox import VersionBox, VersionBoxList

@dataclass_json
@dataclass
class Metadata:
  name: str
  description: str = field(compare=False, default="")
  short_description: str = field(compare=False, default="")
  versions: VersionBoxList = field(default_factory=VersionBoxList)

  def url_for(self, version: Union[str, packagingVersion.Version], provider: str) -> str:
    return self.versions[version].providers[provider].url

  def url_for_youngest_version(self, provider: str) -> str:
    return self.versions.youngest().providers[provider].url

  def __getitem__(self, v: Union[str, packagingVersion.Version]) -> VersionBox:
    return self.versions[v]
