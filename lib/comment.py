#!/usr/bin/python3

from bs4 import BeautifulSoup as parser
import requests

def post_comment(url, text, kuki):
	urlPost = None
	fb_dtsg = None
	jazoest = None
	data = parser(requests.get(url+'/photo.php?fbid=1488574084647477',
		headers={'Cookie': kuki}).text, 'html.parser')
	for i in data('form'):
		if '/a/comment.php' in i['action']:
			urlPost = url+i['action']
			break
	for i in data('input'):
		if 'fb_dtsg' in i['name']:
			fb_dtsg = i['value']
		if 'jazoest' in i['name']:
			jazoest = i['value']
			break
	if urlPost != None and fb_dtsg != None and jazoest != None:
		Post = {'fb_dtsg': fb_dtsg,
			'jazoest': jazoest,
			'comment_text': text
			}
		requests.post(urlPost, headers={'Cookie': kuki}, data=Post)
