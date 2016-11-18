#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from domogik.common.utils import get_rest_url
from domogik.common.utils import get_sanitized_hostname

#tp = TestPlugin('test', get_sanitized_hostname())
s = requests.session()
cid="/client/plugin-test.{0}".format(get_sanitized_hostname())

def check_url ( url, code):
    r = s.get("{0}/{1}".format(get_rest_url(True), url), allow_redirects=False)
    if r.status_code == code:
        print("URL {0} get the expected code {1}".format(url, code))
    else:
        print("URL {0} get an unexpected code exp:{1} got:{2}".format(url, code, r.status_code))
        assert RuntimeError("URL {0} got an unexpected status code exp:{1} got:{2}".format(url, code, r.status_code))

print("Checking URLS without AUTH")
check_url( '/', 302)
check_url( '/error', 404)
check_url( '/login', 200)
check_url( '/clients', 302)
check_url( cid, 302)
check_url( '/scenario', 302)
check_url( '/scenario/edit/0', 302)
check_url( '/timeline/', 302)
check_url( '/battery/', 302)
check_url( '/orphans', 302)
check_url( '/users', 302)
print("")

print("Cheking rest URLS")
check_url('/rest/', 200)
check_url('/rest/map', 200)
check_url('/rest/device/', 200)
check_url('/rest/datatype', 200)
check_url('/rest/sensor/', 200)
print("")

print("Log in")
r = s.post("{0}/login".format(get_rest_url(True)), data={"user" : "admin", "passwd" : "123"})
print("")

print("Checking URLS that need authentication")
check_url( '/', 200)
check_url( '/clients', 200)
check_url( '/scenario', 200)
check_url( '/scenario/edit/0', 200)
check_url( '/timeline/', 200)
check_url( '/battery/', 200)
check_url( '/orphans', 200)
check_url( '/users', 200)
print("")

print("Cheking client specifick URLS with authentication")
check_url( cid, 200)
check_url( "{0}/config".format(cid), 200)
check_url( "{0}/dmg_devices/known".format(cid), 200)
check_url( "{0}/dmg_devices/new".format(cid), 200)
check_url( "{0}/dmg_devices/new/type/test.test".format(cid), 200)
check_url( "{0}/timeline".format(cid), 200)
check_url( "{0}/brain".format(cid), 200)
print("")

print("Log out")
check_url( '/logout', 302)
print("")

print("Checking URLS without AUTH")
check_url( '/', 302)
check_url( '/error', 404)
check_url( '/login', 200)
check_url( '/clients', 302)
check_url( '/scenario', 302)
check_url( '/scenario/edit/0', 302)
check_url( '/timeline/', 302)
check_url( '/battery/', 302)
check_url( '/orphans', 302)
check_url( '/users', 302)
print("")

