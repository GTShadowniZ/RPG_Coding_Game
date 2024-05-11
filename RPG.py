import random
import colorama
from colorama import Fore
from colorama import Style
import sys
import os
import time
import threading
from threading import Timer
import string
import builtins
import ascii_art
from ascii_art import *


def random_f(y):
    z = random.randrange(0,y)
    return z

def clean():
  os.system('cls' if os.name == 'nt' else 'clear')
#while loop for how many times they want to fight monsters before choosing a path
#if they choose a path => call a fucntion for that spacific road
#if they continue going ahead "while x = 0" and will "x-1" and fight a different scenario each time [random] so 7 or so fight paths

colorama.init(autoreset=True)
Italics = '\033[3m'
# CHECK "Needs Fixing Lines" AND "Important Info" AND "todo_list" FOR MORE INFORMATION #
# GOING TO IMPLEMENT "CLASS" AND "__INIT__" TO CLEAN THIS UP HOWEVER THIS IS A DRAFT WHICH I ALWAYS CHANGE

##               ALLL THE IMPORTANT FUCNTIONS         ##

CL = [  #colorama colour bank
    Fore.RED, Fore.BLUE, Fore.GREEN, Fore.MAGENTA, Fore.CYAN,
    Fore.LIGHTYELLOW_EX, Fore.YELLOW, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX,
    Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX
] #colaroma colours 0-9


def progress_bar(seconds):
  
  for progress in range(0, seconds + 1):
    percent = (progress * 100) // seconds
    
    print("\n")
    print("Loading...")
    print("<" + ("=" * progress) + (" " * (seconds - progress)) + "> " +
          str(percent) + "%")
    print("\n")
    time.sleep(1)
    clean() #progress bar to show up




def cap(input):  #capitalises the words within the string all of them#
  name =  str(string.capwords(input))
  return name


def check_inv(self):
    progress_bar(2)
    clean()
    

#####################################



def equip(self):
        
        
        item_chosen = None
        (item, value) = zip(*self.inv.items())
        

        self.inv_func()
        print(self.equipped)

        while True:
             
            item_chosen = cap(
                input(
                    f"\n{Fore.LIGHTCYAN_EX}Item you wish to equip or {Fore.RED + Style.BRIGHT}EXIT: ")) 


            #"Sword" or "Staff" not in item_chosen
            if "Sword" in item_chosen or "Staff" in item_chosen or "Shield" in item_chosen:#returns if item is not chosen correctly
                
                if self.equipped["Primary"] == []:
                    
                    self.equipped["Primary"].append(item_chosen) #equips the item in primary

                    if "Sword" in item_chosen:
                        self.stat["Damage"] += SWORDS[item_chosen].damage #add the dmg for player
                        break
                    
                    elif "Staff" in item_chosen:
                        self.stat["Spell Damage"] += STAFF[item_chosen].MAGIC_DMG #add mana dmg for player
                        break
                
                else:
                    print("\nMust Dequip first and then equip. So EXIT is recommended.")
                    continue

                if self.equipped["Shield"] == []:
                    
                    if "Shield" in item_chosen:
                        self.stat["Defense"] += SHIELDS[item_chosen]
                        break
                
                else:
                    print("\nMust Dequip first and then equip. So EXIT is recommended.")
                    continue
                
            
            elif item_chosen == "Exit":
                break

            else:
                print("Must be a weapon or Spelt correctly\n")
                clean()
                continue
        
        print(f"{Fore.YELLOW}Successfully added!")
        time.sleep(1.5)
        clean()
        progress_bar(3)
        clean()
        return


            
                 

                 
def dequip(self):
     
        item_chosen = None
        

        self.inv_func()
        print(self.equipped)

        while True:
             
            item_chosen = cap(
                input(
                    f"\n{Fore.LIGHTMAGENTA_EX}Item you wish to dequip or {Fore.RED + Style.BRIGHT} EXIT: ")) 


            #"Sword" or "Staff" not in item_chosen
            if "Sword" in item_chosen or "Staff" in item_chosen or "Shield" in item_chosen:#returns if item is not chosen correctly
                
                if self.equipped["Primary"] != []:
                    
                    self.equipped["Primary"].remove(item_chosen) #equips the item in primary PROBLEM IS HERE AI

                    if "Sword" in item_chosen:
                        self.stat["Damage"] -= SWORDS[item_chosen].damage #add the dmg for player
                        break
                    
                    elif "Staff" in item_chosen:
                        self.stat["Spell Damage"] -= STAFF[item_chosen].MAGIC_DMG #add mana dmg for player
                        break
                    
                    else:
                        print("\nMust equip first and then dequip. So EXIT is recommended.")
                        continue
                
                if self.equipped["Shield"] != []:
                    
                    if "Shield" in item_chosen:
                        self.stat["Defense"] -= SHIELDS[item_chosen]
                        break
                
                else:
                    print("\nMust equip first and then dequip. So EXIT is recommended.")
                    continue

            elif item_chosen == "Exit":
                break

            else:
                print(Fore.RED + Italics + "Must be a weapon or Spelt correctly\n")
                clean()
                continue
        
        print(f"{Fore.YELLOW}Successfully removed!")
        time.sleep(1.5)
        clean()
        progress_bar(3)
        clean()
        return


