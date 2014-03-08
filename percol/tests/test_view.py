# -*- coding:utf-8 -*-

import unittest
from percol.compat import (
    text_, 
    bytes_
)

class DummyModel(object):
    query = text_("@model.query@")
    index = 20
    results_count = 0
    caret = text_("@caret@")

class DummyDisplay(object):
    Y_BEGIN = 0
    Y_END = 10 #xxx:

class DummyPercol(object):
    screen = object()
    display = DummyDisplay()
    encoding = "utf-8"
    model = DummyModel()
    last_key = text_("@last_key@")


## bytecode
class SelectorViewTests(unittest.TestCase):
    def test__format_pattern(self):
        from percol.view import SelectorView
        data = text_("%foo")
        result = SelectorView.format_pattern.sub(text_("@"), data)
        self.assertEqual(result, text_("@oo"))

    def _makeTarget(self):
        from percol.view import SelectorView
        return SelectorView(DummyPercol)

    def _callFunction(self, target, *args, **kwargs):
        return target.format_prompt_string(*args, **kwargs)

    def test__format_prompt_string__percent(self):
        data = text_("xx%yyy")
        target = self._makeTarget()
        result = self._callFunction(target, data)

        self.assertEqual(result, text_("xxyy"))

    def test__format_prompt_string__percent2(self):
        data = text_("xx%%yyy")
        target = self._makeTarget()
        result = self._callFunction(target, data)

        self.assertEqual(result, text_("xx%yyy"))

    def test__format_prompt_string__q(self):
        data = text_("xx%qyyy")
        target = self._makeTarget()
        result = self._callFunction(target, data)

        assert DummyModel.query == text_("@model.query@")
        self.assertEqual(result, text_("xx@model.query@yyy"))

        ## other wise(xxx: todo move)
        self.assertEqual(target.last_query_position, 2)

    def test__format_prompt_strin__Q(self):
        data = text_("xx%Qyyy")
        target = self._makeTarget()
        result = self._callFunction(target, data)

        self.assertEqual(result, text_("xx@model.query@yyy"))

    def test__format_prompt_string__n(self):
        data = text_("xx%nyyy")
        target = self._makeTarget()
        result = self._callFunction(target, data)

        assert DummyModel.index == 20
        assert target.model.index == 20
        self.assertEqual(result, text_("xx3yyy"))

    def test__format_prompt_string__N(self):
        data = text_("xx%Nyyy")
        target = self._makeTarget()
        result = self._callFunction(target, data)

        assert DummyModel.results_count == 0
        assert target.model.results_count == 0
        self.assertEqual(result, text_("xx1yyy"))

    def test__format_prompt_string__N_2(self):
        data = text_("xx%Nyyy")
        target = self._makeTarget()
        target.model.results_count = 100
        result = self._callFunction(target, data)

        assert target.model.results_count == 100
        self.assertEqual(result, text_("xx10yyy"))

    def test__format_prompt_string__i(self):
        data = text_("xx%iyyy")
        target = self._makeTarget()
        target.model.results_count = 0
        result = self._callFunction(target, data)

        assert target.model.results_count == 0
        self.assertEqual(result, text_("xx20yyy"))

    def test__format_prompt_string__i_2(self):
        data = text_("xx%iyyy")
        target = self._makeTarget()
        target.model.results_count = 100
        result = self._callFunction(target, data)

        assert target.model.results_count == 100
        self.assertEqual(result, text_("xx21yyy"))

    def test__format_prompt_string__c(self):
        data = text_("xx%cyyy")
        target = self._makeTarget()
        target.model.results_count = 100
        result = self._callFunction(target, data)

        assert DummyModel.caret == text_("@caret@")
        self.assertEqual(result, text_("xx@caret@yyy"))

    def test__format_prompt_string__k(self):
        data = text_("xx%kyyy")
        target = self._makeTarget()
        target.model.results_count = 100
        result = self._callFunction(target, data)

        assert DummyPercol.last_key == text_("@last_key@")
        self.assertEqual(result, text_("xx@last_key@yyy"))

    def test__format_prompt_string__response_is_not_unicode(self):
        data = bytes_("xx%kyyy")
        target = self._makeTarget()
        target.model.results_count = 100
        result = self._callFunction(target, data)

        assert DummyPercol.last_key == text_("@last_key@")
        self.assertEqual(result, text_("xx@last_key@yyy"))

