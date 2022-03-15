"""
Test utils functions
"""
from unittest import TestCase, main as unittest_main
from vagrant_metadata import forge_metadata_url


class TestVagrantMetadataUtils(TestCase):

    def test_forge_metadata_url_error(self):
        with self.assertRaises(Exception):
            forge_metadata_url('toto')
        with self.assertRaises(Exception):
            forge_metadata_url(None)

    def test_forge_metadata_url_work(self):
        self.assertEqual(forge_metadata_url('name/box'),
                         'https://app.vagrantup.com/name/boxes/box')
        self.assertEqual(forge_metadata_url('name/box/toto'),
                         'https://app.vagrantup.com/name/boxes/box')


if __name__ == '__main__':
    unittest_main()
