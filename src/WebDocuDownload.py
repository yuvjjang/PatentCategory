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


    def __init__(self, address=None):
        '''
        Constructor
        '''
        self.downLoadaddress = address
        self.htmlbody = None
        
    def getParsingRootOfTree(self, address):       
        try:
            htmlsource = urllib2.urlopen(address).read()
            return BeautifulSoup(htmlsource, "html.parser")
        except:
            return None
        