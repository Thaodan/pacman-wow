#!/usr/bin/python
Name     = "Modinfo"
Type     = "any"
__self__ = Provider.Modinfo
def __init__(self, mode, DBurl ):
    self.mode   = mode
    self.DBurl  = DBurl
    return self
    
class Mod:
    def __init__(self, mod):
        # open mod file here
        self.mod = open(mod)
        return self

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
    def DownloadUrl(Url):
      return BaseURL+self.shortname+"/download"
    def RequiredDepencies():
	pass
    def OptionalDepencies():
	pass
    def Add():
	return False
    def Remove():
	return False
class DB:
    Type = Raw
    def Fetch():
	return True
    def Update():
	'''
	Remote Provider doesn\'t allow update
	'''
	return False
    def LastAcces():
	return True
    def LastModifed():
	return True
    def SourceProvider():
	return  __self__.Name
    def SyncStatus():
	'''
	Remote Providers are always out of sync
	'''
	return False 
  



'''
Provider.Local = Provider.Modinfo(local,CONFIG_DIR + "/native")
Mod            = Provider.Local.Mod("test")
print(Mod.Description)


'''
