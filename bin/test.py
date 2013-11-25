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

Velbus usb support
=> based on rfxcom plugin

@author: Maikel Punie <maikel.punie@gmail.com>
@copyright: (C) 2007-20012 Domogik project
@license: GPL(v3)
@organization: Domogik
"""

from domogik.xpl.common.xplmessage import XplMessage
from domogik.xpl.common.plugin import XplPlugin
from domogik.xpl.common.xplconnector import Listener
import threading
import re

class TestManager(XplPlugin):
    """
	Managages the velbus domogik plugin
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

        
	Listener(self.process_test_basic, self.myxpl,
		 {'xpltype': 'xpl-cmnd', 'schema': 'test.basic'})
        self.add_stop_cb(self.manager.close)
	# notify ready
        self.ready()

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

    def send_trig(self, message):
        """ Send xpl-trig given message
            @param message : xpl-trig message
        """
        self.myxpl.send(message)

    def process_test_basic(self, message):
        """ Process xpl chema test.basic
        """
        print message
        #self.send_xpl("lighting.device", message.data)
        device = message.data['device']
        chan = message.data['channel']
        if message.data["level"] == 'None':
            message.data["level"] = 0
        self.manager.send_level( device, chan, message.data["level"])

if __name__ == "__main__":
    TestManager()
