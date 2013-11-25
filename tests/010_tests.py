#!/usr/bin/python
# -*- coding: utf-8 -*-

from domogik.xpl.common.plugin import XplPlugin
from domogik.tests.common.plugintestcase import PluginTestCase
from domogik.tests.common.testplugin import TestPlugin
from domogik.tests.common.testdevice import TestDevice
from domogik.tests.common.testsensor import TestSensor
from domogik.common.utils import get_sanitized_hostname
from datetime import datetime
import unittest
import sys
import os
import traceback

class TestPluginTestCase(PluginTestCase):



if __name__ == "__main__":
    ### global variables
    interval = 1    
    path = "/home"

    ### configuration

    # set up the xpl features
    xpl_plugin = XplPlugin(name = 'test', 
                           daemonize = False, 
                           parser = None, 
                           nohub = True,
                           test  = True)

    # set up the plugin name
    name = "diskfree"

    # set up the configuration of the plugin
    # configuration is done in test_0010_configure_the_plugin with the cfg content
    # notice that the old configuration is deleted before
    cfg = { 'configured' : True }
   

    ### start tests

    # load the test devices class
    td = TestDevice()

    # delete existing devices for this plugin on this host
    client_id = "{0}-{1}.{2}".format("plugin", name, get_sanitized_hostname())
    try:
        td.del_devices_by_client(client_id)
    except: 
        print(u"Error while deleting all the test device for the client id '{0}' : {1}".format(client_id, traceback.format_exc()))
        sys.exit(1)

    # create a test device
    try:
        device_id = td.create_device(client_id, "test_device_diskfree", "diskfree.disk_usage")
        td.configure_global_parameters({"device" : path, "interval" : interval})
    except: 
        print(u"Error while creating the test devices : {0}".format(traceback.format_exc()))
        sys.exit(1)
    
    ### prepare and run the test suite
    suite = unittest.TestSuite()
    # check domogik is running, configure the plugin
    suite.addTest(DiskfreeTestCase("test_0001_domogik_is_running", xpl_plugin, name, cfg))
    suite.addTest(DiskfreeTestCase("test_0010_configure_the_plugin", xpl_plugin, name, cfg))
    
    # start the plugin
    suite.addTest(DiskfreeTestCase("test_0050_start_the_plugin", xpl_plugin, name, cfg))

    # do the specific plugin tests
    #suite.addTest(DiskfreeTestCase("test_0100_dummy", xpl_plugin, name, cfg))
    suite.addTest(DiskfreeTestCase("test_0110_total_space", xpl_plugin, name, cfg))
    suite.addTest(DiskfreeTestCase("test_0120_free_space", xpl_plugin, name, cfg))
    suite.addTest(DiskfreeTestCase("test_0130_used_space", xpl_plugin, name, cfg))
    suite.addTest(DiskfreeTestCase("test_0140_percent_used", xpl_plugin, name, cfg))

    # do some tests comon to all the plugins
    suite.addTest(DiskfreeTestCase("test_9900_hbeat", xpl_plugin, name, cfg))
    suite.addTest(DiskfreeTestCase("test_9990_stop_the_plugin", xpl_plugin, name, cfg))
    
    # quit
    res = unittest.TextTestRunner().run(suite)
    xpl_plugin.force_leave()
    sys.exit(res.wasSuccessful())
    
