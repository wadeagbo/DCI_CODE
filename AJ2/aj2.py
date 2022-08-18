import os
import time
import datetime
import smtplib                        # optional (advanced)
from   email.mime.multipart  import *   # optional (& advanced)
from   email.mime.text       import *   # optional (& advanced)
from  email.message          import *   # optional
from  colorama               import *  # optional
from art                     import *  # optional


#initializing colorama
init()

# email function (optional & advanced)
# def gmail_send(subject, message, from_mail, to_mail, password):
#     global link
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(from_mail, password)
#     msg            = EmailMessage()
#     message        = f'{message}'
#     msg.set_content(message)
#     msg['Subject'] = subject
#     msg['From']    = waheed.adeagbo@gmail.com
#     msg['To']      = nadeagbo@yahoo.com
#     server.send_message(msg)

new_entry = input("ENTER DIARY ENTRY HERE >>>")

now  = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
print(now)

with open("./copy.txt", "a") as file:
    file.write(now + new_entry + "\n")