###                     CLASSIFICATION OF CHARACTER     ###

class player:


    def __init__(self):
        self.name = "Unknown"
        self.equipped = {
            "Primary": [],
            "Shield": [], 
            "Special Ability": [], 
            "Spell": []
            }
        
    
    def player_name(self):
        
        try:
            name = input("What do you want to name yourself Player?\f ")
        except name == ValueError:
            print("Incorrect, Please retry\n")
        self.name = name

    def stat_func(self):

        x = random_f(len(CL))
        y = random_f(len(CL))

        colour_1 = CL[x]
        colour_2 = CL[y]


        i1, i2 = zip(*self.stat.items())
        for z in range(len(i1)):
            print(colour_1 + i1[z], ":" , colour_2 + str(i2[z]))
        return None

    def inv_func(self):
        
        x = random_f(len(CL))
        y = random_f(len(CL))

        colour_1 = CL[x]
        colour_2 = CL[y]

        i1, i2 = zip(*self.inv.items())
        for z in range(len(i1)):
            print(colour_1 + i1[z], ":", colour_2 + str(i2[z]))
        return None





class character(player):
        
        def __init__(self):
            super().__init__()
            
            #the exp => take inputs [class] if the exp and level and check to lvl up
            self.exp = 0 #current exp
            self.lvl = 0
            self.hp = 100
            self.mana = 100
            


class swordsman(character):
        
        def __init__(self):
            super().__init__()
            
            self.inv = { #item and quantity
                        "Wooden Sword": 1,
                        "Wooden Shield": 1, 
                        "Bread": 5,
                        "Sphinx": 30 #money
                        }
            
            
            self.stat = {"Hunger": 10, #how long they are going to last
                         "Damage": 7, #sword damage or punching dmg
                         "Defense": 5, #how much they can deflect the attack
                         "Speed": 4, #speed reaction
                         "Health": 15, #
                         "Spell Damage": 5,
                         "Staff Damage": 4}
 
class magician(character):
        
        def __init__(self):
            super().__init__()
            
            self.mana = 150
            self.inv = { #item and quantity
                        "Magic Staff": 1, 
                        "Healing Potion": 1, 
                        "Bread": 5,
                        "Sphinx": 30 #money
                        }
            
            self.stat = {#stats
                        "Hunger": 10,
                         "Damage": 3,
                         "Defense": 4,
                         "Speed": 3,
                         "Health": 10,
                         "Spell Damage": 10}


class EXP_Lvl:

    def __init__(self, lvl, exp, money):
        
        self.LEVEL = lvl
        self.EXP = exp
        self.MONEY = money



#This needs to be in sub class such that it contains rewards as well 
#this has to be an iteration which checks for level and exp current if it is above what it is, lvels up
Levelling_EXP = {
    "1": EXP_Lvl(1, 100, 40),
    "2": EXP_Lvl(2, 250, 50),
    "3": EXP_Lvl(3, 350, 70),
    "4": EXP_Lvl(4, 450, 70),
    "5": EXP_Lvl(5, 600, 80)

}

        
    
  
###                     CLASSIFICIATIONN FOR SPELLS
class Spell:
        
        def __init__(self,damage, mana):
            self.damage = damage
            self.MANA_INTAKE = mana

  
        def __str__(self): #outputs the  spell information when called upon
            return (
                f"Damage: {Fore.LIGHTRED_EX+ self.damage}\n"
                f"Mana Intake: {Fore.LIGHTYELLOW_EX + self.mana_intake}\n")
    
class Burn(Spell): #initialises burn damage to fire-based spells
        
        def __init__(self, damage, mana):
            super().__init__(damage, mana)
            self.burn = 10

class Stun(Spell):#initialises stun [inability to attack back] to spells
        
        def __init__(self, damage, mana):
            super().__init__(damage, mana)
            self.STUN = True


