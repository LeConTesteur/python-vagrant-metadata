
import os
import importlib
import requests_mock
import packaging


from unittest import TestCase, mock, main as unittest_main
from packaging import version as packagingVersion

from vagrant_metadata import VersionBox, Provider, Metadata
from vagrant_metadata.provider import ProviderList
from vagrant_metadata.versionBox import VersionBoxList

class TestVagrantMetadataClass(TestCase):
    def test_metadata_versions_with_provider(self):
        meta = Metadata('test', versions=VersionBoxList([
            VersionBox('1.1.0', providers=ProviderList([
                Provider("libvirt", "url1", "", ""), 
                Provider("virtualbox", "", "", "")
            ])),
            VersionBox('1.0.0', providers=ProviderList([
                Provider("libvirt", "", "", ""), 
                Provider("virtualbox", "url2", "", "")
            ])),
            VersionBox('1.2.0', providers=ProviderList([
                Provider("virtualbox", "url3", "", "")
            ]))
        ]))
        url1 = meta.url_for('1.1.0', 'libvirt')
        self.assertEqual(url1, 'url1')
        url2 = meta.url_for('1.0.0', 'virtualbox')
        self.assertEqual(url2, 'url2')
        url3 = meta.url_for_youngest_version('virtualbox')
        self.assertEqual(url3, 'url3')





if __name__ == '__main__':
    unittest_main()