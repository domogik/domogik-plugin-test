#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This file is part of B{Domogik} project (U{http://www.domogik.org}).

License
=======

B{Domogik} is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

B{Domogik} is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Domogik. If not, see U{http://www.gnu.org/licenses}.

Plugin purpose
==============

Testing Plugin support

@author: Maikel Punie <maikel.punie@gmail.com>; Nico0084 <Nico84dev at gmail.com>
@copyright: (C) 2007-20019 Domogik project
@license: GPL(v3)
@organization: Domogik
"""

from domogik.xpl.common.xplmessage import XplMessage
from domogik.xpl.common.plugin import XplPlugin
from domogik.xpl.common.xplconnector import Listener
from domogik_packages.plugin_test.lib.test import TestRemoteManager
import traceback

class TestManager(XplPlugin):
    """
    Managages the test domogik plugin
    """
    def __init__(self):
        """ Init plugin
        """
        XplPlugin.__init__(self, name='test')

        # check if the plugin is configured. If not, this will stop the plugin and log an error
        if not self.check_configured():
            return

        # get the config values
        device_type = self.get_config("dummy")
        if device_type == None:
            self.log.error('dummy is not configured, exitting')
            self.force_leave()
            return
        # get the devices list
        self.devices = self.get_device_list(quit_if_no_device = False)
        self.remoteManager = TestRemoteManager(self, self.send_xpl, self.send_mq, self.get_stop())
        for a_device in self.devices :
            try :
                if a_device['device_type_id'] not in ['test.xpltest', 'test.mqtest'] :
                    self.log.error(u"Device type {0} : no plugin compatibility".format(a_device['device_type_id']))
                    break
                else :
                    self.remoteManager.addRemote(a_device)
                    self.log.debug("Ready to work with device {0}".format(a_device))
            except:
                self.log.error(traceback.format_exc())
                # we don't quit plugin if an error occured
                #self.force_leave()
                #return
         # Register pub client sensor
        self.add_mq_sub('client.sensor')
        self.add_mq_sub('device.update')
        self.add_mq_sub('device.new')
        Listener(self.process_test_basic, self.myxpl,{'xpltype': 'xpl-cmnd', 'schema': 'test.basic'})
        self.add_stop_cb(self.process_close)
        self.register_cb_update_devices(self.reload_devices)
        # notify ready
        self.log.info("Plugin ready :)")
        self.ready()

    def process_close(self):
        self.log.info(u'Close Plugin from request')

    def on_message(self, msgid, content):
        #Transmit mq message to manager
        XplPlugin.on_message(self, msgid, content)
        if msgid == 'client.sensor':
            self.remoteManager.handle_sensor_pub(content)
        elif msgid == "device.new" :
            self.log.debug("Receive <device.new> : {0}".format(content))
            a_device=content['device']
            try :
                if a_device['device_type_id'] not in ['test.xpltest', 'test.mqtest'] :
                    self.log.error(u"Device type {0} : no plugin compatibility".format(a_device['device_type_id']))
                else :
                    if self.remoteManager.addRemote(a_device):
                        self.log.debug("Ready to work with device {0}".format(a_device))
            except:
                self.log.error(traceback.format_exc())

    def reload_devices(self, devices):
        self.log.debug("Reload devices : {0}".format(devices))

    def send_xpl(self, schema, data):
        """ Send xPL message on network
        """
        self.log.info("schema:%s, data:%s" % (schema, data))
        msg = XplMessage()
        msg.set_type("xpl-trig")
        msg.set_schema(schema)
        for key in data:
            msg.add_data({key : data[key]})
        self.myxpl.send(msg)

    def send_mq(self, message):
        """ Send MQ given message
            @param message : MQ message
        """
        self.send(message)

    def process_test_basic(self, message):
        """ Process xpl schema test.basic
        """
        print(message)
        #self.send_xpl("lighting.device", message.data)
        device = message.data['device']
        chan = message.data['channel']
        if message.data["level"] == 'None':
            message.data["level"] = 0
        self.log.info(u'Test xpl commande sending message to {0},{1},{2}').format(device, chan, message.data["level"])

if __name__ == "__main__":
    TestManager()
