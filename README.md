domogik-plugin-test
=====================

This is a test plugin, the only reason for this plugin is to have some automated testcases for domogik, the folowing actions will be tested:

1- install the plugin
2- configure the plugin
    a- mq request
    b- check for a published message
3- start the plugin
    a- mq request
    b- cehck for a published message
4- create a device (rest)
5- send an xpl command (rest)
6- wait for an xplstat 
7- check sensor table + sensorhistory table (rest)
8- delete the device (rest)
9- stop the plugin (mq)
10- uninstall the plugin

This will create a basic sanity check for domogik, these test will run on travis and maybe later on be used as an initial config tester before the suers start to use domogik.
