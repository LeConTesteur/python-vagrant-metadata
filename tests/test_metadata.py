"""
Test Metadata class
"""
from unittest import TestCase, main as unittest_main

from vagrant_metadata.metadata import Metadata
from vagrant_metadata.provider import Provider
from vagrant_metadata.version_box import VersionBox


class TestVagrantMetadataClass(TestCase):
    def test_metadata_versions_with_provider(self):
        v120 = VersionBox('1.2.0', providers=[
            Provider("virtualbox", "url3", "", "")
        ])
        meta = Metadata('test', versions=[
            VersionBox('1.1.0', providers=[
                Provider("libvirt", "url1", "", ""),
                Provider("virtualbox", "", "", "")
            ]),
            VersionBox('1.0.0', providers=[
                Provider("libvirt", "", "", ""),
                Provider("virtualbox", "url2", "", "")
            ]),
            v120
        ])
        url1 = meta.url_for('1.1.0', 'libvirt')
        self.assertEqual(url1, 'url1')
        url2 = meta.url_for('1.0.0', 'virtualbox')
        self.assertEqual(url2, 'url2')
        url3 = meta.url_for_youngest_version('virtualbox')
        self.assertEqual(url3, 'url3')
        self.assertEqual(meta["1.2.0"], v120)


if __name__ == '__main__':
    unittest_main()
