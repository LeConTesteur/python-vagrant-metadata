"""
Test Proviser and ProviderList Class
"""
from unittest import TestCase, main as unittest_main

from vagrant_metadata.provider import Provider, ProviderList


class TestVagrantProviderListClass(TestCase):

    def test_version_have_provider(self):
        list = ProviderList()
        libvirt = Provider("libvirt", "", "", "")
        virtualbox = Provider("virtualbox", "", "", "")
        list.append(libvirt)
        list.append(virtualbox)

        self.assertEqual(list.libvirt, libvirt)
        self.assertEqual(list['libvirt'], libvirt)
        self.assertEqual(list.virtualbox, virtualbox)
        with self.assertRaises(AttributeError):
            list.hyperv


if __name__ == '__main__':
    unittest_main()
