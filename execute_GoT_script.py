# A script that executes the 'GoT_noble_houses.rb' program.
#
# Examples:
#   Directory: Desktop/2to5.
#     1. From Repo: python execute_GoT_script.py
#     2. From Desktop: python 2to5/execute_GoT_script.py
#     3. Other folder on Desktop: python ../2to5/execute_GoT_script.py
#         => clones git repo inside this folder
#
# This opens the default browser with url 'http://gameofthrones.wikia.com/wiki/House_Stark'
import os

# Context Manager to change current directory.
class ChangeDir:
  def __init__(self, newPath):
    self.newPath = os.path.expanduser(newPath)
  def __enter__(self):
    self.savedPath = os.getcwd()
    os.chdir(self.newPath)
  def __exit__(self, etype, value, traceback):
    os.chdir(self.savedPath)

# Executes a ruby program if the file exists.
class Program:
  def run(self, file_name):
    if os.path.isfile(file_name):
      os.system("ruby %s Stark" %file_name)

# ====== Begin Execution =======
FILE_NAME = 'GoT_noble_houses.rb'

repo_link = 'https://github.com/SaurabhM21/2to5'
dir_name = repo_link[repo_link.rfind('/')+1:]
current_dir = os.getcwd()[os.getcwd().rfind('/')+1:]

# If cloned dir not present inside current dir or user not inside the cloned dir.
if not (os.path.exists(dir_name) or current_dir == dir_name):
  os.system("git clone %s" %repo_link)
  with ChangeDir(dir_name):
    Program().run(FILE_NAME)
# If executing from a level above the cloned dir.
elif os.path.exists(dir_name):
  with ChangeDir(dir_name):
    Program().run(FILE_NAME)
# If executing from the cloned dir.
elif current_dir == dir_name:
  Program().run(FILE_NAME)
else:
  print "Incorrect directory. Please search for %s" %dir_name
