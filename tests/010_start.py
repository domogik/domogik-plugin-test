#!/usr/bin/python
# -*- coding: utf-8 -*-

from domogik.tests.common.testplugin import TestPlugin
from domogik.common.utils import get_sanitized_hostname
from domogikmq.reqrep.client import MQSyncReq
from domogikmq.message import MQMessage
import time
import zmq

tp = TestPlugin('test', get_sanitized_hostname())
tp.request_startup()

time.sleep(10)
cli = MQSyncReq(zmq.Context())
msg = MQMessage()
msg.set_action('client.list.get')
req = cli.request('manager', msg.get(), timeout=10)

if req:
    data = req.get()[1]
    found = False
    for cli in data:
        if cli == "plugin-test.{0}".format(get_sanitized_hostname()):
            found = True
            state = data[cli]["status"]
            if state != "alive":
                assert RuntimeError("MQ REQ client.list.get is saying the plugin is {0}".format(state))
    if not found:
        assert RuntimeError("MQ REQ client.list.get is not returning this plugin")
else:
    assert RuntimeError("MQ request to manager failed")

