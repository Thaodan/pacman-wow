#!/usr/bin/python

'''
'''

#the very thing we are looking for
#
#                <p>If your download doesn't begin <a data-project="20695" data-file="652710" data-href="http://addons.curse.cursecdn.com/files/652/710/Bazooka-v2.2.1.zip" class="download-link" href="#">click here</a>.</p>



import sys
from os import environ
from urllib.request import urlopen,getproxies
from ConfigParser import RawConfigParser as ConfigParser
import gettext
import Provider


DEBUG=True

CRASH_CODE={
    128 :"do argue with me...",
    }



''' static config stuff '''

TEXTDOMAIN    = "wow-pacman" 
TEXTDOMAINDIR = "/usr/share/local"
CONFIG_DIR    = environ["XDG_CACHE_HOME"] + '/wpkg'
CONFIG_FILE   = CONFIG_DIR  + '/wpkg.cfg'

''' dynamic config stuff that will be moved to config file once implemented '''

CACHE_DIR     = environ["XDG_CACHE_HOME"] + "wpkg"
 
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
  
class TocFile:
    '''
    NOTE: Needs changes according to: www.wowpedia.org/The_TOC_Format
    '''
    def __init__(self, file):
        self.file = open(file)
        self.dict = {}
        __line__  = []
        for __line_raw__ in self.file:
            __match__ = re.search('^# ', line) # skip comments
            __match2__ = re.search('^##', line)  
            if not __match__ or __match2__:	
                __line_raw__ = line_raw.replace('## ', '') # we don't want the preceding '## '
                __line__ = __line_raw__.split()
                __line__[0] = __line__[0].replace(':', '')
                self.dict[__line__[0]] = __line__[1]
    def ReadField(self, Field):
        return self.dict[Field]
    def WriteField(self, Field, Data):
        pass

def DownloadFiles(self, Files, TargetDirectory):
    '''
    download from list of urls
    '''
    #FIXME
    for url in Files:
      i = url.rfind('/')
      file = url[i+1:]
      urlopen(url, TargetDirectory/file)
def GetHtmlPage(self, Url):
    try:
        return urlopen(Url)
    except:
        return False
def Extract(Files, TargetDirectory):
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
  Remote  =   config.get('Remote', 'Provider')
  Local   =   config.get('Local', 'Provider')
  if DEBUG:
    print(Remote) 
    print(Local)
                
  Provider.Remote = Provider.Modinfo(remote,"http://test.de/")
  
  #    print(_("Could import selected Providers, check config file"))
   #   sys.exit(1)
  Provider.Local  = Local  
  Provider.Remote = Remote
  if len(sys.argv) <= 1:
    crash(128)
  gettext.install(TEXTDOMAIN)
  ''' NOTE: add argument parser here '''
  ACTION = argv[1]
  SUBACTIONS = 3
  NON_ACTION_ARGS =  3

  if DEBUG:
    print (args)
    print (len(args)

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
                      ActualProvider=ActualProvider(actual_nonaction_arg)
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

