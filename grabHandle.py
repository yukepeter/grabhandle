#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 18:13:21 2017

@author: keyu
"""

import re
import urllib2
import json

url_list1 = ['https://twitter.com/QueenOfSass','https://twitter.com/?lang=en','https://twitter.com/SportMan']
sample_list = ['https://www.pastemagazine.com/articles/2017/01/the-75-best-twitter-accounts-of-2016-1.html']
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
        #print len(handle_list)
    return url_handle_dict
    
if __name__ == "__main__":
    #Get URLs and correspnding handles.
    url_handle_dict = crawlWeb(sample_list)
    #Save result in txt file for later use.
    json.dump(url_handle_dict, open("url_handle.txt",'w'))