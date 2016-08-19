#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyho
----------------------------------

Tests for `pyho` module.
"""

import sys
import datetime
import unittest

from pyho import pyho


class TestPyho(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_laugh(self):
        self.assertEqual(pyho.laugh(), 'hohoho')

    def test_yyyymmdd_to_dt(self):
        self.assertEqual(pyho.yyyymmdd_to_dt(20151225), datetime.date(2015, 12, 25))

    def test_yyyymmdd_to_dt_error(self):
        with self.assertRaises(ValueError):
            pyho.yyyymmdd_to_dt(20161232)


if __name__ == '__main__':
    sys.exit(unittest.main())
