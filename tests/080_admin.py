#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from domogik.common.utils import get_rest_url

s = requests.session()

def check_url ( url, code):
    r = s.get("{0}/{1}".format(get_rest_url(True), url), allow_redirects=False)
    if r.status_code == code:
        print("URL {0} get the expected code {1}".format(url, code))
    else:
        print("URL {0} get an unexpected code exp:{1} got:{2}".format(url, code, r.status_code))
        assert RuntimeError("URL {0} got an unexpected status code exp:{1} got:{2}".format(url, code, r.status_code))

print("Checking normal URLS")
check_url( '/', 302)
check_url( '/error', 404)
check_url( '/login', 200)
check_url( '/clients', 302)

print("Cheking rest URLS")
check_url('/rest/', 200)
check_url('/rest/device/', 200)
check_url('/rest/datatype', 200)
check_url('/rest/sensor/', 200)

print("Log in")
r = s.post("{0}/login".format(get_rest_url(True)), data={"user" : "admin", "passwd" : "123"})

check_url( '/', 200)
check_url( '/clients', 200)
check_url( '/scenario', 200)
check_url( '/scenario/edit/0', 200)
check_url( '/timeline/', 200)
check_url( '/battery/', 200)
check_url( '/orphans', 200)
check_url( '/users', 200)
