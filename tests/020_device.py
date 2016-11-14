import zmq
from zmq.eventloop.ioloop import IOLoop
from domogikmq.reqrep.client import MQSyncReq
from domogikmq.message import MQMessage

# Creating the client
cli = MQSyncReq(zmq.Context())

# build the message
msg = MQMessage()
msg.set_action('device.params')
msg.set_data({'device_type': 'test.test'})
toSend = msg.get()

# request it
print "Requesting device.params"
res = cli.request('dbmgr', toSend, timeout=10)
print "   result is {0}".format(res)

# check the result
if res:
    result = res.get()

    if not result:
        assert RuntimeError("MQ REQ device.params is not replying with the expected data: {0}".format(result))
    else:
        print "   result seems ok"
else:
    assert RuntimeError("MQ REQ device.params is not responding, result is {0}".format(res))


