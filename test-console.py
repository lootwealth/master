import win32api
import time

while True:
    win32api.keybd_event(91, 0, 0, 0)
    time.sleep(1)
    win32api.keybd_event(77, 0, 0, 0)
    time.sleep(1)
    win32api.keybd_event(77, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(91, 0, win32con.KEYEVENTF_KEYUP, 0)