# Create a dictionary to store all the spells in the game
SPELLS = {
    "Fire Ball": Burn(6, 10),
    "Water Splash": Spell(6, 10),
    "Lightning bolt": Stun(6, 10),
    "Wind Flush": Spell(6, 10),
    "Sand Cloud": Stun(7, 11),
    "Earth Swallow": Stun(9, 12),
    "Ice Burg": Spell(10, 14),
    "Ice Mantle": Spell(14, 15),
    "Bomb Rush": Burn(15, 20),
    "Lava Pool": Burn(17, 20),
}

SHIELDS = {
    "Wooden Shield": 5,
    "Iron Shield": 7,
    "Gold Shield": 14,
    "Diamond Shield": 17,
    "Mithril Shield": 20,
    "Adamant Shield": 25,
    "Rune Shield": 30,
}
#####                         WEAPONS

        
class staff:
    
    def __init__(self,name, magic_dmg, ability=[], maximum_mana=0, cost=0, picture=None):
        
        self.NAME = name
        self.MAGIC_DMG = magic_dmg
        self.ABILITIES = ability
        self.MAX_MANA = maximum_mana
        self.COST = cost
        self.PICTURE = picture

STAFF = {  #staff name, normal spell damage, ability [2 extra], total mana increase capacity, cost
    'Magic Staff' : staff('Magic Staff', 5,["Water Splash"], 0, 0),
    'Celestial Staff': staff('Celestial Staff', 7,["Fire Ball"], 40, 10),
    'Holy Light Staff' : staff('Holy Light Staff', 9,["Lightning bolt"], 60, 15),
    'Defender of the Burning Sun' : staff('Defender of the Burning Sun', 15, ["Lava Pool"], 90, 25),
    'Ancient Spirit Staff' : staff('Ancient Spirit Staff', 15, ["Ice Mantle"], 80, 25),
    'Moonshadow': staff('Moonshadow', 22, [], 90, 26), #thinking for special ability
    'Boon of Executions': staff('Boon of Executions', 27, [], 110, 28)#thinking for special ability
}

class sword:
    
    def __init__(self, name, dmg, ability, ability_dmg=[], cost=0):
        
        self.NAME = name
        self.damage = dmg
        self.ABILITY = ability
        self.ability_dmg = ability_dmg
        self.COST = cost

SWORDS = { #name of swords with its corresponding abilities and dmg
    'Wooden Sword': sword('Wooden Sword', 5, None, None, 5),
    'Dawnbreaker': sword('Dawnbreaker', 7, None, None, 8),
    'Fancy Obsidian Claymore': sword('Fancy Obsidian Claymore', 14, 'Knockout', 30, 15),
    'Mithril Sword': sword('Mithril Sword', 17, 'Slashing', 20, 15),
    'Adamant Sword': sword('Adamant Sword', 20, 'Heavenly Splitter', 40, 35),
    'Rune Sword': sword('Rune Sword', 22, 'Calamity', 40, 40)
}


###                          POTIONS
class POTION:
    def __init__(self, name, effect, cost):
        self.NAME = name
        self.EFFECT = effect #in other words, damage
        self.COST = cost #the cost from markets


class POTION_1(POTION):
    def __init__(self, name, effect, cost):
        super().__init__(name, effect, cost)
        self.DURATION = 3 #how many rounds should this last for


class POTION_2(POTION):
    def __init__(self, name, effect, cost):
        super().__init__(name, effect, cost)
        self.DURATION = 6 #how many rounds should this last for



POTION_LVL_1 = {
    'Healing Potion 1': POTION_1('Healing Potion 1', 5, 2),
    'Poison Potion 1': POTION_1('Poison Potion 1', -5, 4),
    'Strength Potion 1': POTION_1('Stregth Potion 1', 10, 5),
    'Resistant Potion 1': POTION_1('Resistance Potion 1', 13, 8),
    'Burning Potion 1': POTION_1('Burning Potion 1', 15, 12)
}

POTION_LVL_2 = {
    'Healing Potion 2': POTION_2('Healing Potion 2', 10, 4),
    'Poison Potion 2': POTION_2('Poison Potion 2', -10, 8),
    'Strength Potion 2': POTION_2('Stregth Potion 2', 20, 10),
    'Resistant Potion 2': POTION_2('Resistance Potion 2', 20, 10),
    'Burning Potion 2': POTION_2('Burning Potion 2', 25, 20)
}








player = swordsman()


equip(player)