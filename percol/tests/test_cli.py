# -*- coding:utf-8 -*-
import unittest

from percol.compat import NativeIO, text_
import mock

class CLITests(unittest.TestCase):
    def test_read_input(self):
        from percol.cli import read_input
        io = NativeIO(text_("this\nis\ntest\message.."))
        with mock.patch("sys.stdin", io):
            result = list(read_input(None, "utf-8"))
            
