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
needrevive = 475 #hp = 0
needheal = 3820 #hp ~30%
fulllife = 3518 #hp = 100%
needrest = 4749 #mana ~30% amarelo
needrest2 = 2100 #mana ~15% azul
fullmana = 4423 #mana ~100% amarelo
fullmana2 = 3191 #mana ~100% azul
    

class Cord:
     
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
    #normalchest cords
    n_open_chest = (404, 116)
    n_leave_chest =(406, 139)
    #key chest
    k_picklock = (398, 114) 
    k_use_key = (414, 141)
    k_use_tokens = (0,0)#not putting the right coordenates for the bot. I'll never use that(414, 161)
    k_leave_chest = (408, 183)
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
    time.sleep(.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #print "Click."          #completely optional. But nice for debugging purposes.

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

def get_hp1():
    box = (Cord.hp1)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\hp1__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_hp2():
    box = (Cord.hp2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\hp2__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_hp3():
    box = (Cord.hp3)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\hp3__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_hp4():
    box = (Cord.hp4)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\hp4__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_hp5():
    box = (Cord.hp5)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\hp5__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_hp6():
    box = (Cord.hp6)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\hp6__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_hp7():
    box = (Cord.hp7)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\hp7__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana1():
    box = (Cord.mana1)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\mana1__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana2():
    box = (Cord.mana2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\mana2__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana3():
    box = (Cord.mana3)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\mana3__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana4():
    box = (Cord.mana4)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\mana4__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana5():
    box = (Cord.mana5)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\mana5__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana6():
    box = (Cord.mana6)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\mana6__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana7():
    box = (Cord.mana7)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\mana7__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_all():
    get_hp1()
    get_hp2()
    get_hp3()
    get_hp4()
    get_hp5()
    get_hp6()
    get_hp7()
    get_mana1()
    get_mana2()
    get_mana3()
    get_mana4()
    get_mana5()
    get_mana6()
    get_mana7()        

def revive1():
    mousePos(Cord.char5)
    leftClick()
    mousePos(Cord.skill7)
    leftClick()
    mousePos(Cord.char1)
    leftClick()
def revive2():
    mousePos(Cord.char5)
    leftClick()
    mousePos(Cord.skill7)
    leftClick()
    mousePos(Cord.char2)
    leftClick()
def revive3():
    mousePos(Cord.char5)
    leftClick()
    mousePos(Cord.skill7)
    leftClick()
    mousePos(Cord.char3)
    leftClick()
def revive4():
    mousePos(Cord.char5)
    leftClick()
    mousePos(Cord.skill7)
    leftClick()
    mousePos(Cord.char4)
    leftClick()
def revive5(): #this is the healer. So this is diferent to cast miracle.
    mousePos(Cord.char2)
    leftClick()
    mousePos(Cord.skill5)
    leftClick()
def revive6():
    mousePos(Cord.char5)
    leftClick()
    mousePos(Cord.skill7)
    leftClick()
    mousePos(Cord.char6)
    leftClick()
def revive7():
    mousePos(Cord.char5)
    leftClick()
    mousePos(Cord.skill7)
    leftClick()
    mousePos(Cord.char7)
    leftClick()
    
    
def startGame():
    #check if a character is dead
    if needrevive > get_hp1():
        print 'Reviving character 1'
        revive1()
    
    if needrevive > get_hp2():
        print 'Reviving character 2'
        revive2()
    
    if needrevive > get_hp3():
        print 'Reviving character 3'
        revive3()
    
    if needrevive > get_hp4():
        print 'Reviving character 4'
        revive4()
    
    if needrevive > get_hp5():
        print 'Reviving character 5. This is the Healer.'
        revive5()
    
    if needrevive > get_hp6():
        print 'Reviving character 6'
        revive6()
    
    if needrevive > get_hp7():
        print 'Reviving character 7'
        revive7()
    else:
        print 'Noone need revive'

    #Check if someone needs heal
        
    #location search for rest
    mousePos((Cord.b7_rest))
    leftClick()
    print 'Rest.'
    time.sleep(5.0)
    #location search for monsters button
    mousePos((Cord.b5_monsters))
    leftClick()
    print 'Look for monsters.'
    time.sleep(1.5)
    #location space bar button
    mousePos((Cord.spacebar))
    leftClick()
    time.sleep(2.3)
    mousePos((Cord.spacebar))
    leftClick()
    print 'Space bar x2.'
    time.sleep(2.3)
    #discardkeychest
    mousePos((Cord.k_leave_chest))
    leftClick()
    print 'Leave key chest.'
    time.sleep(0.2)
    #Opennormalchest
    mousePos((Cord.n_open_chest))
    leftClick()
    print 'Open normal chest.'
    time.sleep(0.2)
    #discardnormalchest
    mousePos((Cord.n_leave_chest))
    leftClick()
    print 'Leave normal chest.'
    time.sleep(0.2)
    #confirmdisrcarditem
    mousePos((Cord.yes))
    leftClick()
    print 'Confirm discard item.'
    time.sleep(0.2)

def main():
    k=0
    while (k < 1000):
        print 'k = ',k
        startGame()
        k=k+1
                
if __name__ == '__main__':
    pass    

