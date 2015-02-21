#!/usr/bin/python
# -*- coding: utf-8 -*-


from domogik.tests.common.testdevice import TestDevice
from domogik.common.utils import get_sanitized_hostname

td = TestDevice()
td.create_device("plugin-test.{0}".format(get_sanitized_hostname()), "test_plugin_device", "test.test")

