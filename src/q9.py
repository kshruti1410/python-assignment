""" print file in a directory """
# pylint: disable=bad-indentation,anomalous-backslash-in-string, redefined-builtin
import os
DIRECTORY = "C:\Program Files\MySQL"
print(dir)
INDEX = 0
def dirtree(dir, index):
   """ reading the file which are present in the given directory """
   filenames = os.listdir(dir)
   for filename in filenames:
      if not os.path.isdir(os.path.abspath(dir+'/'+filename)):
         if filename == filenames[-1]:
            print('|   '*index+'\--', filename)
         else:
            print('|   '*index+'|--', filename)
      else:
         print('|   '*index+'|--', filename)
         dir = dir + '/' + filename
         dirtree(dir, index+1)

dirtree(DIRECTORY, INDEX)
