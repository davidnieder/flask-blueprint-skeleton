# -*- coding: utf-8 -*-

from unittest import TestSuite, TestLoader, TextTestRunner
from .view_tests import ViewTests
from .api_tests import APITests


view_tests = TestLoader().loadTestsFromTestCase(ViewTests)
api_tests = TestLoader().loadTestsFromTestCase(APITests)

test_suite = TestSuite()
test_suite.addTests(view_tests)
test_suite.addTests(api_tests)

def run(verbosity=1):
    TextTestRunner(verbosity=verbosity).run(test_suite)
