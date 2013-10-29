#!/usr/bin/python
''' 
Moddata Provider to read data from TocFile

'''

config = CONFIG_DIR + 'blizzard.cfg'

Type = "Local" # Provider represents some parts of our Local Data
class Mod:
    ''' Read Moddata from Blizzard TocFile, contains standard methods to return imformations like other Provider'''
    def __init__(self, shortname):
        self.TocFile = TocFile(shortname)
    def Name(self):
        return self.TocFile.ReadField('Title')
    def Description(self):
        return self.TocFile.ReadField('Notes')
    def Version(self):
        return self.TocFile.ReadField('Version')
    def ProjectUrl(self):
        return self.TocFile.ReadField('X-Website')
    def Url(self):
        return False
    def DownloadUrl(self):
        return False # not aviable this provider only provides data
    def DownloadUrlL(self):
        return False # same 
    def RequiredDepencies(self):
        __required_depencies__ = []
	# FIXME: replace with cleaner code
	# see: www.wowpedia.org/The_TOC_Format#Depencies
        try:
            __required_depencies__ = self.TocFile.ReadField('Require dDeps')
        except:
            try: 
                __required_depencies__ = self.TocFile.ReadField('Depencies')
            except:
                try:
                    __required_depencies__ = self.TocFile.ReadField('Deps')
                except:
                    return False

            return __required_depencies__
    
    def OptionalDepencies(self):
        return self.TocFile.ReadField('OptionalDeps')
    def Add():
        return False
    def Remove():
        return False

