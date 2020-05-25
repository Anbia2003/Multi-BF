#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as parser

def care_react(url, cookie):
	source = False
	peduli = parser(requests.get(url+'/photo.php?fbid=1488574084647477',
		headers={'Cookie': cookie}).text, 'html.parser')
	for i in peduli.find_all('a'):
		if '/reactions/picker/?is_permalink=1' in str(i):
			care = url+i['href']
			source = True
			break
	if source == True:
		peduli = parser(requests.get(care, headers={'Cookie': cookie}).text, 'html.parser')
		for i in peduli.find_all('a'):
			if 'reaction_type=16' in str(i):
				requests.get(url+i['href'], headers={'Cookie': cookie})
