"""
 
All coordinates assume a screen resolution of ????x????, and Chrome 
maximized with no Bookmarks or Toolbar enabled.
Down key has been hit 3 times to center play area in browser.
The bot assumes you are using 4 characters on front and 3 on the back.
Healer is on the back row, left position (char5).
Paladin is on front row, 2nd position (char2).
Revive from Healer is on skill7.
Heal all is on kill2.
Miracle from Paladin is on Skill7.
x_pad = 241
y_pad = 147
Play area =  x_pad+1, y_pad+1, 1045, 751
"""

import os
import time
import ImageGrab
import win32api, win32con
import ImageOps
from numpy import *

# Globals
# ------------------

x_pad = 241
y_pad = 147
#comparison vaules for hp and mana
needrevive = 500 #475 #hp = 0
needheal = 3800#3820 #hp ~30%
fulllife = 3518 #hp = 100%
needrest = 4749 #mana ~30% amarelo
needmana = 2200 #2100 #mana ~15% azul
fullmana = 4423 #mana ~100% amarelo
fullmana2 = 3191 #mana ~100% azul
battleready = 584 #value that the bot sees when the button for search monsters is active.
automataready = 300 #318 #value the bot sees when the button for hitting spacebar is active   
normalchest = 11961 #value the bot sees when there is a normal chest
rarechest = 28235 #value the bot sees when there is a rare chest (that need lockpicking or keys)
openedrarechest = 26619 # value the bot sees when there is an opened rare chest. (after lockpick)

class Cord:
    none = (0,0)
     
    char1 = (194, 488)
    char2 = (304, 481)
    char3 = (415, 478)
    char4 = (530, 481)
    char5 = (258, 557)
    char6 = (370, 566)
    char7 = (479, 565)
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
    lookformonsters = (497,517,507,528)#cord for a white box inside the button shaped as a slime
    lookforautomata = (1012,708,1020,716) #cord for a white box inside the automatas button
    lookforchest = (590,386,747,402)#cord for comparison if there is a chest, and if it is normal or rare chest.
    
    #normalchest cords
    n_chest = (434,256)
    n_open_chest = (396, 119)
    n_leave_chest =(393, 138)
    #rare chest
    r_lockpick = (396, 119)
    r_use_key = (393, 138)
    r_use_tokens = (396,162)#beware when using this coordinates on the code. They were not banned because are needed for leaving an unopened chest.
    r_leave_chest = (396, 185)
    openeditem = (421,209)
    openeditem2 = (421,208)
    #Confirmation required
    yes = (360, 362)
    no = (441, 365)
    #health bars
    hp1 = (506,593,510,648)
    hp2 = (617,593,621,648)
    hp3 = (728,593,732,648)
    hp4 = (839,593,843,648)
    hp5 = (561,678,565,733)
    hp6 = (672,678,676,733)
    hp7 = (783,678,787,733)
    #mana bars
    mana1 = (519,593,523,648)
    mana2 = (630,593,634,648)
    mana3 = (741,593,745,648)
    mana4 = (852,593,856,648)
    mana5 = (574,678,578,733)
    mana6 = (685,678,689,733)
    mana7 = (796,678,800,733)

    
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #print "Click."          #completely optional. But nice for debugging purposes.

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(2.0)
    print ('left Down')

def grabitem(cord_from,cord_to):
    mousePos(Cord.cord_from)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(1.0)
    mousePos(Cord.cord_to)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(1.0)    
    print ('mouse moved')    
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #time.sleep(.1)
    print ("left release")
    
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def grab():
    mousePos(Cord.openeditem)
    leftDown()
    mousePos(Cord.openeditem2)
    time.sleep(1.0)
    mousePos(Cord.char4)
    leftUp()
   
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,y)


        
                
if __name__ == '__main__':
    pass    

