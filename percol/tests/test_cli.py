# -*- coding:utf-8 -*-
import unittest

from percol.compat import NativeIO, text_, text_type
import mock

class CLITests(unittest.TestCase):
    def test_read_input(self):
        from percol.cli import read_input
        io = NativeIO(text_("this\nis\ntest\message.."))

        with mock.patch("sys.stdin", io):
            result = list(read_input(None, "utf-8"))
            self.assertTrue(isinstance(result[0], text_type))
            self.assertEqual(
                text_("\n").join(result),
                text_("this\nis\ntest\message..")
            )

