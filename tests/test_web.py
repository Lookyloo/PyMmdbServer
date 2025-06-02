#!/usr/bin/env python3

import unittest

from pymmdbserver import PyMmdbServer


class TestBasic(unittest.TestCase):

    def setUp(self) -> None:
        self.client = PyMmdbServer(root_url="https://ip.circl.lu/")

    def test_up(self) -> None:
        self.assertTrue(self.client.is_up)

    def test_ipv4(self) -> None:
        geolookup_result = self.client.geolookup("188.65.220.25")
        self.assertEqual(geolookup_result[0]['country']['iso_code'], 'BE')

    def test_ipv6(self) -> None:
        geolookup_result = self.client.geolookup("2a02:21d0::68:69:25")
        self.assertEqual(geolookup_result[0]['country']['iso_code'], 'BE')

    def test_self(self) -> None:
        my_result = self.client.my_geolookup()
        my_ip = my_result[0]["ip"]
        geolookup_result = self.client.geolookup(my_ip)
        self.assertEqual(my_result, geolookup_result)
