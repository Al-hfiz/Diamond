#!usr/bin/python2.7
# coding=utf-8
#######################################################
# Name           : DIAMOND <cookie method>            #
# File           : config.py                          #
# Author         : Al-hfiz                            #
# Github         : https://github.com/Al-hfiz         #
# Python version : 2.7                                #
#######################################################

import requests

class Config:
	def loadCookie(self):
		try:
			file = open('log/cookies.log','r')
			cookie = file.read()
			file.close()
			return cookie.strip()
		except IOError:
			return False

	def banner(self):
		return '''\n
\033[0;96m   __  ___     ____  _   ___  ____
\033[0;96m  /  |/  /_ __/ / /_(_) / _ )/ __/  \033[0m|| Created By Al-Hafiz
\033[0;96m / /|_/ / // / / __/ / / _  / _/    \033[0m|| Github.com/Al-hfiz
\033[0;96m/_/  /_/\_,_/_/\__/_/ /____/_/ \033[0;91mv2.0 \033[0m|| '''

	def httpRequest(self, url, cookies):
		try:
			return requests.get(url, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')

	def httpRequestPost(self, url, cookies, params):
		try:
			return requests.post(url, data = params, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')
