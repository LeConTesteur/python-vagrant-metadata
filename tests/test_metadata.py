"""
Test Metadata class
"""
from unittest import TestCase, main as unittest_main

from vagrant_metadata.metadata import Metadata
from vagrant_metadata.provider import Provider, ProviderList
from vagrant_metadata.version_box import VersionBox, VersionBoxList


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
