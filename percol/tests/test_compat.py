# -*- coding:utf-8 -*-
import unittest

class DontReach(Exception):
    pass

class DummyIterator(object):
    def __iter__(self):
        yield 1
        raise DontReach()

class LazynessIterationTests(unittest.TestCase):
    def test_iteritems__map(self):
        from percol.compat import (
            iteritems_,
            map_
        )

        dummy = iter(DummyIterator())
        data = {1: dummy, 2:dummy}

        with self.assertRaises(DontReach):
            next(map_(lambda p: next(p[1]), iteritems_(data)))

    def test_iteritems__imap(self):
        from percol.compat import (
            iteritems_,
            imap_
        )

        dummy = iter(DummyIterator())
        data = {1: dummy, 2:dummy}

        result = next(imap_(lambda p: next(p[1]), iteritems_(data)))
        self.assertEqual(result, 1)

    def test_xrange(self):
        from percol.compat import xrange_
        self.assertNotEqual(type(xrange_(1000000000000000000)), list)
