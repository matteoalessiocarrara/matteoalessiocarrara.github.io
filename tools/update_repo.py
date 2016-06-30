#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2016 Matteo Alessio Carrara <sw.matteoac@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import requests
import json

print "TODO inserire data ultimo aggiornamento"

r = requests.get("https://api.github.com/users/matteoalessiocarrara/repos")
j = json.loads(r.text)

swlist = open("../components/swlist.html", "w")
libs = open("../components/libs.html", "w")

is_lib = lambda name: True if name[:4] == "lib-" else False


swlist.write('<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">\n\n')
libs.write('<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">\n\n')

for repo in j:
	html = "<a  href=%s target=_blank>%s</a><br>\n\t%s<br><br>" % (repo['html_url'], repo['name'], repo['description'])
	f = libs if is_lib(repo['name']) else swlist
	f.write(html.encode('utf-8'))


