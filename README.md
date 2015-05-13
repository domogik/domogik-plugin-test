domogik-plugin-test
=====================

This is a test plugin, the only reason for this plugin is to have some automated testcases for domogik, the folowing actions will be tested:

1- install the plugin
    [OK] dmg_package -i <url of stable version>
2- Run testcases
    [OK]- config + check config
    2- start + check running
    3- get device params + validate
    4- create device + validate the get_device
    5- stop plugin + start again (now we have a device)
    6- wait for sensor value to be stored (plugin sends it for every device every 30 seconds)
    7- send an command via rest and wait for the return
    8- rerun 6 (to make sure everything still works after the command sending)
    9- send a command where we will never have a result for
    10- delete device
    [OK]- stop plugin
3- uninstall the plugin
    [OK] -dmg_package -r plugin_test

This will create a basic sanity check for domogik, these test will run on travis and maybe later on be used as an initial config tester before the suers start to use domogik.

The testcases are all stored here in the plugin, so we can use the testrunner to simple run the testcases from within domogik.
