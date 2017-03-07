#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14  2017

@author: keyu
Requirement:  
    An script capable of collecting all the Twitter handles listed on a set of web pages. 
    Input given a list of URLs, output a list of twitter handles for each URL.
"""
from flask import *
import re
import urllib2
import json
import sys

main = Blueprint('main', __name__, template_folder='templates')
# geturl_api = Blueprint('geturl_api', __name__, template_folder='templates')

#Credit to Django project
# https://code.djangoproject.com/browser/django/trunk/django/core/validators.py#L47
#Input: String
#Output: URL if it is vaild
def is_valid_url(url):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    # if url is not None and regex.search(url):
    #     return regex.search(url).group(0)
    # else:
    #     return None
    return url is not None and regex.search(url)

@main.route('/',methods =['GET','POST'])
def main_route():
	options={}
	# sample_list = ['https://www.pastemagazine.com/articles/2017/01/the-75-best-twitter-accounts-of-2016-1.html',
               # 'https://www.pastemagazine.com/articles/2016/01/the-75-best-twitter-accounts-of-2015.html']
	
	def crawlWeb(url_list):
		url_handle_dict = {}
		reg1 = r'(?:@[\w_]+)' 
		for i in url_list:
			if is_valid_url(i):
				try:
					response = urllib2.urlopen(i)
					html_doc = response.read()
					handle_list = re.findall(reg1, html_doc)
					url_handle_dict[i] = handle_list
				except:
					url_handle_dict[i] = "Invalid URL"
			else:
				url_handle_dict[i] = 'This is not a valid URL'
		return url_handle_dict

	if request.method == 'POST':
		sample_list = request.form['url_list'].split()
		url_handle_dict = crawlWeb(sample_list)
		options = {'params':url_handle_dict}
	return render_template("index.html", **options)

#Implement REST API When have time
# @geturl_api.route('/api/geturl', methods=['POST'])
# def geturl_route():
# 	content = request.get_json()
# 	return jsonify(), 200