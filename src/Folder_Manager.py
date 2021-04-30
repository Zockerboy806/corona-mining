import os
import shutil
from datetime import date

today = str(date.today())
todayPath = "C:/Corona Mining/data/" + today
os.chdir("C:/Corona Mining/data")
if os.path.isdir(todayPath):
   shutil.rmtree(todayPath)
os.mkdir(todayPath)