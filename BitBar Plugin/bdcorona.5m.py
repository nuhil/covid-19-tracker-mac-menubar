#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# <bitbar.title>COVID-19 Tracker</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Nuhil Mehdy</bitbar.author>
# <bitbar.author.github>nuhil</bitbar.author.github>
# <bitbar.desc>Watch COVID-19 Statistics</bitbar.desc>
# <bitbar.image>https://github.com/nuhil/covid-19-tracker-mac-menubar/blob/master/icon.gif?raw=true</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.abouturl>https://github.com/nuhil/covid-19-tracker-mac-menubar</bitbar.abouturl>

import requests
from bs4 import BeautifulSoup

response = requests.get("https://covid19.mathdro.id/api/countries/Bangladesh")
data = response.json()
print("😷" + str(data['confirmed']['value']) + "😀" + str(data['recovered']['value']) + "💀" + str(data['deaths']['value']))
