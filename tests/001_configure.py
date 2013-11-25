#!/usr/bin/python

from domogik.tests.common.helpers import configure, delete_configuration, check_config
from domogik.common.utils import get_sanitized_hostname

print "==> Set the config"
delete_configuration("plugin", "test", get_sanitized_hostname())
configure("plugin", "test", get_sanitized_hostname(), "configured", True)
configure("plugin", "test", get_sanitized_hostname(), "dummy", "dummyConfigParam")

print "==> Check the config"
check_config("plugin", "test", get_sanitized_hostname(), "configured", True)
check_config("plugin", "test", get_sanitized_hostname(), "dummy", "dummyConfigParam")
