"""
Class model of version box in metadata json file
We have two classes in this file:
- VersionBox
- VersionBoxList
"""
from dataclasses import dataclass, field
from typing import Iterable, Union
from dataclasses_json import dataclass_json
from packaging import version as packagingVersion

from .provider import Provider, ProviderList


@dataclass_json
@dataclass(eq=True, order=True)
class VersionBox:
    """
    Class model of version box in metadata json file
    """
    version: str = field(compare=True)
    status: str = field(compare=False, default="active")
    description_html: str = field(compare=False, default="")
    description_markdown: str = field(compare=False, default="")
    providers: ProviderList = field(
        default_factory=ProviderList, compare=False)
    _version: str = field(init=False, default='', compare=False)

    def have_provider(self, provider: str) -> bool:
        """
        Test if the provider is in provider list
        """
        return any(self._filter_provider(provider))

    def provider(self, provider: str) -> Provider:
        """
        Get the provider by this name
        """
        try:
            return self.providers[provider]
        except IndexError:
            return None

    def _filter_provider(self, provider: str) -> Iterable:
        return filter(lambda p: p.name == provider, self.providers)

    @property
    def version(self) -> packagingVersion.Version:
        """
        Get the version with type packaging.version.Version
        """
        return self._version

    @version.setter
    def version(self, version: str) -> None:
        """
        Set the version into type packaging.version.Version
        """
        self._version = packagingVersion.Version(version)


class VersionBoxList:
    """
    List of VersionBox with utils methods
    """
    def __init__(self, data) -> None:
        self.data = data

    def __getitem__(self, version: Union[str, packagingVersion.Version]) -> VersionBox:
        """
        Get the VersionBox by version
        """
        if isinstance(version, str):
            version = packagingVersion.Version(version)
        try:
            return next(self._filter_version(version))
        except StopIteration as exception:
            raise IndexError(f'No VersionBox with version: "{version}"') from exception

    def _filter_version(self, version: packagingVersion.Version) -> Iterable:
        return filter(lambda v: v.version == version, self.data)

    def youngest(self) -> VersionBox:
        """
        Get the youngest VersionBox
        """
        return sorted(self.data, reverse=True)[0]
