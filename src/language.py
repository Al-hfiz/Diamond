#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : DIAMOND (MBF) <cookie method>      #
# File           : language.py                        #
# Author         : Al-Hafiz                           #
# Github         : https://github.com/Al-hfiz         #
# Python version : 2.7                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

from bs4 import BeautifulSoup as parser

def main(cookie, url, config):
	try:
		response = config.httpRequest(url+'/language.php', cookie).encode('utf-8')
		html = parser(response, 'html.parser')
		for x in html.find_all('a'):
			if 'Bahasa Indonesia' in str(x):
				config.httpRequest(url+x['href'], cookie)
				break
	except: pass
