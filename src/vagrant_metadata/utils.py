import requests
import json

from packaging import version as packagingVersion
from . import Metadata


def fetch(url: str) -> Metadata:
  r = requests.session().get(url)
  return Metadata.from_json(r.content)


def fetch_version(versions: dict, version: str) -> packagingVersion.Version:
  if version is not None:
    return packagingVersion.Version(version)
  return sorted(
      versions.keys(),
      reverse=True)[0]

def forge_metadata_url(box_name: str) -> str:
  if not '/' in box_name:
    raise Exception(f'box_name must contains "/" : {box_name}')
  return 'https://app.vagrantup.com/{}/boxes/{}'.format(*box_name.split('/'))
