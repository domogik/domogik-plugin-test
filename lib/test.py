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
=> based on rfxcom plugin

@author:  Nico0084 <Nico84dev at gmail.com>
@copyright: (C) 2007-2019 Domogik project
@license: GPL(v3)
@organization: Domogik
"""

import traceback
from domogik.common.utils import Timer

TEST_REMOTE_DEVICES = ['test.xpltest', 'test.mqtest']

def getRemoteId(device):
    """ Return key remote id for node list.
        return Id : <name>-<Id> (str)
                        None if error
    """
    if 'name' in device and 'id' in device:
        return "{0}-{1}".format(device['name'], device['id'])
    else : return None

def checkIfConfigured(deviceType,  device):
    """ Check if device_type have his all parameters configured.
        Methode must be update for all existing test device_type in json
    """
    if deviceType in TEST_REMOTE_DEVICES :
        configured = True
        for param in device["parameters"]:
            if device["parameters"][param]["value"] == "" : configured = False
        return configured
    return False

class TestException(Exception):
    """
    Test exception
    """

    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)


class TestRemoteManager:
    """
    Test domogik plugin
    """
    def __init__(self, plugin, cb_send_xpl, cb_send_mq, stop):
        """ Init object
            @param log : log instance
            @param cb_send_xpl : callback
            @param cb_send_mq : callback
            @param stop :
        """
        self._plugin= plugin
        self._log = plugin.log
        self._callback_xpl = cb_send_xpl
        self._callback_mq = cb_send_mq
        self._stop = stop
        self._dev = None
        self._devtype = 'serial'
        self._nodes = {}

    def addRemote(self, dmgDevice):
        """Add a RFPLayer from domogik device"""
        if dmgDevice["device_type_id"] in TEST_REMOTE_DEVICES :
            clID = getRemoteId(dmgDevice)
            if clID in self._nodes :
                self._log.debug("Manager Remote : node{0} already exist, not added.".format(clID))
                return False
            else:
                if checkIfConfigured(dmgDevice["device_type_id"], dmgDevice ) :
                    self._nodes[clID] = TestNode(dmgDevice, self._log)
                    self._log.info(u"Manager Remote : created new node {0}.".format(clID))
                    # Start thread for starting rfplayer services
                    timer = self._plugin.get_parameter(dmgDevice, 'timer_status')
                    if timer != 0 :
                        Timer(timer, self._nodes[clID].ping, self._plugin).start()
                    else :
                        self._log.info(u"Ping timer for node {0} disable.".format(clID))
                else :
                    self._log.warning(u"Manager Remote : device not configured can't add new node {0}.".format(clID))
                    return False
            return True
        else :
            self._log.error(u"Manager Remote : node type {0} not exist, not added.".format(clID))
            return False

    def removeRemote(self, clID):
        """Remove a remote node """
        node = self._nodes(clID)
        if node :
            self._log.info(u"Manager Remote : remove node {0}.".format(clID))
            self._nodes.pop(clID)

    def send_level(self, clID, channel, level):
        """ Set the level for a device
            if relay => level can only be 0 or 100
            if dimmer => level can be anything from 0 to 100
        """
        self._log.info("received set_level for {0}".format(clID))
        return

class TestNode(object):
    """Class to simulate a device"""

    def __init__(self, device, log):
        """Init class"""
        self._device = device
        self._log = log

    def ping(self):
        """ Simulate ping on a node"""
        self._log.info("Node {0} simulate ping".format(getRemoteId(self._device)))

    def updateDevice(self, device):
        self._device = device


