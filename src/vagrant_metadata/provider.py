"""
Class model of proviser in metadata json file
We have two classes in this file:
- Provider
- ProviderList
"""
from dataclasses import dataclass, field
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
