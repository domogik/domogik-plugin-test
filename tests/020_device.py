import zmq
import json
import requests
from zmq.eventloop.ioloop import IOLoop
from domogikmq.reqrep.client import MQSyncReq
from domogikmq.message import MQMessage
from domogik.common.utils import get_rest_url

### MQ testcase

# Creating the client
cli = MQSyncReq(zmq.Context())

# build the message
msg = MQMessage()
msg.set_action('device.params')
msg.set_data({'device_type': 'test.test'})
toSend = msg.get()

# request it
print "Requesting device.params over MQ"
res = cli.request('dbmgr', toSend, timeout=10)
print "   result is {0}".format(res)

# check the result
if res:
    resultMQ = res.get()
    if not resultMQ:
        assert RuntimeError("MQ REQ device.params is not replying with the expected data: {0}".format(resultMQ))
    else:
        resultMQ = json.loads(resultMQ[1])['result']
        print "   result seems ok"
else:
    assert RuntimeError("MQ REQ device.params is not responding, result is {0}".format(res))


### REST testcase
print "Requesting device.paramsi over REST"
# http://127.0.0.1:40406/rest/device/params/plugin-test.igor/test.test
res = requests.get('{0}/device/params/plugin-test.igor/test.test'.format(get_rest_url()))
if res:
    resultHTTP = res.text
    if not resultHTTP:
        assert RuntimeError("REST REQ device.params is not replying with the expected data: {0}".format(resultHTTP))
    else:
        resultHTTP = json.loads(resultHTTP)
        print "   result seems ok"
else:
    assert RuntimeError("MQ REQ device.params is not responding, result is {0}".format(res))
