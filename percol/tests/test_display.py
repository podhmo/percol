# -*- coding:utf-8 -*-
import unittest
from percol.compat import text_

class ScreenLengthToBytesCount(unittest.TestCase):
    def _callFunction(self, *args, **kwargs):
        from percol.display import screen_length_to_bytes_count
        return screen_length_to_bytes_count(*args, **kwargs)

    def test_shorter_than_max_length(self):
        data = text_("this is test message")
        result = self._callFunction(data, 80, "utf-8")
        self.assertEqual(result, 20)

    def test_longer_than_max_length(self):
        data = text_("this is test message")
        result = self._callFunction(data, 10, "utf-8")
        self.assertEqual(result, 10)

class DummyScreen:
    def __init__(self):
        self.result = []

    def addnstr(self, y, x, raw_str, bytes_count_to_display, style):
        self.result.append((y, x, raw_str, bytes_count_to_display, style))

class DisplayTests(unittest.TestCase):
    def _makeTarget(self):
        from percol.display import Display
        from percol.markup import MarkupParser
        class DummyDisplay(Display):
            def __init__(self, screen, encoding):
                self.screen = screen
                self.encoding = encoding
                self.markup_parser = MarkupParser()
            WIDTH = 80
        return DummyDisplay(DummyScreen(), "utf-8")

    def test_add_aligned_string__filling(self):
        data = text_("this is test message")
        target = self._makeTarget()
        result = target.add_aligned_string(data, fill=True)

