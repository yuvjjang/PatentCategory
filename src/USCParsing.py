#-*- coding: utf-8 -*-

'''
Created on 2016. 7. 24.

@author: sunkist
'''

class ClassParsing(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        
    def getMainTitle(self, soup):
        numList = soup.find_all("td", width="27")
        numListText = []
        for l in numList:
            numListText.append(l.get_text())

        titleList = soup.find_all("td", width="532")
        titleListText = []
        for l in titleList:
            titleListText.append(l.get_text())

        return numListText, titleListText
        
    def getSubTitle(self, soup):
        numList = soup.find_all("td", width="99")
        numListText = []
        for l in numList:
            numListText.append(l.get_text().strip())

        titleList = soup.find_all("td", class_="SubTtl")
        titleListText = []
        for l in titleList:
            titleListText.append(l.get_text().strip())

        return numListText, titleListText
    
    def getSubDescription(self, soup, mainNum, subNum):
        pointSplit = subNum.split('.')
        integers = pointSplit[0]
                
        if len(integers) <3 : 
            integers = '0'*(3-len(integers)) + integers

        if len(pointSplit) == 2:
            points = pointSplit[1]
            if len(points) <3 :
                points = points + '0'*(3-len(points))
        else: points = "000"
            
        revisedSubNum = 'C'+mainNum+'S'+integers + points 
        print revisedSubNum
        subNumSoup = soup.find("a", {"name":revisedSubNum})
        if subNumSoup == None: return None
        return subNumSoup.parent.parent.parent.next_sibling.next_sibling.get_text()
        
        