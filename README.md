domogik-plugin-test
=====================

This is a test plugin, the only reason for this plugin is to have some automated testcases for domogik, the folowing actions will be tested:

1. [OK] install the plugin: dmg_package -i <url of stable version>
2. Run testcases
    001. [OK] Config
    010. [OK] start
    020. [OK] device
        * request the params
        * create a device
    030. Sensor
        * request current data
        * wait for sensor value
        * request current data
    040. Command
        * create a command
        * wait for sensor update
    080. [OK] Admin
        * call some admin urls and expect redirects to login page
        * call some rest urls
        * login to admin
        * call some /admin urls
    090. [OK] stop
3. [OK] uninstall the plugin: dmg_package -r plugin_test

This will create a basic sanity check for domogik, these test will run on travis and maybe later on be used as an initial config tester before the suers start to use domogik.

The testcases are all stored here in the plugin, so we can use the testrunner to simple run the testcases from within domogik.
