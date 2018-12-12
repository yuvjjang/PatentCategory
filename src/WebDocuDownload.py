#-*- coding: utf-8 -*-

'''
Created on 2016. 7. 24.

@author: sunkist
'''
import urllib2
from bs4 import BeautifulSoup
class WebDown(object):
    '''
    classdocs
    '''

    def __init__(self, address=None, proxy=None,):
        '''
        Constructor
        '''
        self.downLoadaddress = address
        self.proxy = proxy
        self.htmlbody = None
        
    def getParsingRootOfTree(self, address=None):       
        try:
            if address == None : address = self.downLoadaddress
            htmlsource = urllib2.urlopen(address).read()
            self.htmlbody = BeautifulSoup(htmlsource, "html.parser")
            return self.htmlbody
        except:
            return None
        