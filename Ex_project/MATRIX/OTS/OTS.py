import time, os, sys, datetime, smtplib, imaplib, mailparser, requests, fileinput, psutil, re
from colorama                    import *
from email.mime.text             import *
from twilio.rest                 import Client
from email.message               import EmailMessage
from var                         import OPERATION, OVERWATCH, CHECKPOINTS, URL, timeT, timeC, mode
init()
################################################################################################################# OTS ######################################################################################################################
#                                                                                                          V A R I A B L E S
clear          = "\033[2J\033[1;1f"
now            = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
now            = str(now)
missedCount    = 0
c              = 0
regex          = re.compile(".*?\((.*?)\)")
test           = "0:03:00"
ONEhour        = "1:00:00"
TWOhours       = "2:00:00"
THREEhours     = "3:00:00"
FOURhours      = "4:00:00"
SIXhours       = "6:00:00"
REPORTTIME     = "reportTIME.txt"
REPORTCHECK    = "reportCHECK.txt"
timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
timerNOW       = datetime.datetime.now().strftime("%H:%M:%S, %m/%d/%Y")
timerNOW       = datetime.datetime.strptime(timerNOW, "%H:%M:%S, %m/%d/%Y")
DELTA          = timerNOW - timerSTART
last3check     = ["NEWSTART","NEWSTART","NEWSTART"]
# FPackage Password
Fpassword      = #import from MYPWS.txt
# ACCOUNT CREDS FOR TWILIO AND 41 EMAIL
ACCOUNT        = #import from MYPWS.txt
TOKEN          = #import from MYPWS.txt
client         = Client(ACCOUNT,TOKEN)
fromaddr       = #import from MYPWS.txt
pw             = #import from MYPWS.txt
sentto         = #import from MYPWS.txt
server         = smtplib.SMTP('smtp.gmail.com', 587) #throws an error if no internet connection
# OTS PARAMETER VARS
OTS            = True
runningT       = True
runningC       = True
nochecks       = True
CHECKMODE      = False
TIMEMODE       = False
pending        = False
ALPHA          = False
SWITCH         = False
LoggedIn       = False
Set            = False
Set1           = False
Set2           = False
Set3           = False
Set4           = False
Set5           = False
Set6           = False
SET            = False
run            = False
rise = """
                    X
                   XX
                  XXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXXX
                 XXX
                 XX
                 X

  
                XXXXX
              XXX  XXX
             XXX     X
              XXXX
              XXXXXX
          XXXXXXXXXXXXXXX"""
#No connection pic
noconnection ="""
       XXX               XXX
        XXX             XXX  
         XXX           XXX  
          XXX         XXX
           XXX       XXX
            XXX     XXX
             XXX   XXX
              XXX XXX
               XXXXX
               XXXXX
              XXX XXX
             XXX   XXX
            XXX     XXX
           XXX       XXX
          XXX         XXX
         XXX           XXX
        XXX             XXX
       XXX               XXX
  - N O    C O N N E C T I O N -"""
#Connection pic
connection ="""
                                VVV  
                               VVV  
                              VVV
                             VVV
                            VVV
                           VVV
                          VVV
                         VVV
        VVV             VVV
         VVV           VVV 
          VVV         VVV 
           VVV       VVV    
            VVV     VVV      
             VVV   VVV       
              VVVVVVV
               VVVVV
                VVV            
                 V

  -      C O N N E C T E D      -"""
################################################################################################################# OTS ######################################################################################################################
#                                                                                                          F U N C T I O N S
#define function to shortly flash the logo in the beginning of the program
def bling():
    print(Fore.RED + rise + Style.RESET_ALL)
    time.sleep(0.01)
    print(clear)
    time.sleep(0.02)
    print(Style.DIM + rise + Style.RESET_ALL)
    time.sleep(0.01)
    print(clear)
    time.sleep(0.01)

#defining internet connection checking function
def check_connection():
    url='http://www.google.com/'
    timeout=5
    checkloop = True
    while checkloop == True:
           try:
                  server     = smtplib.SMTP('smtp.gmail.com', 587)
                  _ = requests.get(url, timeout=timeout)
                  print(clear +  Fore.LIGHTGREEN_EX)
                  print(connection)
                  time.sleep(0.5)
                  print(""+Style.RESET_ALL)
                  print(clear)
                  checkloop = False
           except requests.ConnectionError:
                  print(clear + Fore.LIGHTRED_EX)
                  print(noconnection)
                  time.sleep(2)
                  print(""+Style.RESET_ALL)
                  print("ConnectionError.")
                  input("Enter to try again...")
           except smtplib.SMTPConnectError:
                  print(clear + Fore.LIGHTRED_EX)
                  print(noconnection)
                  time.sleep(2)
                  print(""+Style.RESET_ALL)
                  print("SMTPConnectError.")
                  input("Enter to try again...")

