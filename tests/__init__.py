# -*- coding: utf-8 -*-

from unittest import TestLoader, TextTestRunner
from .view_tests import ViewTests


test_suite = TestLoader().loadTestsFromTestCase(ViewTests)

def run(verbosity=1):
    TextTestRunner(verbosity=verbosity).run(test_suite)

