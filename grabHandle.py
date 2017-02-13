#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 18:13:21 2017

@author: keyu
Requirement:  
    An script capable of collecting all the Twitter handles listed on a set of web pages. 
    Input given a list of URLs, output a list of twitter handles for each URL.
"""

import re
import urllib2
import json
import sys

#Sample list for test 
sample_list = ['https://www.pastemagazine.com/articles/2017/01/the-75-best-twitter-accounts-of-2016-1.html',
               'https://www.pastemagazine.com/articles/2016/01/the-75-best-twitter-accounts-of-2015.html']

#Carwl a list of URLs and store corresonding handle in dictionary 
#Input: List
#Output: Dictionary {key = url : value = list of handles}

def crawlWeb(url_list):
    url_handle_dict = {}
    reg1 = r'(?:@[\w_]+)' 
    for i in url_list:
        response = urllib2.urlopen(i)
        html_doc = response.read()
        handle_list = re.findall(reg1, html_doc)
        url_handle_dict[i] = handle_list
        print len(handle_list)
    return url_handle_dict
    
if __name__ == "__main__":
    #Get URLs and correspnding handles.

    url_handle_dict = crawlWeb(sample_list)
    #Save result in txt file for later use.
    json.dump(url_handle_dict, open("url_handle.txt",'w'))