#defining email function to confirm check-ins to operator
def gmail_send(subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('41.notification@gmail.com', 'lopskxpqbjxlctpl')
    msg            = EmailMessage()
    message        = f'{message}\n'
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From']    = '41.notification@gmail.com'
    msg['To']      = 'markus.beyer10969@web.de'
    server.send_message(msg)

#defining check in collection function, recording last 3 check ins
def check_in():
    run = True
    while run == True:
        if M41.upper() == "M":
            del last3check[0]
            last3check.append("Mcheck")
        elif M41.upper() == "C":
            del last3check[0]
            last3check.append("Ccheck")

############################################################################################### P R O G R A M        S T A R T #############################################################################################################
check_connection()
while Set == False:
    while Set1 == False:
        print(clear)
        print("           CURRENT OPERATION: "+OPERATION)
        print("           CORRECT? (y/n)")
        CONF = input("           ---> ")
        if   CONF.upper() == "N":
            print(clear)
            print("""
           --  ENTER OPERATION NAME --
                                 """)
            choice = input("OPERATION ")
            print("")
            OPERATION = choice.upper()
            for line in fileinput.FileInput("var.py", inplace=1):
                if "OPERATION      = " in line:
                    line = line.replace(line, "OPERATION      = '"+str(OPERATION)+"'\n")
                print(line, end='')
            print(clear)
        elif CONF.upper() == "Y":
            Set1 = True
        else:
            continue
    while Set2 == False:
        print(clear)
        print("           CURRENT OVERWATCH: "+OVERWATCH)
        print("           CORRECT? (y/n)")
        CONF = input("           ---> ")
        if   CONF.upper() == "N":
            print(clear)
            print("""
           -- ENTER OVERWATCH PHONE --
                                 """)
            choice = input("OVERWATCH PHONE NR : ")
            print("")
            OVERWATCH = choice.upper()
            for line in fileinput.FileInput("var.py", inplace=1):
                if "OVERWATCH      = " in line:
                    line = line.replace(line, "OVERWATCH      = '"+str(OVERWATCH)+"'\n")
                print(line, end='')
            print(clear)
        elif CONF.upper() == "Y":
            Set2 = True
        else:
            continue
    if "ngrok.exe" in (p.name() for p in psutil.process_iter()):
        print(Fore.GREEN+"NGROK ALREADY RUNNING"+Style.RESET_ALL)
        time.sleep(0.5)
    else:
        os.startfile("NGROK.lnk")
    while Set3 == False:
        print(clear)
        print("           CURRENT NGROK URL: "+URL)
        print("           CORRECT? (y/n)")
        CONF = input("           ---> ")
        if   CONF.upper() == "N":
            print(clear)
            print("""
           --    ENTER NGROK URL   --
                                 """)
            choice = input("           http://")
            print("")
            URL = "http://"+choice
            for line in fileinput.FileInput("var.py", inplace=1):
                if "URL            = " in line:
                    line = line.replace(line, "URL            = '"+str(URL)+"'\n")
                print(line, end='')
            print(clear)
        elif CONF.upper() == "Y":
            Set3 = True
        else:
            continue
    while Set4 == False:
        print(clear)
        if   timeT == FOURhours:
            x = "4h"
        elif timeT == THREEhours:
            x = "3h"
        elif timeT == TWOhours:
            x = "2h"
        elif timeT == ONEhour:
            x = "1h"
        elif timeT == test:
            x = "3min (test)"
        print("           CURRENT TIME T: "+x)
        print("           CORRECT? (y/n)")
        CONF = input("           ---> ")
        if   CONF.upper() == "N":
            print(clear)
            print("""
           -- CHOOSE T TIME WINDOW  --
                    (1) 1h
                    (2) 2h
                    (3) 3h
                    (4) 4h
                    (T) 3 minutes (test)

                       """)
            choice = input("")
            if   choice == "1":
                timeT = '1:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeT          = " in line:
                        line = line.replace(line, "timeT          = '"+str(timeT)+"'\n")
                    print(line, end='')
            elif choice == "2":
                timeT = '2:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeT          = " in line:
                        line = line.replace(line, "timeT          = '"+str(timeT)+"'\n")
                    print(line, end='')
            elif choice == "3":
                timeT = '3:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeT          = " in line:
                        line = line.replace(line, "timeT          = '"+str(timeT)+"'\n")
                    print(line, end='')
            elif choice == "4":
                timeT = '4:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeT          = " in line:
                        line = line.replace(line, "timeT          = '"+str(timeT)+"'\n")
                    print(line, end='')
            elif choice.upper() == "T":
                timeT = '0:03:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeT          = " in line:
                        line = line.replace(line, "timeT          = '"+str(timeT)+"'\n")
                    print(line, end='')
            print(clear)
        elif CONF.upper() == "Y":
            Set4 = True
            break #why is this necessary????
        else:
            continue
    while Set5 == False:
        print(clear)
        if   timeC == FOURhours:
            x = "4h"
        elif timeC == THREEhours:
            x = "3h"
        elif timeC == TWOhours:
            x = "2h"
        elif timeC == ONEhour:
            x = "1h"
        elif timeC == test:
            x = "3min (test)"
        print("           CURRENT TIME C: "+x)
        print("           CORRECT? (y/n)")
        CONF = input("           ---> ")
        if   CONF.upper() == "N":
            print(clear)
            print("""
           -- CHOOSE C TIME WINDOW  --
                    (1) 1h
                    (2) 2h
                    (3) 3h
                    (4) 4h
                    (T) 3 minutes (test)

                       """)
            choice = input("")
            if   choice == "1":
                timeC = '1:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeC          = " in line:
                        line = line.replace(line, "timeC          = '"+str(timeC)+"'\n")
                    print(line, end='')
            elif choice == "2":
                timeC = '2:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeC          = " in line:
                        line = line.replace(line, "timeC          = '"+str(timeC)+"'\n")
                    print(line, end='')
            elif choice == "3":
                timeC = '3:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeC          = " in line:
                        line = line.replace(line, "timeC          = '"+str(timeC)+"'\n")
                    print(line, end='')
            elif choice == "4":
                timeC = '4:00:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeC          = " in line:
                        line = line.replace(line, "timeC          = '"+str(timeC)+"'\n")
                    print(line, end='')
            elif choice.upper() == "T":
                timeC = '0:03:00'
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "timeC          = " in line:
                        line = line.replace(line, "timeC          = '"+str(timeC)+"'\n")
                    print(line, end='')
            print(clear)
        elif CONF.upper() == "Y":
            Set5 = True
            break #why is this necessary????
        else:
            continue
    while Set6 == False:
        print(clear)
        x = mode
        print("           CURRENT MODE: "+x)
        print("           CORRECT? (y/n)")
        CONF = input("           ---> ")
        if   CONF.upper() == "N":
            print(clear)
            print("""               --
           --    CHOOSE OTS MODE    --
                    (1) HOT
                    (2) TEST
                       """)
            choice = input("")
            if   choice == "1":
                mode = "HOT"
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "mode           = " in line:
                        line = line.replace(line, "mode           = '"+str("HOT")+"'\n")
                    print(line, end='')
                MODE = Fore.LIGHTRED_EX+"                    HOT HOT HOT"+Style.RESET_ALL
            elif choice == "2":
                mode = "TEST"
                for line in fileinput.FileInput("var.py", inplace=1):
                    if "mode           = " in line:
                        line = line.replace(line, "mode           = '"+str("TEST")+"'\n")
                    print(line, end='')
                MODE = Fore.GREEN      +"                    TEST TEST TEST"+Style.RESET_ALL
            print(clear)
        elif CONF.upper() == "Y":
            if mode == "HOT":
                MODE = Fore.LIGHTRED_EX+"                    HOT HOT HOT"+Style.RESET_ALL
            elif mode == "TEST":
                MODE = Fore.GREEN      +"                    TEST TEST TEST"+Style.RESET_ALL
            Set6 = True
            break #why is this necessary? is it?
        else:
            continue
    SET = False
    while SET == False:
        print(clear)
        if   timeT == "4:00:00":
            timeT = datetime.timedelta(hours=4)
            TTT   = "4 hours"
        elif timeT == "3:00:00":
            timeT = datetime.timedelta(hours=3)
            TTT = "3 hours"
        elif timeT == "2:00:00":
            timeT = datetime.timedelta(hours=2)
            TTT = "2 hours"
        elif timeT == "1:00:00":
            timeT = datetime.timedelta(hours=1)
            TTT = "1 hour"
        elif timeT == "0:03:00":
            timeT = datetime.timedelta(minutes=3)
            TTT = "3 minutes (test)"
        if   timeC == "4:00:00":
            timeC = datetime.timedelta(hours=4)
            CCC = "4 hours"
        elif timeC == "3:00:00":
            timeC = datetime.timedelta(hours=3)
            CCC = "3 hours"
        elif timeC == "2:00:00":
            timeC = datetime.timedelta(hours=2)
            CCC = "2 hours"
        elif timeC == "1:00:00":
            timeC = datetime.timedelta(hours=1)
            CCC = "1 hour"
        elif timeC == "0:03:00":
            timeC = datetime.timedelta(minutes=3)
            CCC = "3 minutes (test)"
        print("""

  Operative Travel Security System
  --      current settings      --

      OPERATION """+Fore.LIGHTGREEN_EX+OPERATION+Style.RESET_ALL+          """
   OVERWATCH     = """+Fore.LIGHTGREEN_EX+str(OVERWATCH)+Style.RESET_ALL+  """
   NGROK URL     = """+Fore.LIGHTGREEN_EX+str(URL)+Style.RESET_ALL+        """
   T TIME WINDOW = """+Fore.LIGHTGREEN_EX+str(TTT)+Style.RESET_ALL+        """
   C TIME WINDOW = """+Fore.LIGHTGREEN_EX+str(CCC)+Style.RESET_ALL+        """
   MODE          = """+                   mode                    +        """


        (1) START OTS | RERUN SETTINGS (2)"""+Style.RESET_ALL)
        CONF = input("           ---> ")
        if   CONF.upper() == "1":
            print(clear)
            print("")
            SET = True
            Set = True
        elif CONF.upper() == "2":
            Set  = False
            Set1 = False
            Set2 = False
            Set3 = False
            Set4 = False
            Set5 = False
            SET  = True
            break #why is this necessary????
        else:
            continue

#Set Mode Part 1
if mode == "HOT":
    COPS   = "+4930110"      #Police Germany
    FOROFF = "+493018172000" #Foreign Office Germany
elif mode == "TEST":
    COPS   = "+4917624806086" #my phone
    FOROFF = "+4917624806086" #my phone 

#Set Mode Part 2
while run == False:
        print(clear)
        print("""
           [1] TIMEMODE   |   CHECKMODE [2]
                                 """)
        choice = input("           ---> ")
        if choice == "1":
                TIMEMODE  = True
                run       = True
        elif choice == "2":
                CHECKMODE = True
                run       = True
        else:
                print(Fore.LIGHTRED_EX+"INVALID"+Style.RESET_ALL)
                time.sleep(1)

#do bling() with max of 7 times
run = True
while run == True:
    bling()
    c += 1
    if c == 7:
        run = False
# OTS
while OTS == True:
    if TIMEMODE == True:################################################################################################################################################################################################# TIMEMODE
        timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
        timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
        runningT = True
        while runningT == True:
            print(clear)
            now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
            now = str(now)
            print("           >--- "+Fore.LIGHTRED_EX+"O"+Fore.RED+"perative "+Fore.LIGHTRED_EX+"T"+Fore.RED+"ravel "+Fore.LIGHTRED_EX+"S"+Fore.RED+"ecurity System "+Style.RESET_ALL+"---< ("+Style.BRIGHT+"5.0"+Style.RESET_ALL+")"+Fore.RED)
            print("                    OPERATION "+Fore.LIGHTRED_EX+OPERATION.upper()+Style.RESET_ALL)
            print(MODE)
            print("                    "+now)
            print("                    TIME MODE ("+TTT+")")
            if   ALPHA == True:
                    print(Fore.LIGHTYELLOW_EX+"                    ALPHA ALPHA ALPHA"+Style.RESET_ALL)
            elif ALPHA == False:
                    print("")
            timerNOW     = datetime.datetime.now().strftime("%H:%M:%S, %m/%d/%Y")
            timerNOW     = datetime.datetime.strptime(timerNOW, "%H:%M:%S, %m/%d/%Y")
            DELTA        = timerNOW - timerSTART
            if   TTT == "4 hours":
                if DELTA.seconds >= 10800 and DELTA.seconds < 14400:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 14400:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            elif TTT == "3 hours":
                if DELTA.seconds >= 7200 and DELTA.seconds < 10800:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 10800:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            elif TTT == "2 hours":
                if DELTA.seconds >= 5400 and DELTA.seconds < 7200:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 7200:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            elif TTT == "1 hour":
                if DELTA.seconds >= 2700 and DELTA.seconds < 3600:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 3600:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            elif TTT == "3 minutes (test)":
                if DELTA.seconds >= 120 and DELTA.seconds < 180:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 180:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
            now = str(now)
            if os.path.exists(REPORTTIME) == False:
                report = open(REPORTTIME, 'w')
                report.write(now + " TIME STARTED!")
                report.close()
            if DELTA < timeT:
                emails   = True
                messages = True
                REACHED  = False
                LoggedIn = False
                while LoggedIn == False:
                    now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
                    now = str(now)
                    try:
                        mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
                        mail.login(fromaddr, pw)
                        LoggedIn = True
                    except (imaplib.IMAP4.error, imaplib.IMAP4.abort,ConnectionResetError):
                        print(Fore.LIGHTRED_EX + "LOGIN FAILED" + Style.RESET_ALL)
                        if os.path.exists("ERRORLOG.txt") == False:
                                report = open("ERRORLOG.txt", 'w')
                                report.write(now + " LOGINERROR")
                                report.close()
                        elif os.path.exists("ERRORLOG.txt") == True:
                                report = open("ERRORLOG.txt", 'a')
                                report.write("\n" + now + " LOGINERROR")
                                report.close()
                listloop = True
                while listloop == True:
                    try:
                        mail.list()
                        mail.select("inbox")
                        listloop = False
                    except:
                        print("ERROR (mail.list)")
                result, data   = mail.search(None, 'SUBJECT "[OTS]"')
                result2, data2 = mail.search(None, 'FROM "noreply@findmespot.com"')
                ids  = data[0]
                ids2 = data2[0]
                id_list  = ids.split()
                id_list += ids2.split()
                try:
                        latest_email_id = id_list[-1]
                        messages = True
                except IndexError:
                        now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
                        now = str(now)
                        print(clear)
                        print("           >--- "+Fore.LIGHTRED_EX+"O"+Fore.RED+"perative "+Fore.LIGHTRED_EX+"T"+Fore.RED+"ravel "+Fore.LIGHTRED_EX+"S"+Fore.RED+"ecurity System "+Style.RESET_ALL+"---< ("+Style.BRIGHT+"5.0"+Style.RESET_ALL+")"+Fore.RED)
                        print("                    OPERATION "+Fore.LIGHTRED_EX+OPERATION.upper()+Style.RESET_ALL)
                        print()
                        print("                    "+now)
                        print("                    TIME MODE")
                        print()
                        messages     = False
                        timerNOW     = datetime.datetime.now().strftime("%H:%M:%S, %m/%d/%Y")
                        timerNOW     = datetime.datetime.strptime(timerNOW, "%H:%M:%S, %m/%d/%Y")
                        DELTA        = timerNOW - timerSTART
                        if   TTT == "4 hours":
                                if DELTA.seconds >= 10800 and DELTA.seconds < 14400:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 14400:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        elif TTT == "3 hours":
                                if DELTA.seconds >= 7200 and DELTA.seconds < 10800:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 10800:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        elif TTT == "2 hours":
                                if DELTA.seconds >= 5400 and DELTA.seconds < 7200:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 7200:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        elif TTT == "1 hour":
                                if DELTA.seconds >= 2700 and DELTA.seconds < 3600:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 3600:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        elif TTT == "3 minutes (test)":
                                if DELTA.seconds >= 120 and DELTA.seconds < 180:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 180:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        print("Waiting for Check-In (" + str(missedCount) + " missed)")
                        time.sleep(1)
                if messages == True:
                    def empty_folder(m, do_expunge=True):
                        print(Fore.LIGHTGREEN_EX + "CHECKED IN! " + Style.RESET_ALL + Fore.GREEN + now + Style.RESET_ALL)
                        REACHED = True  #############################################################################################################
                        m.select("inbox")  # select all trash
                        m.store("1:*", '+FLAGS', '\\Deleted')  # Flag all Trash as Deleted
                        if do_expunge:  # See Gmail Settings -> Forwarding and POP/IMAP -> Auto-Expunge
                            m.expunge()  # not need if auto-expunge enabled
                        else:
                            print("Expunge was skipped.")
                            return
                    result, data = mail.fetch(latest_email_id, "RFC822")
                    m = mailparser.parse_from_bytes(data[0][1])
                    text = "From: "  # the Signature of emails sent by my phone. After that, anything is irrelevant
                    entry = m.body.split(text, 1)[0]
                    message = str(entry.upper())
                    empty_folder(mail)
                    now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
                    now = str(now)
                    if "CHECK" in message:
                            timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
                            timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
                            if ALPHA == True:
                                ALPHA = False
                                if "(" in message and ")" in message:
                                    coordinates = re.findall(regex,message)
                                    coordinates = str(coordinates)
                                else:
                                    coordinates = "[no coordinates]"
                                check = "Alpha End("+now+" "+coordinates+")"
                                del last3check[0]
                                last3check.append(check)
                                gmail_send("CONFIRMATION","ALPHA END. "+str(last3check)+" -41")
                            elif ALPHA == False:
                                if "(" in message and ")" in message:
                                    coordinates = re.findall(regex,message)
                                    coordinates = str(coordinates)
                                else:
                                    coordinates = "[no coordinates]"
                                check = "Check In("+now+" "+coordinates+")"
                                del last3check[0]
                                last3check.append(check)
                                gmail_send("CONFIRMATION","CHECK IN CONFIRMED. "+str(last3check)+" -41") 
                            if os.path.exists(REPORTTIME) == False:
                                    report = open(REPORTTIME, 'w')
                                    report.write(now + " CHECKED IN! "+coordinates)
                                    report.close()
                            elif os.path.exists(REPORTTIME) == True:
                                    report = open(REPORTTIME, 'a')
                                    report.write("\n" + now + " CHECKED IN! "+coordinates)
                                    report.close()
                            missedCount = 0
                    elif "FLIGHT" in message:  # Flight Mode
                        print(now + Fore.LIGHTRED_EX + " FLIGHT MODE ACTIVATED." + Style.RESET_ALL)
                        if "(" in message and ")" in message:
                            coordinates = re.findall(regex,message)
                            coordinates = str(coordinates)
                        else:
                            coordinates = "[no coordinates]"
                        check = "Flight Start("+now+" "+coordinates+")"
                        del last3check[0]
                        last3check.append(check)
                        gmail_send("CONFIRMATION","FLIGHT MODE ACTIVATED. "+str(last3check)+" -41")
                        time.sleep(0.1)
                        message = client.messages.create(
                                to     = OVERWATCH,
                                from_  = "+447480781141",
                                body   = "OVERWATCH. Your Operator just activated Flight Mode.   -41"
                                )
                        if os.path.exists(REPORTTIME) == False:
                                report = open(REPORTTIME, 'w')
                                report.write(now + " FLIGHT MODE ACTIVATED")
                                report.close()
                        elif os.path.exists(REPORTTIME) == True:
                                report = open(REPORTTIME, 'a')
                                report.write("\n" + now + " FLIGHT MODE ACTIVATED")
                                report.close()
                        empty_folder(mail)
                        pending = True
                        while pending == True:
                                now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
                                now = str(now)
                                print(clear)
                                print(Fore.LIGHTRED_EX+"               !!!-            FLIGHT  MODE          -!!!"+Style.RESET_ALL)
                                print(Fore.YELLOW     +"               Pending for arrival message from Operator..."+Style.RESET_ALL)
                                LoggedIn = False
                                while LoggedIn == False:
                                    now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
                                    now = str(now)
                                    try:
                                        mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
                                        mail.login(fromaddr, pw)
                                        LoggedIn = True
                                    except (imaplib.IMAP4.error, imaplib.IMAP4.abort):
                                        print("LOGIN FAILED")
                                        if os.path.exists("ERRORLOG.txt") == False:
                                            report = open("ERRORLOG.txt", 'w')
                                            report.write(now + " LOGINERROR")
                                            report.close()
                                        elif os.path.exists("ERRORLOG.txt") == True:
                                            report = open("ERRORLOG.txt", 'a')
                                            report.write("\n" + now + " LOGINERROR")
                                            report.close()
                                listloop = True
                                while listloop == True:
                                    try:
                                        mail.list()
                                        mail.select("inbox")
                                        listloop = False
                                    except:
                                        print("ERROR (mail.list)")
                                result, data   = mail.search(None, 'SUBJECT "[OTS]"')
                                result2, data2 = mail.search(None, 'FROM "noreply@findmespot.com"')
                                ids  = data[0]
                                ids2 = data2[0]
                                id_list  = ids.split()
                                id_list += ids2.split()
                                noemails = True
                                try:
                                        latest_email_id = id_list[-1]
                                        noemails = False
                                except IndexError:
                                        print()
                                        print("               WAITING FOR CONFIRMATION SINCE " + str(timerNOW))
                                        noemails = True
                                        time.sleep(1)
                                        print(clear)
                                if noemails == False:
                                        def empty_folder(m, do_expunge=True):
                                                print(Fore.LIGHTGREEN_EX + "CHECKED IN! " + Style.RESET_ALL + Fore.GREEN + now + Style.RESET_ALL)
                                                m.select("inbox")  # select all trash
                                                m.store("1:*", '+FLAGS', '\\Deleted')  # Flag all Trash as Deleted
                                                if do_expunge:  # See Gmail Settings -> Forwarding and POP/IMAP -> Auto-Expunge
                                                        m.expunge()  # not need if auto-expunge enabled
                                                else:
                                                        print("Expunge was skipped.")
                                                        return
                                        result, data = mail.fetch(latest_email_id,"RFC822")
                                        m = mailparser.parse_from_bytes(data[0][1])
                                        text = "From: " #the Signature of emails sent by my phone. After that, anything is irrelevant
                                        entry = m.body.split(text, 1)[0]
                                        message = entry.upper()
                                        empty_folder(mail)
                                        if "CHECK" in message:
                                                if "(" in message and ")" in message:
                                                    coordinates = re.findall(regex,message)
                                                    coordinates = str(coordinates)
                                                else:
                                                    coordinates = "[no coordinates]"
                                                check = "Flight End("+now+" "+coordinates+")"
                                                del last3check[0]
                                                last3check.append(check)
                                                gmail_send("CONFIRMATION","FLIGHT MODE ENDED. "+str(last3check)+" -41")
                                                if os.path.exists(REPORTTIME) == False:
                                                        report = open(REPORTTIME, 'w')
                                                        report.write(now + " FLIGHT MODE ENDED.")
                                                        report.close()
                                                elif os.path.exists(REPORTTIME) == True:
                                                        report = open(REPORTTIME, 'a')
                                                        report.write("\n" + now + " FLIGHT MODE ENDED.")
                                                        report.close()
                                                        empty_folder(mail)
                                                message = client.messages.create(
                                                to     = OVERWATCH,
                                                from_  = "+447480781141",
                                                body   = "OVERWATCH. Your Operator just ended Flight Mode.   -41"
                                                )
                                                timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
                                                timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
                                                pending = False
                                        else:
                                                print(Fore.LIGHTRED_EX + "FLIGHT MODE ENDING FAILED" + Style.RESET_ALL)
                                                if os.path.exists("ERRORLOG.txt") == False:
                                                    report = open("ERRORLOG.txt", 'w')
                                                    report.write(now + " F-INIT ERROR")
                                                    report.close()
                                                elif os.path.exists("ERRORLOG.txt") == True:
                                                    report = open("ERRORLOG.txt", 'a')
                                                    report.write("\n" + now + " F-INIT ERROR")
                                                    report.close()
                    elif "ALPHA" in message:
                        ALPHA = True
                        try:
                                requests.get("http://127.0.0.1:8000/shutdown")
                        except requests.exceptions.ConnectionError:
                                pass
                        os.startfile("protocols\\ALPHA.lnk")
                        time.sleep(1)
                        call = client.calls.create(
                                to= OVERWATCH,
                                from_="+447480781141",
                                url=URL,
                                method='GET'
                                )
                        message = client.messages.create(
                                to     = OVERWATCH,
                                from_  = "+447480781141",
                                body   = "Good day sir. Your Operator just used the ALPHA command, something seems to be indicating danger. Be ready.  -41"
                                )
                        #DONE
                        if os.path.exists(REPORTTIME) == False:
                                report = open(REPORTTIME, 'w')
                                report.write(now + " ALPHA COMMAND RECEIVED")
                                report.close()
                        elif os.path.exists(REPORTTIME) == True:
                                report = open(REPORTTIME, 'a')
                                report.write("\n" + now + " ALPHA COMMAND RECEIVED")
                                report.close()
                                empty_folder(mail)
                        missedCount = 0
                        if "(" in message and ")" in message:
                            coordinates = re.findall(regex,message)
                            coordinates = str(coordinates)
                        else:
                            coordinates = "[no coordinates]"
                        check = "Alpha Start("+now+" "+coordinates+")"
                        del last3check[0]
                        last3check.append(check)
                        gmail_send("CONFIRMATION","ALPHA CONFIRMED. "+str(last3check)+" -41")
                    elif "HOTEL" in message or "INITIALIZE" in message:  # [!]  F - PROTOCOL  [!]
                        print(now + Fore.LIGHTRED_EX + " F-PROTOCOL REQUESTED!" + Style.RESET_ALL)
                        if "(" in message and ")" in message:
                            coordinates = re.findall(regex,message)
                            coordinates = str(coordinates)
                        else:
                            coordinates = "[no coordinates]"
                        check = "F-Protocol Request("+now+" "+coordinates+")"
                        del last3check[0]
                        last3check.append(check)
                        time.sleep(0.1)
                        if os.path.exists(REPORTTIME) == False:
                                report = open(REPORTTIME, 'w')
                                report.write(now + " HOTEL COMMAND RECEIVED")
                                report.close()
                        elif os.path.exists(REPORTTIME) == True:
                                report = open(REPORTTIME, 'a')
                                report.write("\n" + now + " HOTEL COMMAND RECEIVED")
                                report.close()
                                empty_folder(mail)
                        pending = True
                        try:
                                requests.get("http://127.0.0.1:8000/shutdown")
                        except requests.exceptions.ConnectionError:
                                pass
                        os.startfile("protocols\\HOTEL.lnk")
                        time.sleep(1)
                        call = client.calls.create(
                                to= OVERWATCH,
                                from_="+447480781141",
                                url=URL,
                                method='GET'
                                )
                        message = client.messages.create(
                                to     = OVERWATCH,
                                from_  = "+447480781141",
                                body   = "Attention. The F-Protocol has been requested. You being the Overwatch have to decide wether to initiate or to abort. Be aware that once confirmed, the Protocol can not be stopped and authorities will be contacted. Your choice Sir.   -41"
                                )
                        if os.path.exists(REPORTTIME) == False:
                                report = open(REPORTTIME, 'w')
                                report.write(now + " F-PROTOCOL REQUESTED!")
                                report.close()
                        elif os.path.exists(REPORTTIME) == True:
                                report = open(REPORTTIME, 'a')
                                report.write("\n" + now + " F-PROTOCOL REQUESTED!")
                                report.close()
                        empty_folder(mail)
                        while pending == True:
                                now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
                                now = str(now)
                                print(clear)
                                print(Fore.LIGHTRED_EX+"               !!!-       F-PROTOCOL INITIATED       -!!!"+Style.RESET_ALL)
                                print(Fore.YELLOW     +"               Pending for confirmation from Overwatch..."+Style.RESET_ALL)
                                LoggedIn = False
                                while LoggedIn == False:
                                    now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
                                    now = str(now)
                                    try:
                                        mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
                                        mail.login(fromaddr, pw)
                                        LoggedIn = True
                                    except (imaplib.IMAP4.error, imaplib.IMAP4.abort):
                                        print("LOGIN FAILED")
                                        if os.path.exists("ERRORLOG.txt") == False:
                                            report = open("ERRORLOG.txt", 'w')
                                            report.write(now + " LOGINERROR")
                                            report.close()
                                        elif os.path.exists("ERRORLOG.txt") == True:
                                            report = open("ERRORLOG.txt", 'a')
                                            report.write("\n" + now + " LOGINERROR")
                                            report.close()
                                listloop = True
                                while listloop == True:
                                    try:
                                        mail.list()
                                        mail.select("inbox")
                                        listloop = False
                                    except:
                                        print("ERROR (mail.list)")
                                result, data   = mail.search(None, 'SUBJECT "[OTS]"')
                                result2, data2 = mail.search(None, 'FROM "noreply@findmespot.com"')
                                ids  = data[0]
                                ids2 = data2[0]
                                id_list  = ids.split()
                                id_list += ids2.split()
                                noemails = True
                                try:
                                        latest_email_id = id_list[-1]
                                        noemails = False
                                except IndexError:
                                        print()
                                        print("               WAITING FOR CONFIRMATION SINCE " + str(timerNOW))
                                        noemails = True
                                        time.sleep(1)
                                        print(clear)
                                if noemails == False:
                                        def empty_folder(m, do_expunge=True):
                                                print(Fore.LIGHTGREEN_EX + "CHECKED IN! " + Style.RESET_ALL + Fore.GREEN + now + Style.RESET_ALL)
                                                m.select("inbox")  # select all trash
                                                m.store("1:*", '+FLAGS', '\\Deleted')  # Flag all Trash as Deleted
                                                if do_expunge:  # See Gmail Settings -> Forwarding and POP/IMAP -> Auto-Expunge
                                                        m.expunge()  # not need if auto-expunge enabled
                                                else:
                                                        print("Expunge was skipped.")
                                                        return
                                        result, data = mail.fetch(latest_email_id,"RFC822")
                                        m = mailparser.parse_from_bytes(data[0][1])
                                        text = "From: " #the Signature of emails sent by my phone. After that, anything is irrelevant
                                        entry = m.body.split(text, 1)[0]
                                        message = entry.upper()
                                        empty_folder(mail)
                                        if "ABORT" in message or "CHECK" in message:
                                                if "(" in message and ")" in message:
                                                    coordinates = re.findall(regex,message)
                                                    coordinates = str(coordinates)
                                                else:
                                                    coordinates = "[no coordinates]"
                                                check = "F-Protocol Abort ("+now+")"
                                                del last3check[0]
                                                last3check.append(check)
                                                gmail_send("ATTENTION","F-PROTOCOL REQUEST ABORTED. "+str(last3check)+" -41")
                                                if os.path.exists(REPORTTIME) == False:
                                                        report = open(REPORTTIME, 'w')
                                                        report.write(now + " F-PROTOCOL ABORTED.")
                                                        report.close()
                                                elif os.path.exists(REPORTTIME) == True:
                                                        report = open(REPORTTIME, 'a')
                                                        report.write("\n" + now + " F-PROTOCOL ABORTED.")
                                                        report.close()
                                                        empty_folder(mail)
                                                timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
                                                timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
                                                pending = False
                                        elif "CONFIRM" in message:#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!
                                                print(clear)#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!
                                                print("Initiating F-Protocol...")#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!    C A L L I N G      A U T H O R I T I E S   ! ! !      #!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#
                                                try:#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!
                                                        requests.get("http://127.0.0.1:8000/shutdown")#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!
                                                except requests.exceptions.ConnectionError:
                                                        pass
                                                check = "F-Protocol Confirm("+now+")"
                                                del last3check[0]
                                                last3check.append(check)
                                                os.startfile("protocols\\FOXTROT.lnk")
                                                time.sleep(1)
                                                call = client.calls.create(
                                                        to=COPS, 
                                                        from_="+447480781141",
                                                        url=URL,
                                                        method='GET'
                                                        )
                                                call = client.calls.create(
                                                        to=FOROFF, 
                                                        from_="+447480781141",
                                                        url=URL,
                                                        method='GET'
                                                        )
                                                #INFORM OVERWATCH
                                                message = client.messages.create(
                                                        to     = OVERWATCH,
                                                        from_  = "+447480781141",
                                                        body   = """Overwatch. The F-Protocol has been activated. \nBe aware, that authorities are being called and briefed at this moment, leading them to you for further Details. Give them the F-Package. It's everything we have: Planned Route, Subject Files, OTS Reports, Operation Documents. The Password is """+Fpassword+""". All together.  -41 """
                                                        )
                                                if os.path.exists(REPORTTIME) == False:
                                                        report = open(REPORTTIME, 'w')
                                                        report.write(now + " F-PROTOCOL CONFIRMED!!!")
                                                        report.close()
                                                elif os.path.exists(REPORTTIME) == True:
                                                        report = open(REPORTTIME, 'a')
                                                        report.write("\n" + now + " F-PROTOCOL CONFIRMED!!!")
                                                        report.close()
                                                        empty_folder(mail)
                                                pending = False
                                                endless = True
                                                while endless == True:
                                                    print(clear)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                    time.sleep(1)
                                                    print(clear)
                                                    print("")
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print("")
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print("")
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print("")
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print("")
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print("")
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print("")
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print("")
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print("")
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print("")
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print("")
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print("")
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print("")
                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                    print("")
                                                    time.sleep(1)############################################################################################################################################################# E  N  D  !!!
                                        else:
                                                print(Fore.LIGHTRED_EX + "F-PROTOCOL INITIALIZATION FAILED" + Style.RESET_ALL)
                                                if os.path.exists("ERRORLOG.txt") == False:
                                                    report = open("ERRORLOG.txt", 'w')
                                                    report.write(now + " F-INIT ERROR")
                                                    report.close()
                                                elif os.path.exists("ERRORLOG.txt") == True:
                                                    report = open("ERRORLOG.txt", 'a')
                                                    report.write("\n" + now + " F-INIT ERROR")
                                                    report.close()
                    elif "SWITCH" in message:
                            print("SWITCHING MODES")
                            time.sleep(1)
                            missedCount = 0
                            if os.path.exists(REPORTTIME) == False:
                                    report = open(REPORTTIME, 'w')
                                    report.write(now + " SWITCHING MODES")
                                    report.close()
                            elif os.path.exists(REPORTTIME) == True:
                                    report = open(REPORTTIME, 'a')
                                    report.write("\n" + now + " SWITCHING MODES")
                                    report.close()
                                    empty_folder(mail)
                            message = client.messages.create(
                                    to     = OVERWATCH,
                                    from_  = "+447480781141",
                                    body   = "Greetings Sir. OTS switched to Checkpoint-Mode. - 41"
                                    )
                            if "(" in message and ")" in message:
                                coordinates = re.findall(regex,message)
                                coordinates = str(coordinates)
                            else:
                                coordinates = "[no coordinates]"
                            check = "Switch Modes("+now+" "+coordinates+")"
                            del last3check[0]
                            last3check.append(check)
                            gmail_send("CONFIRMATION","SWITCHED TO CHECK. "+str(last3check)+" -41")
                            CHECKMODE = True
                            TIMEMODE  = False
                            runningT  = False
                    elif "UP" in message:
                            print("CONFIRMING THAT OTS IS RUNNING")
                            time.sleep(1)
                            if os.path.exists(REPORTTIME) == False:
                                    report = open(REPORTTIME, 'w')
                                    report.write(now + " UP COMMAND RECEIVED")
                                    report.close()
                            elif os.path.exists(REPORTTIME) == True:
                                    report = open(REPORTTIME, 'a')
                                    report.write("\n" + now + " UP COMMAND RECEIVED")
                                    report.close()
                                    empty_folder(mail)
                            if "(" in message and ")" in message:
                                coordinates = re.findall(regex,message)
                                coordinates = str(coordinates)
                            else:
                                coordinates = "[no coordinates]"
                            check = "Up("+now+" "+coordinates+")"
                            del last3check[0]
                            last3check.append(check)
                            gmail_send("CONFIRMATION","UP IN TIME. "+str(last3check)+" -41")
                            timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
                            timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
                            ALPHA          = False
                            missedCount    = 0
            elif DELTA >= timeT:
                missedCount += 1
                if os.path.exists(REPORTTIME) == False:
                    report = open(REPORTTIME, 'w')
                    report.write(now + " MISSED TIME-WINDOW! (" + str(missedCount) + " total)")
                    report.close()
                elif os.path.exists(REPORTTIME) == True:
                    report = open(REPORTTIME, 'a')
                    report.write("\n" + now + " MISSED TIME WINDOW! (" + str(missedCount) + " total)")
                    report.close()
                check = "MISSED CHECK("+now+")"
                del last3check[0]
                last3check.append(check)
                gmail_send("NOTIFICATION","MISSED CHECK (TIME)"+str(last3check)+" -41")
                #INFORM OVERWATCH
                message = client.messages.create(
                        to     = OVERWATCH,
                        from_  = "+447480781141",
                        body   = "OVERWATCH. Your Operator missed a time window. That's " + str(missedCount) + " in total Sir. It's up to you how to proceed.   - 41"
                        )
                def empty_folder(m, do_expunge=True):
                            m.select("inbox")  # select all trash
                            m.store("1:*", '+FLAGS', '\\Deleted')  # Flag all Trash as Deleted
                            if do_expunge:  # See Gmail Settings -> Forwarding and POP/IMAP -> Auto-Expunge
                                m.expunge()  # not need if auto-expunge enabled
                            else:
                                print("Expunge was skipped.")
                                return
                empty_folder(mail)
                timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
                timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
                if missedCount == 3:
                        try:
                                requests.get("http://127.0.0.1:8000/shutdown")
                        except requests.exceptions.ConnectionError:
                                pass
                        os.startfile("protocols\\threemissed.lnk")
                        time.sleep(1)
                        call = client.calls.create(
                                to= OVERWATCH,
                                from_= "+447480781141",
                                url=URL,
                                method='GET'
                                )
                elif missedCount > 3:
                        try:
                                requests.get("http://127.0.0.1:8000/shutdown")
                        except requests.exceptions.ConnectionError:
                                pass
                        os.startfile("protocols\\moremissed.lnk")
                        time.sleep(1)
                        call = client.calls.create(
                                to= OVERWATCH,
                                from_= "+447480781141",
                                url=URL,
                                method='GET'
                                )
        print(Fore.LIGHTGREEN_EX + "TIME RECORDING ENDED!" + Style.RESET_ALL)
        report = open(REPORTTIME, 'a')
        report.write("\n" + now + " TIME RECORDING ENDED!")
        report.close()
        if os.path.exists("REPORTS\\TIME1.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME1.txt")
        elif os.path.exists("REPORTS\\TIME2.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME2.txt")
        elif os.path.exists("REPORTS\\TIME3.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME3.txt")
        elif os.path.exists("REPORTS\\TIME4.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME4.txt")
        elif os.path.exists("REPORTS\\TIME5.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME5.txt")
        elif os.path.exists("REPORTS\\TIME6.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME6.txt")
        elif os.path.exists("REPORTS\\TIME7.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME7.txt")
        elif os.path.exists("REPORTS\\TIME8.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME8.txt")
        elif os.path.exists("REPORTS\\TIME9.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME9.txt")
        elif os.path.exists("REPORTS\\TIME10.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME10.txt")
        elif os.path.exists("REPORTS\\TIME11.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME11.txt")
        elif os.path.exists("REPORTS\\TIME12.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME12.txt")
        elif os.path.exists("REPORTS\\TIME13.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME13.txt")
        elif os.path.exists("REPORTS\\TIME14.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME14.txt")
        elif os.path.exists("REPORTS\\TIME15.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME15.txt")
        elif os.path.exists("REPORTS\\TIME16.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME16.txt")
        elif os.path.exists("REPORTS\\TIME17.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME17.txt")
        elif os.path.exists("REPORTS\\TIME18.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME18.txt")
        elif os.path.exists("REPORTS\\TIME19.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME19.txt")
        elif os.path.exists("REPORTS\\TIME20.txt") == False:
            os.rename(REPORTTIME, "REPORTS\\TIME20.txt")
    elif CHECKMODE == True:################################################################################################################################################################################################# CHECKMODE
        timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
        timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
        SWITCH = False
        zcount = 0
        for i in CHECKPOINTS:
            if os.path.exists(REPORTCHECK) == False:
                report = open(REPORTCHECK, 'w')
                report.write(now + " TRIP STARTED!")
                report.close()
            if i in open(REPORTCHECK).read():
                continue
            time.sleep(0.5)
            now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
            now = str(now)
            print(clear)
            print("           >--- "+Fore.LIGHTRED_EX+"O"+Fore.RED+"perative "+Fore.LIGHTRED_EX+"T"+Fore.RED+"ravel "+Fore.LIGHTRED_EX+"S"+Fore.RED+"ecurity System "+Style.RESET_ALL+"---< ("+Style.BRIGHT+"5.0"+Style.RESET_ALL+")"+Fore.RED)
            print("                    OPERATION "+Fore.LIGHTRED_EX+OPERATION.upper()+Style.RESET_ALL)
            print(MODE)
            print("                    "+now)
            print("                    CHECKPOINT MODE ("+CCC+")")
            timerNOW     = datetime.datetime.now().strftime("%H:%M:%S, %m/%d/%Y")
            timerNOW     = datetime.datetime.strptime(timerNOW, "%H:%M:%S, %m/%d/%Y")
            DELTA = timerNOW - timerSTART
            if   CCC == "4 hours":
                if DELTA.seconds >= 10800 and DELTA.seconds < 14400:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 14400:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            elif CCC == "3 hours":
                if DELTA.seconds >= 7200 and DELTA.seconds < 10800:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 10800:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            elif CCC == "2 hours":
                if DELTA.seconds >= 5400 and DELTA.seconds < 7200:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 7200:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            elif CCC == "1 hour":
                if DELTA.seconds >= 2700 and DELTA.seconds < 3600:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 3600:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            elif CCC == "3 minutes (test)":
                if DELTA.seconds >= 120 and DELTA.seconds < 180:
                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                elif DELTA.seconds >= 180:
                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                else:
                    print("Passed time: "+str(DELTA))
            print("Waiting for Checkpoint " + i + " (" + str(missedCount) + " missed)")
            time.sleep(1)
            if i not in open(REPORTCHECK).read():
                runningC = True
                SWITCH   = False
                while runningC == True:
                    emails = True
                    messages = True
                    LoggedIn = False
                    while LoggedIn == False:
                        now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
                        now = str(now)
                        try:
                            mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
                            mail.login(fromaddr, pw)
                            LoggedIn = True
                        except (imaplib.IMAP4.error, imaplib.IMAP4.abort,ConnectionResetError):
                            print(Fore.LIGHTRED_EX + "LOGIN FAILED" + Style.RESET_ALL)
                            if os.path.exists("ERRORLOG.txt") == False:
                                    report = open("ERRORLOG.txt", 'w')
                                    report.write(now + " LOGINERROR")
                                    report.close()
                            elif os.path.exists("ERRORLOG.txt") == True:
                                    report = open("ERRORLOG.txt", 'a')
                                    report.write("\n" + now + " LOGINERROR")
                                    report.close()
                    listloop = True
                    while listloop == True:
                        try:
                            mail.list()
                            mail.select("inbox")
                            listloop = False
                        except:
                            print("ERROR (mail.list)")
                    result, data   = mail.search(None, 'SUBJECT "[OTS]"')
                    result2, data2 = mail.search(None, 'FROM "noreply@findmespot.com"')
                    ids  = data[0]
                    ids2 = data2[0]
                    id_list  = ids.split()
                    id_list += ids2.split()
                    try:
                        latest_email_id = id_list[-1]
                        messages = True
                    except IndexError:
                        now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
                        now = str(now)
                        print(clear)
                        print("           >--- "+Fore.LIGHTRED_EX+"O"+Fore.RED+"perative "+Fore.LIGHTRED_EX+"T"+Fore.RED+"ravel "+Fore.LIGHTRED_EX+"S"+Fore.RED+"ecurity System "+Style.RESET_ALL+"---< ("+Style.BRIGHT+"5.0"+Style.RESET_ALL+")"+Fore.RED)
                        print("                    OPERATION "+Fore.LIGHTRED_EX+OPERATION.upper()+Style.RESET_ALL)
                        print()
                        print("                    "+now)
                        print("                    CHECKPOINT MODE")
                        zcount += 1
                        if ALPHA == True and zcount == 2:
                            print(Fore.LIGHTYELLOW_EX+"                    ALPHA ALPHA ALPHA"+Style.RESET_ALL)
                            zcount = 0
                        elif ALPHA == False:
                            print("")
                        if zcount >= 2:
                            zcount = 0
                        messages     = False
                        timerNOW     = datetime.datetime.now().strftime("%H:%M:%S, %m/%d/%Y")
                        timerNOW     = datetime.datetime.strptime(timerNOW, "%H:%M:%S, %m/%d/%Y")
                        DELTA        = timerNOW - timerSTART
                        if   CCC == "4 hours":
                                if DELTA.seconds >= 10800 and DELTA.seconds < 14400:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 14400:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        elif CCC == "3 hours":
                                if DELTA.seconds >= 7200 and DELTA.seconds < 10800:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 10800:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        elif CCC == "2 hours":
                                if DELTA.seconds >= 5400 and DELTA.seconds < 7200:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 7200:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        elif CCC == "1 hour":
                                if DELTA.seconds >= 2700 and DELTA.seconds < 3600:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 3600:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        elif CCC == "3 minutes (test)":
                                if DELTA.seconds >= 120 and DELTA.seconds < 180:
                                    print("Passed time: "+Fore.LIGHTYELLOW_EX+str(DELTA)+Style.RESET_ALL)
                                elif DELTA.seconds >= 180:
                                    print("Passed time: "+Fore.LIGHTRED_EX+str(DELTA)+Style.RESET_ALL)
                                else:
                                    print("Passed time: "+str(DELTA))
                        print("Waiting for Checkpoint " + i + " (" + str(missedCount) + " missed)")
                        time.sleep(1)
                        if DELTA >= timeC:  
                            missedCount += 1
                            if os.path.exists(REPORTCHECK) == False:
                                report = open(REPORTCHECK, 'w')
                                report.write(now + " MISSED CHECKPOINT " + i + " !")
                                report.close()
                            elif os.path.exists(REPORTCHECK) == True:
                                report = open(REPORTCHECK, 'a')
                                report.write("\n" + now + " MISSED CHECKPOINT " + i + " !")
                                report.close()
                            if missedCount == 3:
                                try:
                                    requests.get("http://127.0.0.1:8000/shutdown")
                                except requests.exceptions.ConnectionError:
                                    pass
                                os.startfile("protocols\\threemissed.lnk")
                                time.sleep(1)
                                call = client.calls.create(
                                    to= OVERWATCH,
                                    from_= "+447480781141",
                                    url=URL,
                                    method='GET'
                                    )
                            elif missedCount > 3:
                                try:
                                    requests.get("http://127.0.0.1:8000/shutdown")
                                except requests.exceptions.ConnectionError:
                                    pass
                                os.startfile("protocols\\moremissed.lnk")
                                time.sleep(1)
                                call = client.calls.create(
                                    to= OVERWATCH,
                                    from_= "+447480781141",
                                    url=URL,
                                    method='GET'
                                    )
                            #INFORM OVERWATCH
                            message = client.messages.create(
                                    to     = OVERWATCH,
                                    from_  = "+447480781141",
                                    body   = "OVERWATCH. Your Operator missed a time window. That's " + str(missedCount) + " in total Sir. It's up to you how to proceed.   - 41"
                                    )
                            timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
                            timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
                            print(Fore.LIGHTGREEN_EX + "MISSED CHECKPOINT " + i + "! " + Style.RESET_ALL + Fore.GREEN + now + Style.RESET_ALL)
                            timer = 0
                            runningC = False
                    if messages == True:
                        def empty_folder(m, do_expunge=True):
                            m.select("inbox")  # select all trash
                            m.store("1:*", '+FLAGS', '\\Deleted')  # Flag all Trash as Deleted
                            if do_expunge:  # See Gmail Settings -> Forwarding and POP/IMAP -> Auto-Expunge
                                m.expunge()  # not need if auto-expunge enabled
                            else:
                                print("Expunge was skipped.")
                                return
                        result, data = mail.fetch(latest_email_id, "RFC822")
                        m = mailparser.parse_from_bytes(data[0][1])
                        text = "From: "  # the Signature of emails sent by my phone. After that, anything is irrelevant
                        entry = m.body.split(text, 1)[0]
                        message = entry.upper()
                        empty_folder(mail)
                        #if i in message:
                        #        timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
                        #        timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
                        #        print(Fore.LIGHTGREEN_EX + "REACHED CHECKPOINT " + i + "! " + Style.RESET_ALL + Fore.GREEN + now + Style.RESET_ALL)                           <-- Whats all this???
                        #        ALPHA = False
                        #        if os.path.exists(REPORTCHECK) == False:
                        #                report = open(REPORTCHECK, 'w')
                        #                report.write(now + " REACHED CHECKPOINT " + i)
                        #                report.close()
                        #        elif os.path.exists(REPORTCHECK) == True:
                        #                report = open(REPORTCHECK, 'a')
                        #                report.write("\n" + now + " REACHED CHECKPOINT " + i)
                        #                report.close()
                        #        runningC = False
                        if "CHECK" in message:
                                missedCount    = 0
                                timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
                                timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
                                print(Fore.LIGHTGREEN_EX + "REACHED CHECKPOINT " + i + "! " + Style.RESET_ALL + Fore.GREEN + now + Style.RESET_ALL)
                                if os.path.exists(REPORTCHECK) == False:
                                        report = open(REPORTCHECK, 'w')
                                        report.write(now + " REACHED CHECKPOINT " + i)
                                        report.close()
                                elif os.path.exists(REPORTCHECK) == True:
                                        report = open(REPORTCHECK, 'a')
                                        report.write("\n" + now + " REACHED CHECKPOINT " + i)
                                        report.close()
                                if ALPHA == True:
                                    ALPHA = False
                                    check = "Alpha End. Reached "+i+"("+now+")"
                                    del last3check[0]
                                    last3check.append(check)
                                    gmail_send("CONFIRMATION","ALPHA END. REACHED "+i+" "+str(last3check)+" -41")
                                elif ALPHA == False:
                                    check = "Reached "+i+"("+now+")"
                                    del last3check[0]
                                    last3check.append(check)
                                    gmail_send("CONFIRMATION","REACHED "+i+" "+str(last3check)+" -41")
                                runningC = False
                        elif "ALPHA" in message:
                                #INFORM OVERWATCH
                                ALPHA = True
                                try:
                                        requests.get("http://127.0.0.1:8000/shutdown")
                                except requests.exceptions.ConnectionError:
                                        pass
                                os.startfile("protocols\\ALPHA.lnk")
                                time.sleep(1)
                                call = client.calls.create(
                                        to= OVERWATCH,
                                        from_= "+447480781141",
                                        url=URL,
                                        method='GET'
                                        )
                                message = client.messages.create(
                                        to     = OVERWATCH,
                                        from_  = "+447480781141",
                                        body   = "Good day sir. Your Operator just used the ALPHA command, something seems to be indicating danger. Be ready.  -41"
                                        )
                                if os.path.exists(REPORTCHECK) == False:
                                        report = open(REPORTCHECK, 'w')
                                        report.write(now + " ALPHA COMMAND RECEIVED")
                                        report.close()
                                elif os.path.exists(REPORTCHECK) == True:
                                        report = open(REPORTCHECK, 'a')
                                        report.write("\n" + now + " ALPHA COMMAND RECEIVED")
                                        report.close()
                                        empty_folder(mail)
                                check = "Alpha Start("+now+")"
                                del last3check[0]
                                last3check.append(check)
                                gmail_send("CONFIRMATION","ALPHA CONFIRMED. "+str(last3check)+" -41")
                        elif "HOTEL" in message or "INITIALIZE" in message:  # [!]  F - PROTOCOL  [!]
                                print(now + Fore.LIGHTRED_EX + " F-PROTOCOL REQUESTED!" + Style.RESET_ALL)
                                check = "F-Protocol Requested("+now+")"
                                del last3check[0]
                                last3check.append(check)
                                time.sleep(0.1)
                                if os.path.exists(REPORTCHECK) == False:
                                        report = open(REPORTCHECK, 'w')
                                        report.write(now + " HOTEL COMMAND RECEIVED")
                                        report.close()
                                elif os.path.exists(REPORTCHECK) == True:
                                        report = open(REPORTCHECK, 'a')
                                        report.write("\n" + now + " HOTEL COMMAND RECEIVED")
                                        report.close()
                                        empty_folder(mail)
                                        pending = True
                                        try:
                                                requests.get("http://127.0.0.1:8000/shutdown")
                                        except requests.exceptions.ConnectionError:
                                                pass
                                        os.startfile("protocols\\HOTEL.lnk")
                                        time.sleep(1)
                                        call = client.calls.create(
                                                to= OVERWATCH,
                                                from_= "+447480781141",
                                                url=URL,
                                                method='GET'
                                                )
                                        message = client.messages.create(
                                                to     = OVERWATCH,
                                                from_  = "+447480781141",
                                                body   = "Attention. The F-Protocol has been requested. You being the Overwatch have to decide wether to initiate or to abort. Be aware that once confirmed, the Protocol can not be stopped and authorities will be contacted. Your choice Sir.   -41"
                                                )
                                        if os.path.exists(REPORTCHECK) == False:
                                                report = open(REPORTCHECK, 'w')
                                                report.write(now + " F-PROTOCOL REQUESTED!")
                                                report.close()
                                        elif os.path.exists(REPORTCHECK) == True:
                                                report = open(REPORTCHECK, 'a')
                                                report.write("\n" + now + " F-PROTOCOL REQUESTED!")
                                                report.close()
                                        while pending == True:
                                                now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
                                                now = str(now)
                                                print(clear)
                                                print(Fore.LIGHTRED_EX+"               !!!-       F-PROTOCOL INITIATED       -!!!"+Style.RESET_ALL)
                                                print(Fore.YELLOW     +"               Pending for confirmation from Overwatch..."+Style.RESET_ALL)
                                                mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
                                                mail.login(fromaddr,pw)
                                                listloop = True
                                                while listloop == True:
                                                    try:
                                                        mail.list()
                                                        mail.select("inbox")
                                                        listloop = False
                                                    except:
                                                        print("ERROR (mail.list)")
                                                result, data   = mail.search(None, 'SUBJECT "[OTS]"')
                                                result2, data2 = mail.search(None, 'FROM "noreply@findmespot.com"')
                                                ids  = data[0]
                                                ids2 = data2[0]
                                                id_list  = ids.split()
                                                id_list += ids2.split()
                                                noemails = True
                                                try:
                                                        latest_email_id = id_list[-1]
                                                        noemails = False
                                                except IndexError:
                                                        print()
                                                        print("               WAITING FOR CONFIRMATION SINCE " + str(timerNOW))
                                                        noemails = True
                                                        time.sleep(1)
                                                        print(clear)
                                                if noemails == False:
                                                        def empty_folder(m, do_expunge=True):
                                                                print(Fore.LIGHTGREEN_EX + "CHECKED IN! " + Style.RESET_ALL + Fore.GREEN + now + Style.RESET_ALL)
                                                                m.select("inbox")  # select all trash
                                                                m.store("1:*", '+FLAGS', '\\Deleted')  # Flag all Trash as Deleted
                                                                if do_expunge:  # See Gmail Settings -> Forwarding and POP/IMAP -> Auto-Expunge
                                                                        m.expunge()  # not need if auto-expunge enabled
                                                                else:
                                                                        print("Expunge was skipped.")
                                                                        return
                                                        result, data = mail.fetch(latest_email_id,"RFC822")
                                                        m = mailparser.parse_from_bytes(data[0][1])
                                                        text = "From: " #the Signature of emails sent by my phone. After that, anything is irrelevant
                                                        entry = m.body.split(text, 1)[0]
                                                        message = entry.upper()
                                                        empty_folder(mail)
                                                        if "ABORT" in message or "CHECK" in message:
                                                                check = "F-Protocol Aborted("+now+")"
                                                                del last3check[0]
                                                                last3check.append(check)
                                                                gmail_send("ATTENTION","F-PROTOCOL ABORTED. ("+now+") -41")
                                                                if os.path.exists(REPORTCHECK) == False:
                                                                        report = open(REPORTCHECK, 'w')
                                                                        report.write(now + " F-PROTOCOL ABORTED.")
                                                                        report.close()
                                                                elif os.path.exists(REPORTCHECK) == True:
                                                                        report = open(REPORTCHECK, 'a')
                                                                        report.write("\n" + now + " F-PROTOCOL ABORTED.")
                                                                        report.close()
                                                                        empty_folder(mail)
                                                                timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
                                                                timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
                                                                pending = False
                                                        elif "CONFIRM" in message:#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!
                                                                print(clear)#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!
                                                                print("Initiating F-Protocol...")#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!    C A L L I N G      A U T H O R I T I E S   ! ! !      #!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#
                                                                try:#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!
                                                                        requests.get("http://127.0.0.1:8000/shutdown")#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!
                                                                except requests.exceptions.ConnectionError:
                                                                        pass
                                                                os.startfile("protocols\\FOXTROT.lnk")
                                                                time.sleep(1)
                                                                call = client.calls.create(
                                                                        to= COPS, 
                                                                        from_= "+447480781141",
                                                                        url=URL,
                                                                        method='GET'
                                                                        )
                                                                call = client.calls.create(
                                                                        to= FOROFF, 
                                                                        from_= "+447480781141",
                                                                        url=URL,
                                                                        method='GET'
                                                                        )
                                                                #INFORM OVERWATCH
                                                                message = client.messages.create(
                                                                        to     = OVERWATCH,
                                                                        from_  = "+447480781141",
                                                                        body   = """Overwatch. The F-Protocol has been activated. Be aware, that authorities are being called and briefed at this moment, leading them to you for further Details. Give them the F-Package. It's everything we have: Planned Route, Subject Files, OTS Reports, Operation Documents. The Password is """+Fpassword+""".  -41 """
                                                                        )
                                                                if os.path.exists(REPORTCHECK) == False:
                                                                        report = open(REPORTCHECK, 'w')
                                                                        report.write(now + " F-PROTOCOL CONFIRMED!!!")
                                                                        report.close()
                                                                elif os.path.exists(REPORTCHECK) == True:
                                                                        report = open(REPORTCHECK, 'a')
                                                                        report.write("\n" + now + " F-PROTOCOL CONFIRMED!!!")
                                                                        report.close()
                                                                        empty_folder(mail)
                                                                pending = False
                                                                endless = True
                                                                while endless == True:
                                                                    print(clear)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print(Fore.LIGHTRED_EX+"!!!  F-PROTOCOL ACTIVATED  !!!"+Style.RESET_ALL)
                                                                    time.sleep(1)
                                                                    print(clear)
                                                                    print("")
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print("")
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print("")
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print("")
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print("")
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print("")
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print("")
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print("")
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print("")
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print("")
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print("")
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print("")
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    print("")
                                                                    print(Fore.RED        +"     Operator compromised     "+Style.RESET_ALL)
                                                                    time.sleep(1)############################################################################################################################################################# E  N  D  !!!
                                                        else:
                                                                print(Fore.LIGHTRED_EX + "F-PROTOCOL INITIALIZATION FAILED" + Style.RESET_ALL)
                                                                if os.path.exists("ERRORLOG.txt") == False:
                                                                    report = open("ERRORLOG.txt", 'w')
                                                                    report.write(now + " F-INIT ERROR")
                                                                    report.close()
                                                                elif os.path.exists("ERRORLOG.txt") == True:
                                                                    report = open("ERRORLOG.txt", 'a')
                                                                    report.write("\n" + now + " F-INIT ERROR")
                                                                    report.close()
                        elif "SWITCH" in message:
                            print("SWITCHING MODES")
                            time.sleep(1)
                            missedCount = 0
                            if os.path.exists(REPORTCHECK) == False:
                                    report = open(REPORTCHECK, 'w')
                                    report.write(now + " SWITCHING MODES")
                                    report.close()
                            elif os.path.exists(REPORTCHECK) == True:
                                    report = open(REPORTCHECK, 'a')
                                    report.write("\n" + now + " SWITCHING MODES")
                                    report.close()
                                    empty_folder(mail)
                            message = client.messages.create(
                                    to     = OVERWATCH,
                                    from_  = "+447480781141",
                                    body   = "Greetings Sir. OTS switched to Time-Mode. - 41"                                      
                                    )
                            check = "Switch Modes("+now+")"
                            del last3check[0]
                            last3check.append(check)
                            gmail_send("CONFIRMATION","SWITCHED TO TIME. LAST CHECKPOINT "+i+" "+str(last3check)+" -41")
                            SWITCH = True
                            runningC = False
                        elif "UP" in message:
                            print("CONFIRMING THAT OTS IS RUNNING")
                            time.sleep(1)
                            if os.path.exists(REPORTCHECK) == False:
                                    report = open(REPORTCHECK, 'w')
                                    report.write(now + " UP COMMAND RECEIVED")
                                    report.close()
                            elif os.path.exists(REPORTCHECK) == True:
                                    report = open(REPORTCHECK, 'a')
                                    report.write("\n" + now + " UP COMMAND RECEIVED")
                                    report.close()
                                    empty_folder(mail)
                            check = "Up("+now+")"
                            del last3check[0]
                            last3check.append(check)
                            gmail_send("CONFIRMATION","UP IN CHECK. STANDBY FOR CHECKPOINT "+i+" "+str(last3check)+" -41")
                            timerSTART     = datetime.datetime.today().strftime("%H:%M:%S | %m/%d/%Y")
                            timerSTART     = datetime.datetime.strptime(timerSTART, "%H:%M:%S | %m/%d/%Y")
                            ALPHA          = False
                            missedCount    = 0
                if SWITCH == True:
                        break
        print(Fore.LIGHTGREEN_EX + "ALL CHECKPOINTS REACHED!" + Style.RESET_ALL)
        report = open(REPORTCHECK,'a')
        report.write("\n TRIP ENDED!")
        report.close()
        if   os.path.exists("REPORTS\\TRIP1.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP1.txt")
        elif os.path.exists("REPORTS\\TRIP2.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP2.txt")
        elif os.path.exists("REPORTS\\TRIP3.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP3.txt")
        elif os.path.exists("REPORTS\\TRIP4.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP4.txt")
        elif os.path.exists("REPORTS\\TRIP5.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP5.txt")
        elif os.path.exists("REPORTS\\TRIP6.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP6.txt")
        elif os.path.exists("REPORTS\\TRIP7.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP7.txt")
        elif os.path.exists("REPORTS\\TRIP8.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP8.txt")
        elif os.path.exists("REPORTS\\TRIP9.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP9.txt")
        elif os.path.exists("REPORTS\\TRIP10.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP10.txt")
        elif os.path.exists("REPORTS\\TRIP11.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP11.txt")
        elif os.path.exists("REPORTS\\TRIP12.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP12.txt")
        elif os.path.exists("REPORTS\\TRIP13.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP13.txt")
        elif os.path.exists("REPORTS\\TRIP14.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP14.txt")
        elif os.path.exists("REPORTS\\TRIP15.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP15.txt")
        elif os.path.exists("REPORTS\\TRIP16.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP16.txt")
        elif os.path.exists("REPORTS\\TRIP17.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP17.txt")
        elif os.path.exists("REPORTS\\TRIP18.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP18.txt")
        elif os.path.exists("REPORTS\\TRIP19.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP19.txt")
        elif os.path.exists("REPORTS\\TRIP20.txt") == False:
            os.rename(REPORTCHECK, "REPORTS\\TRIP20.txt")
        TIMEMODE  = True
        CHECKMODE = False
