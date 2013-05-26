#!/usr/bin/python
''' 
Moddata Provider to read data from TocFile

'''
ProviderType = "Local" # Provider represents some parts of our Local Data
__self__     = Provider.Blizzard
class Mod:
    ''' Read Moddata from Blizzard TocFile, contains standard methods to return imformations like other Provider'''
    def __init__():
	TocFile = Tools.TocFile
	TocFile.OpenFile(Shortname)
    def Name(Url):
	return Tools.TocFile.ReadField('Title')
    def Description(Url):
	return Tools.TocFile.ReadField('Notes')
    def Version():
	return Tools.TocFile.ReadField('Version')
    def ProjectUrl(Url):
	return Tools.TocFile.ReadField('X-Website')
    def Url(shortname):
	return False
    def DownloadUrl(Url):
	return False # not aviable this provider only provides data
    def DownloadUrlL(DownloadUrls):
	return False # same 
    def RequiredDepencies():
	__required_depencies__ = []
	# FIXME: replace with cleaner code
	# see: www.wowpedia.org/The_TOC_Format#Depencies
	try:
	    __required_depencies__ = TocFile.ReadField('Require dDeps')
	except:
	    try: 
		__required_depencies__ = TocFile.ReadField('Depencies')
	    except:
		try:
		    __required_depencies__ = TocFile.ReadField('Deps')
		except:
		    return False

	return __required_depencies__
    
    def OptionalDepencies():
	return TocFile.ReadField('OptionalDeps')
    def Add():
	return False
    def Remove():
	return False

class DB:
    def __init__():
	pass
    def Fetch():
	pass
    def Update(source_db):
	return True
    def SyncStatus():
	return False
    def LastAcces():
	return True
    def LastModifed():
	return True
    def SourceProvider():
	return __self__.Name