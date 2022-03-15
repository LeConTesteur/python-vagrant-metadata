"""
Acceptance test
"""
import requests_mock


from unittest import TestCase, main as unittest_main

from vagrant_metadata import fetch


class TestVagrantMetadata(TestCase):
    @requests_mock.Mocker()
    def test_fetch(self, mock):
        mock.get('http://test.com', text='''
{
  "description":"Test",
  "short_description":"description",
  "name":"test",
  "versions":[
     {
        "version":"1.0.1",
        "status":"active",
        "description_html":"<h1></h1>",
        "description_markdown":"",
        "providers":[
           {
              "name":"libvirt",
              "url":"https://test.com/test.box",
              "checksum":null,
              "checksum_type":null
           },
           {
              "name":"virtualbox",
              "url":"https://test.com/test.box",
              "checksum":null,
              "checksum_type":null
           }
        ]
     },
     {
        "version":"1.0.0",
        "status":"active",
        "description_html":"<h1></h1>",
        "description_markdown":"",
        "providers":[
           {
              "name":"libvirt",
              "url":"https://test.com/test.box",
              "checksum":null,
              "checksum_type":null
           },
           {
              "name":"virtualbox",
              "url":"https://test.com/test.box",
              "checksum":null,
              "checksum_type":null
           }
        ]
     }
  ]
}
        ''')
        meta = fetch('http://test.com')
        self.assertEqual(meta.name, 'test')
        self.assertEqual(meta.description, 'Test')
        #self.assertEqual(meta['1.0.0'].provider('libvirt').url, "https://test.com/test.box")


if __name__ == '__main__':
    unittest_main()
