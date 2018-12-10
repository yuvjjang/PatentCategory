# -*- coding: utf-8 -*-

import logging
from urllib import request

logging.basicConfig(filename='example.log', format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',\
                    datefmt='%d-%m-%Y:%H:%M:%S',\
                    level=logging.DEBUG)
origin_addr = 'http://patft.uspto.gov/'
search_addr = 'http://patft.uspto.gov/netahtml/PTO/srchnum.htm'
example_num = ['6633616']

page_addr_format1 = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1='
page_addr_op1 = '.PN.&OS=PN/'
page_addr_op2 = '&RS=PN/'

search_page = page_addr_format1+example_num[0] + page_addr_op1 + page_addr_op2
logging.debug(search_page)
html = None

try:
    #request.Request
    #add header

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    #add cookie

    req = request.Request(search_page, headers = headers)
    resp = request.urlopen(req)
    respData = resp.read()
    logging.debug(respData)
except Exception as e:
    logging.debug(html)
    logging.debug(str(e))


