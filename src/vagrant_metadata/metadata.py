"""
Class model of metadata in metadata json file
"""
from typing import Union
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from packaging import version as packagingVersion

from .version_box import VersionBox, VersionBoxList


@dataclass_json
@dataclass
class Metadata:
    """
    Class model of metadata in metadata json file
    """
    name: str
    description: str = field(compare=False, default="")
    short_description: str = field(compare=False, default="")
    versions: VersionBoxList = field(default_factory=VersionBoxList)

    def url_for(self, version: Union[str, packagingVersion.Version], provider: str) -> str:
        """
        Get the download url of box for the specific version and provider
        """
        return self.versions[version].providers[provider].url

    def url_for_youngest_version(self, provider: str) -> str:
        """
        Get the download url of box for the youngest version and the specific provider
        """
        return self.versions.youngest().providers[provider].url

    def __getitem__(self, version: Union[str, packagingVersion.Version]) -> VersionBox:
        return self.versions[version]
