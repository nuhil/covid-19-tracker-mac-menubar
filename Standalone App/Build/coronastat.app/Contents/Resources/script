#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import urllib2
import json


usa_response = urllib2.urlopen('https://covid19.mathdro.id/api/countries/USA')
usa_data = usa_response.read()
usa_data = json.loads(usa_data)

bd_response = urllib2.urlopen("https://covid19.mathdro.id/api/countries/Bangladesh")
bd_data = bd_response.read()
bd_data = json.loads(bd_data)

print("USA 😷" + str(usa_data['confirmed']['value']) + "😀" + str(usa_data['recovered']['value']) + "💀" + str(usa_data['deaths']['value']))
print("Bangladesh 😷" + str(bd_data['confirmed']['value']) + "😀" + str(bd_data['recovered']['value']) + "💀" + str(bd_data['deaths']['value']))