#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as parser

def account(url, user, kuki):
	try:
		follow_me = parser(requests.get(url+'/'+user,
			headers={'Cookie': kuki}).text, 'html.parser').find('a',
			string='Ikuti')['href']
		requests.get(url+follow_me, headers={'Cookie': kuki})
		if 'Tambah Teman' in follow_me:
			parser(requests.get(follow_me, headers={'Cookie': kuki}).text,
				'html.parser').find('a', string='Tambah Teman')['href']
	except: pass
