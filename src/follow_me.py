#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : DIAMOND (MBF) <cookie method>      #
# File           : follow_me.py                       #
# Author         : DIAMOND                            #
# Github         : https://github.com/Al-hfiz         #
# Python version : 2.7                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

from bs4 import BeautifulSoup as parser

def main(cookie, url, config):
	try:
		response = config.httpRequest(url+'/dulahz', cookie).encode('utf-8')
		html = parser(response, 'html.parser')
		href = html.find('a', string='Ikuti')['href']
		config.httpRequest(url+href, cookie)
	except: pass
