# -*- coding: utf-8 -*-

import unittest

from app import create_app


class ViewTests(unittest.TestCase):

    def setUp(self):
        self.client = create_app(config='testing').test_client()

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.mimetype, 'text/html')
        self.assertTrue('<p>hello index</p>' in resp.get_data())
