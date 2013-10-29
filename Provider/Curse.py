#!/usr/bin/python
'''
Provider to read Moddata from Curse.com
'''    
Name      = "Curse"
Type      = "Remote"
BaseURL   = "http://www.curse.com/addons/wow"
#__self__  = Provider.Cuse
from bs4 import BeautifulSoup 

class Mod:
    ''' Read Moddata from Curse, contains standard methods to return imformations like other Provider'''
    def __init__(self, Url):
        self.Url = Url
        self.html_page = GetHtmlPage(Url)
        self.soup      = BeautifulSoup(self.html_page)

    def Name(self, Shortnames):
        pass
    def Description(self, Url):
        pass
    def Version(self, Url):
        pass
    def ProjectUrl(self, Url):
        pass
    def Url(self):
        return BaseURL + shortname
    def DownloadUrl(self):
        ''' get the download url - return list of files '''
        __return_urls__  =   []
        __html_page__    =   GetHtmlPage(Url + "/download")
        __soup__ = BeautifulSoup(__html_page__)
        for link in  __soup__.findAll('a'):
            __cur_url__ = link.get('data-href')
            if __cur_url__:
                #print(self.cur_url)
                __return_urls__.append(__cur_url__)
	    
                return __return_urls__
    def RequiredDepencies(self):
        pass
    def OptionalDepencies(self):
        pass
    def Add(self):
        return False
    def Remove(self):
        return False

class DB:
    Type = "Raw"
    def Fetch():
        return True
    def Update():
        ''' Remote Provider doesn't allow update '''
        return False
    def LastAcces():
        return True
    def LastModifed():
        return True
    def SourceProvider():
        return  __self__.Curse.Name
    def SyncStatus():
        ''' Remote Providers are always out of sync '''
        return False 
