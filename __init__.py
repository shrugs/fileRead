#!/usr/bin/python
# -*- coding: utf-8 -*-
# by MattCMultimedia

import random
from plugin import *
import os
import re

#change this to be to path to your text files including a final "/" 
#ex:  /siriservercore/plugins/fileRead/
#where all of my text files are in /fileRead/
#for example, yellow.txt is in /siriservercore/plugins/fileRead/yellow.txt
path_to_files = "/siriservercore/plugins/fileRead/"

class readFile(Plugin):

     
     #@register("en-US",".*change.*file [a-zA-Z0-9]+")
     @register("en-US",".*switch.*file")
     def switch_file(self, speech, language):
          
          #Asks Question and gets answer
          answer = self.ask('What would you like to change the file to?')
          filename = str(answer)
          
          filepath = path_to_files + filename + ".txt"
          
          if os.path.exists(filepath) == True:
               f = open(filepath, 'r')
          else:
               f = open(filepath, 'w')
               name_answer = self.ask('What would you like the file to say?')
               file_contents = str(name_answer)
               f.write(file_contents)
               self.say(filename + " now contains the phrase" + '"' + file_contents + '".')
               
               
          
          #Save answer to file to retrieve later
          path_store = open(path_to_files + 'path_store.txt', 'w')
          path_store.write(filepath)
          path_store.close()
          
          self.say ("Open file has been set to " + '"' + filename + '".')
          
          self.complete_request()
          
          
     #@register("en-US",".*content.*file.*")
     #@register("en-US",".*contents.*file.*")
     @register("en-US",".*read.*file")
     def read_file(self, speech, language):
          
          path_store = open(path_to_files + 'path_store.txt', 'r')
          file_link = str(path_store.read())
          path_store.close()
          file_to_be_read = open(file_link, 'r')
                    
          

          self.say (file_to_be_read.read())
          self.complete_request()

          
     @register('en-US',"(.*write.*to.*file)|(.*write.*file.*)|(.*writefile.*)|(.*right.*file.*)")
     def write_file(self, speech, language):
          path_store = open(path_to_files + 'path_store.txt', 'r')
          file_link = str(path_store.read())
          
          match = re.search('\w+\.txt', file_link)
          if match:
               filename = match.group()
          else:
               print "error"
          
          
          path_store.close()
          file_to_write = open(file_link, 'w')
          answer = self.ask("What do you want the file " + '"' +  filename  + '"' + " to say?")
          string_to_write = str(answer)
          file_to_write.write(string_to_write)
          file_to_write.close()
          self.say(filename + ' now contains ' + '"' + string_to_write + '".')
          self.complete_request()
          
     @register('en-US','.*check.*file')
     def check_file(self, speech, language):
          path_store = open(path_to_files + 'path_store.txt', 'r')
          
          file_link = str(path_store.read())
          
          match = re.search('\w+\.txt', file_link)
          if match:
               filename = match.group()
          else:
               print "error"
     
          self.say("The currently selected file is " +'"' + filename + '".')
          self.complete_request()
     
     
     @register('en-US','(new file.*)|(create new file.*)')
     def new_file(self, speech, language):
          answer = self.ask("What should the new file be called?")
          new_file_name = str(answer)
          
          filepath = path_to_files + new_file_name + ".txt"
          
          f = open(filepath, 'w')
          content_answer = self.ask('What would you like the file to say?')
          file_contents = str(content_answer)
          f.write(file_contents)
          self.say(new_file_name + " now contains the phrase" + '"' + file_contents + '".')
          
          self.complete_request()