# -*- coding:utf-8 -*-
import unittest
from percol.compat import xrange_

class ListIO(object):
    def __init__(self):
        self.result = []

    def write(self, x):
        self.result.append(x)

def getnumbers(n, io):
    for x in xrange_(0, n):
        io.write(x)
        yield x

class LazyArrayTests(unittest.TestCase):
    def _makeTarget(self, *args, **kwargs):
        from percol.lazyarray import LazyArray
        return LazyArray(*args, **kwargs)

    def test_rest_elements_are_not_consumed(self):
        tmp = ListIO()
        target = self._makeTarget(getnumbers(20, tmp))
        value_7 = target[7]
        self.assertEqual(value_7, 7)
        self.assertEqual(tmp.result, [0, 1, 2, 3, 4, 5, 6, 7])

    def test_rest_elements_are_not_consumed_and_cache(self):
        tmp = ListIO()
        target = self._makeTarget(getnumbers(20, tmp))
        value_7 = target[7]
        value_3 = target[3]
        self.assertEqual(value_7, 7)
        self.assertEqual(value_3, 3)
        self.assertEqual(tmp.result, [0, 1, 2, 3, 4, 5, 6, 7])


    def test_after_read_all_same_as_array(self):
        tmp = ListIO()
        target = self._makeTarget(getnumbers(20, tmp))
        self.assertEqual(list(target), list(range(0, 20)))
        self.assertEqual(tmp.result, list(range(0, 20)))
