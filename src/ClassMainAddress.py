#-*- coding: utf-8 -*-

'''
Created on 2016. 7. 24.

@author: sunkist
'''

#import urllib2
#from bs4 import BeautifulSoup

#usc class number and title address
#http://www.uspto.gov/web/patents/classification/selectnumwithtitle.htm
def uscMainAddress():
    return u"http://www.uspto.gov/web/patents/classification/selectnumwithtitle.htm"

#usc specific class number and title address
#http://www.uspto.gov/web/patents/classification/uspc002/sched002.htm
def uscSubAddress(subNum):
    return u"http://www.uspto.gov/web/patents/classification/uspc"+subNum+"/sched"+subNum+".htm"
 
#usc specific class description
def uscDescriptionAddress(mainNum): 
    return "http://www.uspto.gov/web/patents/classification/uspc"+mainNum+"/defs"+mainNum+".htm"

def cpcMainAddress():
    return u'http://www.uspto.gov/web/patents/classification/cpc.html'

def cpcSectionAddress(section):
    return "http://www.uspto.gov/web/patents/classification/cpc/html/cpc-"+section+".html"

