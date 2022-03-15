"""
Public function
"""
import requests

from .metadata import Metadata


def fetch(url: str) -> Metadata:
    """
    Download metadata json for url and create Metadata class
    """
    response = requests.session().get(url)
    return Metadata.from_json(response.content) # pylint: disable=E1101

def forge_metadata_url(box_name: str) -> str:
    """
    Forge the metadata url from name
    """
    if not '/' in box_name:
        raise Exception(f'box_name must contains "/" : {box_name}')
    user, name, *_ = box_name.split('/', maxsplit=2)
    return f'https://app.vagrantup.com/{user}/boxes/{name}'
