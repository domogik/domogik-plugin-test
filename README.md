domogik-plugin-test
=====================

This is a test plugin, the only reason for this plugin is to have some automated testcases for domogik, the folowing actions will be tested:

1. install the plugin
    a. [OK] dmg_package -i <url of stable version>
2. Run testcases
    001. [OK] Config
    010. [OK] start
    020. device
        * request the params (and validate)
            * [OK] Over MQ
            * Over REST
        * create a device
    030. sensor
        * request current data
        * wait for sensor value
        * request current data
    040. command
        * create a command
        * wait for sensor update
    090. [OK] stop
3. uninstall the plugin
    a. [OK] -dmg_package -r plugin_test

This will create a basic sanity check for domogik, these test will run on travis and maybe later on be used as an initial config tester before the suers start to use domogik.

The testcases are all stored here in the plugin, so we can use the testrunner to simple run the testcases from within domogik.
