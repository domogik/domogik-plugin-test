#!/usr/bin/python
# -*- coding: utf-8 -*-

from domogik.tests.common.testplugin import TestPlugin
from domogik.common.utils import get_sanitized_hostname

tp = TestPlugin('test', get_sanitized_hostname())
tp.request_startup()
