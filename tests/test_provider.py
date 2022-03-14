import os
import importlib
import requests_mock
import packaging


from unittest import TestCase, mock, main as unittest_main
from packaging import version as packagingVersion

from vagrant_metadata import VersionBox, Provider, Metadata
from vagrant_metadata.provider import ProviderList

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