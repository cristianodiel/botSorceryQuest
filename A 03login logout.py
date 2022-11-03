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
spin_button_not_ready1 = 7335
spin_button_not_ready2 = 7657
spin_button_not_ready3 = 7347
spin_button_already_spinned_today = 7374
spin_button_already_spinned_today1 = 7335
spin_button_already_spinned_today2 = 7657
spin_button_ready = 32855


class Cord:
    browseruparror = (1054, -79)
    browserdownarror = (1051, 595)
    login = (594, -71)
    signin = (854, -71)
    signout = (838, -69)
    spin = (399, 554)
    spinbutton = (x_pad+320, y_pad+532, x_pad+483, y_pad+577)
    firefox = (1075, -30)
    http = (100, -120)
    nextgame = (600, 490)
    sorceryquest = (50, 490)
    play = (450, 400)

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
    print 'spin button=',a
    #im.save(os.getcwd() + '\\spinbutton__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def check_spinbutton():
    spin_button_ready = 32850
    while spin_button_ready > get_spinbutton():
        if spin_button_already_spinned_today2 == get_spinbutton():
            print 'roulette already spinned today in this account. Moving to next.'
            spin_button_ready = 0
        else:
            time.sleep(1)
            print 'waiting for spin button to appear'
    
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

class account:
    bigdirk = "bigdirk"
    kemaro = "kemaro"
    zenoir = "zenoir"
    gillium = "gillium"
    orb = "orb"
    viguro = "viguro"
    horn = "horn"
    palma = "palma"
    gola = "gola"
    mushura = "mushura"
    mule = "mule"
    zendor = "zendor"
    gimard = "gimard"
    
def openbrowser():
    leftClick(Cord.firefox)
    
def a():
    openbrowser()
    time.sleep(5)
    leftClick(Cord.http)
    keyb ("edgebee")
    keyb("\r")
    time.sleep(7)
    leftClick(Cord.nextgame)
    time.sleep(2)
    leftClick(Cord.sorceryquest)
    time.sleep(3)
    leftClick(Cord.play)
    time.sleep(3)
    call_account(account.bigdirk)
    call_account(account.kemaro)
    call_account(account.zenoir)
    call_account(account.gillium)
    call_account(account.orb)
    call_account(account.horn)
    call_account(account.gola)
    call_account(account.mushura)
    #call_account(account.mule) used tokens
    call_account(account.zendor)
    call_account(account.gimard)
    #call_account(account.palma)
    #call_account(account.viguro)
    
def call_account(account):
    leftClick(Cord.login)
    leftClick(Cord.login)
    keyb(account)
    keyb("\r")
    leftClick(Cord.signin)
    time.sleep(5)
    leftClick(Cord.browserdownarror)
    leftClick(Cord.browserdownarror)
    check_spinbutton()
    leftClick(Cord.spin)
    time.sleep(5)
    leftClick(Cord.spin)
    time.sleep(5)
    leftClick(Cord.browseruparror)
    leftClick(Cord.browseruparror)
    time.sleep(3)
    leftClick(Cord.signout)
    time.sleep(5)
   

if __name__ == '__main__':
    pass    
a()
