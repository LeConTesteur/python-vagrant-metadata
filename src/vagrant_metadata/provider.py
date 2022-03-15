"""
Class model of proviser in metadata json file
We have two classes in this file:
- Provider
- ProviderList
"""
from collections import UserList
from dataclasses import dataclass, field
from typing import Iterable
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Provider:
    """
    Class model of proviser in metadata json file
    """
    name: str
    url: str
    checksum_type: str = field(default="")
    checksum: str = field(default="")


class ProviderList(UserList):
    """
    List of Provider with utils methods
    """
    def __getattr__(self, name: str) -> Provider:
        try:
            return next(self._filter_provider(name))
        except StopIteration as exception:
            raise AttributeError(f'No Provider with name: "{name}"')  from exception

    def __getitem__(self, p: str) -> Provider:
        try:
            return next(self._filter_provider(p))
        except StopIteration as exception:
            raise IndexError(f'No ProviderList with name: "{p}"') from exception

    def _filter_provider(self, provider: str) -> Iterable:
        return filter(lambda p: p.name == provider, self.data)
