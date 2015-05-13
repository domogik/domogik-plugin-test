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
print(cli.request('manager', msg.get(), timeout=10).get())

