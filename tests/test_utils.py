import os
import importlib
import requests_mock
import packaging


from unittest import TestCase, mock, main as unittest_main
from packaging import version as packagingVersion

from vagrant_metadata import VersionBox, Provider, Metadata
from vagrant_metadata.utils import fetch_version, forge_metadata_url

class TestVagrantMetadataUtils(TestCase):

    def test_forge_metadata_url_error(self):
        with self.assertRaises(Exception):
            forge_metadata_url('toto')
        with self.assertRaises(Exception):
            forge_metadata_url()

    def test_forge_metadata_url_work(self):
        self.assertEqual(forge_metadata_url('name/box'), 'https://app.vagrantup.com/name/boxes/box')
        self.assertEqual(forge_metadata_url('name/box/toto'), 'https://app.vagrantup.com/name/boxes/box')

    def test_fetch_version_with_specify_version(self):
        self.assertEqual(
            fetch_version(None, '1.1.1'),
            packagingVersion.Version('1.1.1')
        )


    def test_fetch_version_with_last_version(self):
        versions = {
            packagingVersion.Version('1.1.1'): VersionBox('1.1.0', providers=[
                Provider("libvirt", "", "", ""), 
                Provider("virtualbox", "", "", "")
            ]),
            packagingVersion.Version('1.0.0'): VersionBox('1.0.0', providers=[
                Provider("libvirt", "", "", ""), 
                Provider("virtualbox", "", "", "")
            ]),
            packagingVersion.Version('1.2.0'): VersionBox('1.2.0', providers=[
                Provider("virtualbox", "", "", "")
            ])
        }
        self.assertEqual(
            fetch_version(versions, None),
            packagingVersion.Version('1.2.0')
        )

if __name__ == '__main__':
    unittest_main()