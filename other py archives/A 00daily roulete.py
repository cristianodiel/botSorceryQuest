"""
 
All coordinates assume a screen resolution of ????x????, and Firefox
maximized with no Bookmarks or Toolbar enabled.
Down key was not hit. The program hit is automatically.
The bot assumes you are using 4 characters on front and 3 on the back.
Healer is on the back row, left position.
x_pad = 241
y_pad = 147
Play area =  x_pad+1, y_pad+1, 1045, 751
"""

import os
import time
import win32api, win32con
import ImageOps
import ImageGrab
from numpy import *

# Globals
# ------------------

x_pad = 242
y_pad = 160


class Cord:
    browserdownarror = (1051,609)
    browseruparror = (1058, -66)
    login = (594, -56)
    signin = (863, -59)
    signout = (821, -58)
    spin = (400, 565)
    spinbutton = (x_pad+320, y_pad+532, x_pad+483, y_pad+577)

def leftClick(cord):
    #Cord.mouse = get_cords()
    #print 'mouse before =', Cord.mouse
    mousePos(cord)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click."          #completely optional. But nice for debugging purposes.
    #mousePos(Cord.mouse)

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ("left release")
    
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
   
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,y)
    
def get_spinbutton():
    box = (Cord.spinbutton)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'hp5=',a
    im.save(os.getcwd() + '\\spinbutton__' + str(int(time.time())) + '.png', 'PNG')    
    return a
# -*- coding: utf-8 -*-

def keyb(ch=None,shift=False,control=False,alt=False, delaik=0.02):   
    for b in ch:
        c=b
        if (b>='A' and b<='Z') or shift:
            win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
        if b>='a' and b<='z':
            c=b.upper()
        if alt:
            win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)
            time.sleep(0.250)
        if control:
            win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
        if isinstance(b,(int)):
            cord=b
        else:
            cord=ord(c)

        win32api.keybd_event(cord, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
        if delaik>0.0:
            time.sleep(delaik)
        win32api.keybd_event(cord, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
win32con.KEYEVENTF_KEYUP, 0)
        if delaik>0.0:
            time.sleep(delaik)

        if control:
            win32api.keybd_event(win32con.VK_CONTROL, 0, 
win32con.KEYEVENTF_KEYUP, 0)
        if alt:
            win32api.keybd_event(win32con.VK_MENU, 0, 
win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.05)
        if (b>='A' and b<='Z') or shift:
            win32api.keybd_event(win32con.VK_SHIFT, 0, 
win32con.KEYEVENTF_KEYUP, 0)



#time.sleep(5)  #user has 5 sec for prepare a target-window
#keyb("AZERTYUIOP ")
#keyb("azertyuiop")
#keyb("\r")
#keyb("1234567890",shift=True) #shift == True for french keyboard
#keyb("\n")
#keyb("AAAAAAAAA\n")
#time.sleep(1)
#keyb("f",alt=True)  # {Alt} F   (ouvre menu ?)
#time.sleep(1)
#keyb([27,27])  # 2 x {Escape}
class account:
    bigdirk = "bigdirk"
    kemaro = "kemaro"
    
def daily():
    call_account(account.bigdirk)
    call_account(account.kemaro)
    
def call_account(account):
    leftClick(Cord.login)
    leftClick(Cord.login)
    keyb(account)
    keyb("\r")
    leftClick(Cord.signin)
    time.sleep(5)
    leftClick(Cord.browserdownarror)
    leftClick(Cord.browserdownarror)
    
    time.sleep(15)
    leftClick(Cord.spin)
    time.sleep(5)
    leftClick(Cord.spin)
    time.sleep(5)
    leftClick(Cord.browseruparror)
    leftClick(Cord.browseruparror)
    leftClick(Cord.signout)
    time.sleep(5)
   

if __name__ == '__main__':
    pass    

