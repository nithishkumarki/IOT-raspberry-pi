import subprocess
from subprocess import call 

import os 
import glob 
import time 
import smtplib 
import base64 

from email.mine.image import MIMEImage 
from email.mine.multipart import MIMEMultipart

gmailuser="nithishkumarkt.22cse@kongu.edu"
gmailpassword="******"

From=""
To=[""]

while True:
    subprocess.Popen("raspistill -o image.jpg",shell=True)
    time.sleep(1)
    
    imageObj=MIMEImage()
    image['Subject']="this is subject content"
    
    fp=open("image.jpg","rb")
    img=MIMEImage(fp.read())
    
    imageObj.attach(img)
    
    try:
        server=smptlib.SMTP("smtp.gamil.com",587)
        server.starttls();
        server.login(gmailuser,gmailpassword)
        server.sendmail(Form,To,msg)
    except exception as e:
        print (e)
    
