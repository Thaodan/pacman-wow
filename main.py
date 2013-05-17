#!/usr/bin/python

'''
'''

#the very thing we are looking for
#
#                <p>If your download doesn't begin <a data-project="20695" data-file="652710" data-href="http://addons.curse.cursecdn.com/files/652/710/Bazooka-v2.2.1.zip" class="download-link" href="#">click here</a>.</p>



import sys
from urllib.request import urlopen,getproxies
from bs4 import BeautifulSoup
from ConfigParser import RawConfigParser as ConfigParser
import gettext



DEBUG=True

CRASH_CODE={
    128 :"do argue with me...",
    }



''' static config stuff '''

TEXTDOMAIN = "wow-pacman" 
TEXTDOMAINDIR = "/usr/share/local" 
CONFIG_FILE='siterip.cfg'

''' dynamic config stuff that will be moved to config file once implemented '''
CACHE_DIR = "pkg_cache"

''' example mod '''

SampleMode={
  "Name"        : "TestMod",
  "GShortname"  : "Test",
  "Description" : "A test Mod",
  "Contains"    : { "test", "Test" },
  "ProjectUrl"  :  "test.de",
  "ProviderURL" : "local/Test",
  "License"     : "BSD",
  "Hosters": {
    "Curse": {
      "Shortname": "Test",
    },
  }
}

def crash(code):
    '''
    This method accepts code argument,
    looks it up in CRASH_CODE
    prints the message and exits
    '''
    print(CRASH_CODE[code])
    sys.exit(code)

class Provider:
    class Curse:
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
    class Blizzard:
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
    class Modinfo:
        Name     = "Modinfo"
        Type     = "any"
        __self__ = Provider.Modinfo
        class Mod:
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
          

  #class Template:
    #'''
    #Template class 
    #'''
    #class Mod:
      #def Name(Url):
        #pass
      #def Description(Url):
        #pass
      #def Version():
        #pass
      #def ProjectUrl(Url):
        #return Tools.TocFile.ReadField('X-Website')
      #def Url(shortname):
        #return False
      #def DownloadUrl(Url):
        #return False # not aviable this provider only provides data
      #def DownloadUrlL(DownloadUrls):
        #return False # same 
      #def RequiredDepencies():
        #pass
      #def OptionalDepencies():
        #pass
      
          
          
class Tools:
  def __init__():
    pass
  def DownloadFiles(self.Files, self.TargetDirectory):
    '''
    download from list of urls
    '''
    #FIXME
    for url in self.Files:
      i = url.rfind('/')
      file = url[i+1:]
      urlopen(url, self.TargetDirectory/file)
    
  def GetHtmlPage(self.Url):
    try:
      return urlopen(self.Url)
    except:
      return False
  def Extract(Files, TargetDirectory):
      pass
  def GenMODINFO():
      pass
  class TocFile:
   '''
   NOTE: Needs changes according to: www.wowpedia.org/The_TOC_Format
   '''
   def ReadField(Field):
     pass
   def WriteField(Field, Data):
     try:
       pass
     except:
       return False
   def OpenFile():
     pass
  class Install:
      def __init__():
          pass
      def Mod(PaketAdresse):
          __mod_path__ = PaketAdresse[:1] 
          __mod_basename__ = PaketAdresse[:1]
          try:
              __mod_path__.Mod.get(__mod_basename__)
          except:
              print("Error while getting", PaketAdresse)
        # no Native MODINFO found try to gues by TocFile and gen local Modinfo
        #  try: 
        #      Tools.Extract(PaketAdresse,CACHE_DIR)
        #  except:
           #   print "error while extracting mod"
         ##     return False

          #if not exist PaketAdresse/.MODINFO:
           #   try:
            #      Tools.GenMODINFO(PaketAdresse/*.toc, PaketAdresse/.MODINFO)
             # except:
             #     print _("error while generating MODFILE for:")
              #    return False
         # try: 
          #    ConfigParser.read(PaketAdresse/.MODINFO)
           #   __install__ = ConfigParser.get('ModInfo', 'Install')
         # except:
         #     return False
        #  if __install__ == True:
         #     os.system(In
        # copy files to Chroot
        # run .install files
        
    def Provider():
        pass
      

def main():
  '''
  the main event :P
  '''
  config = ConfigParser.RawConfigParser()
  config.read(CONFIG_FILE)

  '''
  Get Remote and Local Data Provider
  '''
  Provider.Remote  =   config.get('Remote', 'Provider')
  Provider.Local   =   config.get('Local', 'Provider')
  if DEBUG:
    print Remote 
    print Local 
    
  if len(sys.argv) <= 1:
    crash(128)
  gettext.install(TEXTDOMAIN)
  ''' NOTE: add argument parser here '''
  ACTION = argv[1]
  SUBACTIONS = 3
  NON_ACTION_ARGS =  3

  if DEBUG:
    print args
    print len(args)
  if ACTION == SYNC:
    ActualProvider  = Provider.Remote
  elif ACTION == QUERRY or ACTION == Remove:
    ActualProvider  = Provider.Local
  if ActualProvider.Mod.Name(non_action_args):
      if ACTION == QUERRY or ACTION == SYNC:
          # parse subactions for sync and querry
          for current_sub_action in SUBACTIONS:
              if current_sub_action == LIST.SUMARY:
                  for actual_nonaction_arg in NON_ACTION_ARGS:
                      print _("Name"), ": ", ActualProvider.Mod.Name(actual_nonaction_arg)
                      print _("Description:"), ": ",ActualProvider.Mod.Description(actual_nonaction_arg)
                      print _("Version"), ": ",ActualProvider.Mod.Version(actual_nonaction_arg)
                      print _("URL"),": ",ActualProvider.Mod.ProjectUrl(actual_nonaction_arg)
                      print _("ProviderURL"),": ",ActualProvider.Mod.Url(non_action_arg)
                      print _("Depends on"),": ",ActualProvider.Mod.RequiredDepencies(non_action_arg)
                      print _("Optional Deps"),": ",ActualProvider.Mod.OptionalDepencies
              if current_sub_action == LIST.FILES:
                  for File in ActualProvider.Mod.Contents:
                      print File
              if current_sub_action == SEARCH.GROUPMEMBERS:
                  print ActualProvider.Querry.Groups.Name(NON_ACTION_ARGS)
                  ''' FIXME add search modifers'''   
              if current_sub_action == SEARCH.NAME:
                  # search for NON_ACTION_ARGS in ActualProvider.Mod.Name and print results
                  for search_name in ActualProvider.Mod.Name(NON_ACTION_ARGS):
                      print search_name
          
      if ACTION == SYNC:
          # parse subactions that are sync only
          for current_sub_action in SUBACTIONS:
              if current_sub_action == update_db:
                  Provider.Local.DB.Update(Provider.Remote.DB.Fetch)
          # download packages
          for non_action_arg  in NON_ACTION_ARGS:
              try:
                  __mod_basename__ = basename(non_action_arg)
                  Tools.DownloadFiles(Provider.Remote.Mod.DownloadUrlls(non_action_arg), CACHE_DIR/__mod_basename__)
                  __mod_basename__stack__.append(__mod_basename__)
              except:
                  print _("error while downloading:"), , non_action_arg
              
          for __mod_basename__ in __mod_basename__stack__:
              try:
                  Tools.Install.Mod(CACHE_DIR/__mod_basename__)
              except:
                  print 'error while installing'
                  return False

if __name__ == "__main__":
    main()

