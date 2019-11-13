from domogik.tests.common.testdevice import TestDevice
from domogik.common.utils import get_sanitized_hostname

cid = "plugin-test.{0}".format(get_sanitized_hostname())
t = TestDevice()

# an xpl device
params = t.get_params(cid, "test.xpltest")
params['name'] = 'Test-xpl-device(éèàî)'
params['reference'] = 'Test-xpl-reference (éèàî)'
params['description'] = 'Test-xpl-description (éèàî'
# global params
for the_param in params['global']:
    if the_param['key'] == "DeviceTypeParamNoXPL":
        the_param['value'] = 150
    if the_param['key'] == "timer_status":
        the_param['value'] = 10
# xpl params
for the_param in params['xpl']:
    if the_param['key'] == "DeviceTypeParam":
        the_param['value'] = 'xpl-set-devicetype (éèàî)'
params['xpl_stats']['test_xpl_stat'][0]['value'] = 'xpl-stat-set-device (éèàî)'
params['xpl_commands']['test_xpl_command'][0]['value'] = 200
dev = t.create_device(params)

# an mq device
params = t.get_params(cid, "test.mqtest")
params['name'] = 'Test-mq-device (éèàî)'
params['reference'] = 'Test-mq-reference(éèàî)'
params['description'] = 'Test-mq-description(éèàî)'
# global params
for the_param in params['global']:
    if the_param['key'] == "DeviceTypeParam":
        the_param['value'] = 150
    if the_param['key'] == "timer_status":
        the_param['value'] = 10
dev = t.create_device(params)
