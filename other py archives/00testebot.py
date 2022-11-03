"""
 
All coordinates assume a screen resolution of ????x????, and Chrome 
maximized with no Bookmarks or Toolbar enabled.
Down key has been hit 3 times to center play area in browser.
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
from numpy import *

# Globals
# ------------------

x_pad = 241
y_pad = 147


class Cord:
     
    char_front1 = (194, 488)
    char_front2 = (304, 481)
    char_front3 = (415, 478)
    char_front4 = (530, 481)
    char_back1 = (258, 557)
    char_back2 = (370, 566)
    char_back3 = (479, 565)
    skill1 = (658, 489)
    skill2 = (696, 491)
    skill3 = (737, 491)
    skill4 = (773, 491)
    skill5 = (660, 529)
    skill6 = (698, 531)
    skill7 = (735, 529)
    skill8 = (772, 531)
    item1 = (659, 578)
    item2 = (695, 581)
    item3 = (735, 581)
    #actions
    q_attack = (660, 449)
    w_defend = (695, 448)
    e_flee = (733, 448)
    r_automata = (769, 455)
    spacebar = (779, 574)
    #buttons outside battle
    b1_west = (31, 385)
    b2_north = (87, 387)
    b3_south = (145, 387)
    b4_east = (202, 386)
    b5_monsters = (259, 383)
    b6_parties = (317, 381)
    b7_rest = (374, 381)
    b8_lever = (426, 386)
    #normalchest cords
    n_open_chset = (404, 116)
    n_leave_chest =(406, 139)
    #key chest
    k_picklock = (398, 114) 
    k_use_key = (414, 141)
    #k_use_tokens = (414, 161)
    k_leave_chest = (408, 183)

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click."          #completely optional. But nice for debugging purposes.

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
def startGame():
    #location search for monsters button
    mousePos((265, 372))
    leftClick()
    time.sleep(.1)
    #location space bar button
    mousePos((777, 568))
    leftClick()
    time.sleep(2.3)
    mousePos((777, 568))
    leftClick()
    time.sleep(2.3)

def main():
    k=0
    while (k < 10):
        print 'k = ',k
        startGame()
        k=k+1
                
if __name__ == '__main__':
    pass    

