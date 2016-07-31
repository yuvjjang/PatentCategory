#-*- coding: utf-8 -*-

'''
Created on 2016. 7. 24.

@author: sunkist
'''

#import urllib2
#from bs4 import BeautifulSoup

class ClassAddress(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.mainClassTitlePairList = []
    
    #usc class number and title address
    #http://www.uspto.gov/web/patents/classification/selectnumwithtitle.htm
    def uscMainAddress(self):
        return u"http://www.uspto.gov/web/patents/classification/selectnumwithtitle.htm"
    
    #usc specific class number and title address
    #http://www.uspto.gov/web/patents/classification/uspc002/sched002.htm
    def uscSubAddress(self, subNum):
        return u"http://www.uspto.gov/web/patents/classification/uspc"+subNum+"/sched"+subNum+".htm"
     
    #usc specific class description
    def uscDescriptionAddress(self, mainNum): 
        return "http://www.uspto.gov/web/patents/classification/uspc"+mainNum+"/defs"+mainNum+".htm"
    
    def cpcMainAddress(self):
        return u'http://www.uspto.gov/web/patents/classification/cpc.html'
    
    def cpcSectionAddress(self, section):
        return "http://www.uspto.gov/web/patents/classification/cpc/html/cpc-"+section+".html"
    
    