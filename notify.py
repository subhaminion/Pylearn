# #!/usr/bin/env python
# #-*- coding: utf-8 -*-

# import subprocess

# def sendmessage(message):
#     subprocess.Popen(['notify-send', message])
#     return

# sendmessage('Hai Subham How are you!')
import os
os.system('notify-send "Notification" "Hi Subham How are you"')