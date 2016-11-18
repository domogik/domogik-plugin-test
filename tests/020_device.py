from domogik.tests.common.testdevice import TestDevice
from domogik.common.utils import get_sanitized_hostname

cid = "plugin-test.{0}".format(get_sanitized_hostname())
t = TestDevice()

# an xpl device
params = t.get_params(cid, "test.xpltest")
params['name'] = 'Test-xpl-device'
params['reference'] = 'Test-xpl-reference'
params['description'] = 'Test-xpl-description'
params['global'][0]['value'] = 'xpl-set-global'
params['xpl'][0]['value'] = 'xpl-set-devicetype'
params['xpl_stats']['test_xpl_stat'][0]['value'] = 'xpl-stat-set-device' 
params['xpl_commands']['test_xpl_command'][0]['value'] = 'xpl-cmd-set-device' 
dev = t.create_device(params)

# an mq device
params = t.get_params(cid, "test.mqtest")
params['name'] = 'Test-mq-device'
params['reference'] = 'Test-mq-reference'
params['description'] = 'Test-mq-description'
params['global'][0]['value'] = 'mq-set-global'
dev = t.create_device(params)
