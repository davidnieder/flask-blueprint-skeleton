# -*- coding: utf-8 -*-

import unittest

from app import create_app


class APITests(unittest.TestCase):

    def setUp(self):
        self.client = create_app(config='testing').test_client()

    def test_apihello(self):
        resp = self.client.get('/api/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.mimetype, 'application/json')
        self.assertTrue('"message": "hello api"' in resp.get_data())
