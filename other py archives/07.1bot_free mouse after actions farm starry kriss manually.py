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
    cord_from = (0,0)
    cord_to = (0,0)
     
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
    spacebar = (764, 560)
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
    r_use_tokens = (396, 162) #beware when using this coordinates on the code. They were not banned because are needed for leaving an unopened chest.
    r_leave_chest = (396, 185)
    openeditem = (421,209)
    openeditem2 = (420,208)
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

    
def leftClick(cord):
    Cord.mouse = get_cords()
    print 'mouse before =', Cord.mouse
    mousePos(cord)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #print "Click."          #completely optional. But nice for debugging purposes.
    mousePos(Cord.mouse)
    print 'mouse after =', Cord.mouse

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

def grabitem(cord):
    mousePos(Cord.openeditem)
    leftDown()
    mousePos(Cord.openeditem2)
    time.sleep(1.0)
    mousePos(cord)
    leftUp() 
   
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,y)
    return (x,y)

def get_hp1():
    box = (Cord.hp1)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'hp1=',a
    #im.save(os.getcwd() + '\\hp1__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_hp2():
    box = (Cord.hp2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'hp2=',a
    #im.save(os.getcwd() + '\\hp2__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_hp3():
    box = (Cord.hp3)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'hp3=',a
    #im.save(os.getcwd() + '\\hp3__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_hp4():
    box = (Cord.hp4)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'hp4=',a
    #im.save(os.getcwd() + '\\hp4__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_hp5():
    box = (Cord.hp5)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'hp5=',a
    #im.save(os.getcwd() + '\\hp5__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_hp6():
    box = (Cord.hp6)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'hp6=',a
    #im.save(os.getcwd() + '\\hp6__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_hp7():
    box = (Cord.hp7)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'hp7=',a
    #im.save(os.getcwd() + '\\hp7__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana1():
    box = (Cord.mana1)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'mana1=',a
    #im.save(os.getcwd() + '\\mana1__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana2():
    box = (Cord.mana2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'mana2=',a
    #im.save(os.getcwd() + '\\mana2__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana3():
    box = (Cord.mana3)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'mana3=',a
    #im.save(os.getcwd() + '\\mana3__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana4():
    box = (Cord.mana4)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'mana4=',a
    #im.save(os.getcwd() + '\\mana4__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana5():
    box = (Cord.mana5)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'mana5=',a
    #im.save(os.getcwd() + '\\mana5__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana6():
    box = (Cord.mana6)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'mana6=',a
    #im.save(os.getcwd() + '\\mana6__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_mana7():
    box = (Cord.mana7)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'mana7=',a
    #im.save(os.getcwd() + '\\mana7__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_all_mana():
    #get_hp1()
    #get_hp2()
    #get_hp3()
    #get_hp4()
    #get_hp5()
    #get_hp6()
    #get_hp7()
    get_mana1()
    get_mana2()
    get_mana3()
    get_mana4()
    get_mana5()
    get_mana6()
    get_mana7()

def get_chest():
    box = (Cord.lookforchest)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print 'chest=',a
    im.save(os.getcwd() + '\\chest__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def revive1():
    #mousePos(Cord.char5)
    leftClick(Cord.char5)
    #mousePos(Cord.skill7)
    leftClick(Cord.skill4)
    #mousePos(Cord.char1)
    leftClick(Cord.char1)
def revive2():
    #mousePos(Cord.char5)
    leftClick(Cord.char5)
    #mousePos(Cord.skill7)
    leftClick(Cord.skill4)
    #mousePos(Cord.char2)
    leftClick(Cord.char2)
def revive3():
    #mousePos(Cord.char5)
    leftClick(Cord.char5)
    #mousePos(Cord.skill7)
    leftClick(Cord.skill4)
    #mousePos(Cord.char3)
    leftClick(Cord.char3)
def revive4():
    #mousePos(Cord.char5)
    leftClick(Cord.char5)
    #mousePos(Cord.skill7)
    leftClick(Cord.skill4)
    #mousePos(Cord.char4)
    leftClick(Cord.char4)
def revive5(): #this is the healer. So this is diferent to cast miracle.
    #mousePos(Cord.char2)
    leftClick(Cord.char2)
    #mousePos(Cord.skill5)
    leftClick(Cord.skill5)
def revive6():
    #mousePos(Cord.char5)
    leftClick(Cord.char5)
    #mousePos(Cord.skill7)
    leftClick(Cord.skill4)
    #mousePos(Cord.char6)
    leftClick(Cord.char6)
def revive7():
    #mousePos(Cord.char5)
    leftClick(Cord.char5)
    #mousePos(Cord.skill7)
    leftClick(Cord.skill4)
    #mousePos(Cord.char7)
    leftClick(Cord.char7)
    
def heal_all():
    #mousePos(Cord.char5)
    leftClick(Cord.char5)
    #mousePos(Cord.skill2)
    leftClick(Cord.skill2)
    time.sleep(7)
    
def spacebar():
    #mousePos(Cord.spacebar)
    leftClick(Cord.spacebar)
    print 'Spacebar.'
    
def look_for_battle():
    box = (Cord.lookformonsters)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print 'look_for_battle=',a
    #im.save(os.getcwd() + '\\lookformonsters__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def look_for_automata():
    box = (Cord.lookforautomata)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print 'look_for_automata=',a
    #im.save(os.getcwd() + '\\lookforautomata__' + str(int(time.time())) + '.png', 'PNG')    
    return a
def look_for_chest():
    box = (Cord.lookforchest)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print 'look_for_chest=',a
    #im.save(os.getcwd() + '\\lookforchset__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def check_healing():       
    #check if a character is dead
    if needrevive > get_hp5():
        print 'Reviving character 5. This is the Healer.' #have priority, so comes first.
        revive5()
    
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
    
    if needrevive > get_hp6():
        print 'Reviving character 6'
        revive6()
    
    if needrevive > get_hp7():
        print 'Reviving character 7'
        revive7()
    else:
        print 'Noone need revive'

    #Check if someone needs heal
    if needheal < get_hp1():
        print 'Character 1 need heal.'
        heal_all()
    if needheal < get_hp2():
        print 'Character 2 need heal.'
        heal_all()
    if needheal < get_hp3():
        print 'Character 3 need heal.'
        heal_all()
    if needheal < get_hp4():
        print 'Character 4 need heal.'
        heal_all()
    if needheal < get_hp5():
        print 'Character 5 need heal.'
        heal_all()
    if needheal < get_hp6():
        print 'Character 6 need heal.'
        heal_all()
    if needheal < get_hp7():
        print 'Character 7 need heal.'
        heal_all()
def rest():
    #location search for rest
    #mousePos((Cord.b7_rest))
    leftClick(Cord.b7_rest)
    print 'Rest.'
    time.sleep(5.0)
    
def startGame():
    #check if inside a battle
    if automataready < look_for_automata():
        spacebar()
        time.sleep(8)
        #mousePos(Cord.none)
    
    #check if is outside a battle
    if battleready == look_for_battle():
        check_healing()
    #check if rest is needed
        if needmana > get_mana1():
            rest()
        if needmana > get_mana2():
            rest()
        if needmana > get_mana3():
            rest()
        if needmana > get_mana4():
            rest()
        if needmana > get_mana5():
            rest()
        if needmana > get_mana6():
            rest()
        if needmana > get_mana7():
            rest() 
    #location search for monsters button
        #mousePos((Cord.b5_monsters))
        leftClick(Cord.b5_monsters)
        print 'Look for monsters.'
        time.sleep(1.5)
    #check if there is a normal chest
    if normalchest == look_for_chest():
        #mousePos(Cord.n_chest)
        leftClick(Cord.n_chest)
        print 'Open normal chest.'
        time.sleep(5.0)
        #mousePos(Cord.n_open_chest)
        leftClick(Cord.n_open_chest)
        print 'Discard normal chest.'
        time.sleep(5.0)
        #mousePos(Cord.yes)
        leftClick(Cord.yes)
        print 'Confirm discard normal chest, after opening it.'
        time.sleep(1.0)
    #check if there is a rare chest
    if rarechest == look_for_chest():
        #mousePos(Cord.r_lockpick)
        leftClick(Cord.none)#r_lockpick)
        #mousePos(Cord.yes)
        #leftClick(Cord.yes)
        print 'Try to lockpick rare chest.'
        time.sleep(5.0)
        #check if failed on lockpick
        if rarechest == look_for_chest():
            #mousePos(Cord.r_use_tokens) #after failing lockpick atempt, the "leave chest" button comes to position 3 on clickable choices
            leftClick(Cord.none)#r_use_tokens)#after failing lockpick atempt, the "leave chest" button comes to position 3 on clickable choices
            time.sleep(5.0)
            #mousePos(Cord.no) #just to be sure we'll not spend tokens accidentaly, instead of leaving chest.
            leftClick(Cord.no) #just to be sure we'll not spend tokens accidentaly, instead of leaving chest.
            time.sleep(5.0)
            print 'Discarding locked chest, after failed lockpick attempt.'
    #check if the chest was opened
    if openedrarechest == look_for_chest():
        grabitem(Cord.char1)
        print 'Trying to drag item to character 1.'
    if openedrarechest == look_for_chest():
        grabitem(Cord.char2)
        print 'Character 1 has a full bag. Trying to drag to character 2'
    if openedrarechest == look_for_chest():
        grabitem(Cord.char3)
        print 'Character 2 also has a full bag. Trying to drag to character 3'
    if openedrarechest == look_for_chest():
        grabitem(Cord.char4)
        print 'Another full bag. Next. Character 4.'
    if openedrarechest == look_for_chest():
        grabitem(Cord.char5)
        print 'Front line all full. Giving item to Character 5.'
    if openedrarechest == look_for_chest():
        grabitem(Cord.char6)
        print 'Char 5 is already full. This was expected, since he is the healer. Giving item to Character 6.'
    if openedrarechest == look_for_chest():
        grabitem(Cord.char7)
        print 'Almost full. Just character 7 have space.'
    if openedrarechest == look_for_chest():
        print ' Oh boy, nevermind. Everybody is full. Human intervention needed here.'

    
def main():
    k=0
    while (k < 50000000):
        #print 'k = ',k
        startGame()
        k=k+1
        
                
if __name__ == '__main__':
    pass    

