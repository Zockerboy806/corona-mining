from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from datetime import date
import os

today = str(date.today())
gauth = GoogleAuth()
path = "/Corona Mining/data/" + today

gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

path = "/Corona Mining/data/" + today

for x in os.listdir(path):
    f = drive.CreateFile({'title': x})
    f.SetContentFile(os.path.join(path, x))
    f.Upload()
    f = None