#!/usr/bin/python
'''
Provider to read Moddata from Curse.com
'''    
Name      = "Curse"
Type      = "Remote"
BaseURL   = "http://www.curse.com/addons/wow"
__self__  = Provider.Cuse
def __init__():
    ''' Cache HTML Page so that not every functions needs to pull it'''
    __self__.html_page = Tools.GetHtmlPage(Url)
    soup               = BeautifulSoup(__self__.html_page)

class Mod:
    ''' Read Moddata from Curse, contains standard methods to return imformations like other Provider'''
    def Name(Shortnames):
	pass
    def Description(Url):
	pass
    def Version(Url):
	pass
    def ProjectUrl(Url):
	pass
    def Url(shortname):
	return BaseURL+self.shortname
    def DownloadUrl(self.Url):
	''' get the download url - return list of files '''
	self.__return_urls__  =   []
	self.html_page        =   Tools.GetHtmlPage(DownloadUrl)
	for link in  __self__.soup.findAll('a'):
	    self.cur_url = link.get('data-href')
	    if self.cur_url:
		print(self.cur_url)
		self.__return_urls__.append(cur_url)
	    
	return self.__return_urls__
    def RequiredDepencies():
	pass
    def OptionalDepencies():
	pass
    def Add():
	return False
    def Remove():
	return False

class DB:
    Type = "Raw"
    def Fetch():
	return True
    def Update():
	'''
	Remote Provider doesn't allow update
	'''
	return False
    def LastAcces():
	return True
    def LastModifed():
	return True
    def SourceProvider():
	return  __self__.Curse.Name
    def SyncStatus():
	'''
	Remote Providers are always out of sync
	'''
	return False 