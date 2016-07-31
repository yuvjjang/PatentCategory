#-*- coding: utf-8 -*-

'''
Created on 2016. 7. 24.

@author: sunkist
'''
from ClassMainAddress import ClassAddress as ca
from WebDocuDownload import WebDown as wd
from USCParsing import ClassParsing as cp

ad = ca().cpcMainAddress()
soup = wd().getParsingRootOfTree(ad)


"""
ad = ca().uscMainAddress()
soup = wd().getParsingRootOfTree(ad)
mainNumList, mainTitleList = cp().getMainTitle(soup)

for pair in mainNumList:
    print pair
    ad = ca().uscSubAddress(pair)
    soup = wd().getParsingRootOfTree(ad)
    subNumList, subTitleList = cp().getSubTitle(soup)
    descList = []
    ad = ca().uscDescriptionAddress(pair)
    print ad
    soup = wd().getParsingRootOfTree(ad)
    for num in subNumList:   
        description = cp().getSubDescription(soup, pair, num)
        if description == None: description=u""
        descList.append((description,))
    
    subSummarize = zip(subNumList, subTitleList, descList)
    print len(subSummarize)
    for s in subSummarize:
        if len(s[0]) == 0: subSummarize.remove(s)
    print len(subSummarize)
"""
#subPair = subPair + tuple(cp().getSubDescription(soup, pair[0], subPair[0]))

