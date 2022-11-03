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
#locations
at_temple = 58729
at_city = 56964
at_outskirts = 56764
#buttons
person1 = 21464
person2 = 31606
noperson = 13852
parties = 56405 #other parties screen opened
loadingparties = 4089
stillloading = 3315
honorparty1 = 28802
honorparty2 = 28340
honorparty3 = 28005
alreadyfarmed1 = 19127
alreadyfarmed1 = 20123
alreadyfarmed1 = 18940

battleready = 584 #value that the bot sees when the button for search monsters is active.
automataready = 300 #318 #value the bot sees when the button for hitting spacebar is active   
normalchest = 11099 # 11961 #value the bot sees when there is a normal chest
tpscroll = 24803 #25007  #what is seen when the item dropped is a tp scroll (on jungle lvl 2)
#11206 is what appears when the daily roulette is disponible.
rarechest = 27106 #28235 #value the bot sees when there is a rare chest (that need lockpicking or keys)
openedrarechest = 26619 # value the bot sees when there is an opened rare chest on tower L1. (after lockpick)
openedrarechest = 26719 # value the bot sees when there is an opened rare chest on old port L1. (after lockpick)
openedrarechest = 26509 # value the bot sees when there is an opened rare chest on old port L1. (after lockpick)
openedrarechest2 = 24884 # value the bot sees when there is an opened rare chest on old port L1. (after lockpick)
openednormalchest = 11360 # value the bot sees when there is an opened normal chest on jungle L2.
negatetokens = 12438 # value the bot sees when asking to confirm tokens use.

class Cord:
    none = (0,0)
    cord_from = (0,0)
    cord_to = (0,0)
    safe_position = (244,747)
    party1 = (725, 248, 773, 316)
    party2 = (719, 319, 775, 384)
    party3 = (722, 389, 776, 452)
    attackparty1 = (513, 161)
    attackparty2 = (511, 222)
    attackparty3 = (511, 302)
    party_down_arrow = (543, 347)
     
    #actions
    q_attack = (660, 449)
    w_defend = (695, 448)
    e_flee = (733, 448)
    r_automata = (769, 455)
    spacebar = (764, 560)
    #buttons outside battle
    b1 = (31, 385)#_west
    b2 = (87, 387)#_north
    b3 = (145, 387)#_south
    b4 = (202, 386)#_east
    b5 = (259, 383)#_monsters
    b6 = (317, 381)#_parties
    b7 = (374, 381)#_rest
    b8 = (426, 386)#_lever
    lookformonsters = (497,517,507,528)#cord for a white box inside the button shaped as a slime
    lookforautomata = (1012,708,1020,716) #cord for a white box inside the automatas button

    #Confirmation required
    yes = (360, 362)
    no = (441, 361)
    #Buttons check
    buttons_check = (246, 490, 725, 546)
    person_check = (539, 500, 575, 536)
    
def leftClick(cord):
    Cord.mouse = get_cords()
    #print 'mouse before =', Cord.mouse
    mousePos(cord)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #print "Click."          #completely optional. But nice for debugging purposes.
    mousePos(Cord.mouse)
    mousePos(Cord.safe_position)
    #print 'mouse after =', Cord.mouse

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(1.0)
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
    #print (x,y)
    return (x,y)

def buttons_check():
    box = (Cord.buttons_check)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'buttons_check=',a
    im.save(os.getcwd() + '\\buttonscheck__' + str(int(time.time())) + '.png', 'PNG')    
    return a
def person_check():
    box = (Cord.person_check)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'person_check=',a
    im.save(os.getcwd() + '\\personcheck__' + str(int(time.time())) + '.png', 'PNG')    
    return a
def check_honor_party1():
    box = (Cord.party1)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'party1_check=',a
    im.save(os.getcwd() + '\\party1check__' + str(int(time.time())) + '.png', 'PNG')    
    return a
def check_honor_party2():
    box = (Cord.party2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'party2_check=',a
    im.save(os.getcwd() + '\\party2check__' + str(int(time.time())) + '.png', 'PNG')    
    return a
def check_honor_party3():
    box = (Cord.party3)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'party3_check=',a
    im.save(os.getcwd() + '\\party3check__' + str(int(time.time())) + '.png', 'PNG')    
    return a
def look_for_automata():
    box = (Cord.lookforautomata)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'look_for_automata=',a
    im.save(os.getcwd() + '\\lookforautomata__' + str(int(time.time())) + '.png', 'PNG')    
    return a
def look_for_battle():
    box = (Cord.lookformonsters)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'look_for_battle=',a
    im.save(os.getcwd() + '\\lookformonsters__' + str(int(time.time())) + '.png', 'PNG')    
    return a
def spacebar():
    #mousePos(Cord.spacebar)
    leftClick(Cord.spacebar)
    print 'Spacebar.'
def farm():
    k = 0 # this means we are wandering through the game, and not inside a battle.
    j = 0
    print "k =", k
    while k==0:
        if at_temple == buttons_check():
            print "leaving temple"
            leftClick(Cord.b4)
        elif at_city == buttons_check():
            print "going to outskirts"
            leftClick(Cord.b6)
        elif at_outskirts == buttons_check():
            print "checking if there is someone in the same square"
            if person1 == person_check() or person2 == person_check():
                print "there is. opening parties screen"
                leftClick(Cord.b6)
            elif noperson == person_check():
                print "noone in this square"
            else:
                print "something went wrong with person check"    
        elif parties == buttons_check():
            print "opened parties screen"
            j=0
            while j<2:
                while loadingparties == check_honor_party1() or stillloading ==check_honor_party1():
                    print "waiting for parties"
                    time.sleep(5)
                if honorparty1 == check_honor_party1():
                    print "chalenging party1"
                    leftClick(Cord.attackparty1)
                    k=1 #this means we are inside a honor battle
                    print "k =", k
                    time.sleep(.1)                
                elif honorparty2 == check_honor_party2():
                    print "chalenging party2"
                    leftClick(Cord.attackparty2)
                    k=1 #this means we are inside a honor battle
                    print "k =", k
                    time.sleep(.1)
                elif honorparty3 == check_honor_party3():
                    leftClick(Cord.attackparty3)
                    print "chalenging party3"
                    k=1 #this means we are inside a honor battle
                    print "k =", k
                    time.sleep(.1)
                else:
                    j=j+1
                    print "j =", j
                    leftClick(Cord.party_down_arrow)
    while k==1:
        while battleready <> look_for_battle():
            print "we are inside the honor fight"
            if automataready < look_for_automata():
                spacebar()
                print "spacebar"
                time.sleep(3)
                k=0
if __name__ == '__main__':
    pass    

