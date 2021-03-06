#RPG_TEST
#Dennis Gordick
#10/21/2014
"""
Task list:
fix bug where you can sell potions you don't have
allow player to leave battle
make battles more difficult
create different types of monsters
create a limit to the cave
add bosses
improve shop inventory
gain skill points every level to improve yourself
"""

import random
import time
import pickle, shelve

response=input("New game or Load game? (Choose load or new)")
while response != "load" and response != "new":
	print(response + " is invalid input")
	response=input("New game or Load game? (Choose load or new)")

if response == "load":
	try:
		f = shelve.open("save.dat")
		attributes = f["attributes"]
		f.close()
		Name = attributes["Name"]
		Race = attributes["Race"]
		Class = attributes["Class"]
		Weapon = attributes["Weapon"]
		xp = attributes["xp"]
		player_lvl = attributes["player_lvl"]
		gold = attributes["gold"]
		potions = attributes["potions"]
	except:
		print("Save file is corrupt or doesn't exist")
		response="new"
if response=="new":
	Name=input("What is your name?")
	Race=input("What is your race? (Your choices are Human, Elf, and Dwarf.)")
	Class=input("What is your class? (Your choices are Warrior, Archer, and Mage.")
	if Class=="Warrior":
	    Weapon="Sword"
	    print("A "+Weapon+" is your weapon")
	elif Class=="Archer":
	    Weapon="Bow"
	    print("A "+Weapon+" is your weapon")
	else:
	    Weapon="Staff"
	    print("A "+Weapon+" is your weapon")


if Class=="Warrior":
    Weapon="Sword"
    print("A "+Weapon+" is your weapon")
elif Class=="Archer":
    Weapon="Bow"
    print("A "+Weapon+" is your weapon")
else:
    Weapon="Staff"
    print("A "+Weapon+" is your weapon")

print("The "+str(Weapon)+" weilding "+ str(Class)+" of the "+ str(Race)+" clan, whent out on an adventure. There name was "+str(Name))

xp=0
player_lvl=1
extra_health=int(player_lvl)*10
health=90+int(extra_health)
gold=0
potions=0

kill=0
boss_kill=0

while health > 0:

    extra_health=int(player_lvl)*10
    health=90+int(extra_health)
    LVL_XP=90+int(extra_health)

    if int(xp) >= int(LVL_XP):
        player_lvl+= 1
        print("Level Up! "+str(player_lvl))

    player_dmg_min=0+int(player_lvl)
    player_dmg_max=7+int(player_lvl)

    explore=input("Do you want to explore or go to town or look at some stats/info or even save? (only say explore or town or info or save)")
    turns=1
    if explore=="explore":
        lvl=input("What level monsters?")
        if lvl.isdigit():
            print("You explore")
            turns=1
            while turns < 100 and int(health) > 0:

                monster_lvl= int(lvl)
                monster_dmg= int(lvl)
                monster_xp= int(lvl)/int(player_lvl)*2
                monster_loot= int(monster_lvl)

                encounter=random.randint(1,100)
                drop_lvl=int(lvl)

                #normal fight
                if int(encounter) >=70:
                    print("You encounterd a LVL: "+str(monster_lvl)+" Monster!")
                    monster_health=int(monster_lvl)*2
                    while int(monster_health) > 0 and health > 0:
                        print("Your Health: "+str(health))
                        print("Monsters Health: "+str(monster_health))

                        #Actual combat
                        attack=input("Do you attack or use a potion or run? (attack or potion or run)")
                        
                        if attack == "attack":
                              hit=random.randint(1,100)
                              if int(hit)<=75:
                                  dmg=random.randint(int(player_dmg_min),int(player_dmg_max))
                                  monster_health=int(monster_health)-int(dmg)
                                  print("\nYou did "+ str(dmg)+" damage")
                              else:
                                    print("You missed!")
                        elif attack=="potion":
                            if potions >0:
                                health=90+int(extra_health)
                                print("Potions left... "+str(potions))
                            else:
                                print("You have no potions... You just waisted your turn!")

                        else:
                            print("You sit there and take it")
                        monster_hit_chance=random.randint(1,100)
                        if int(monster_hit_chance)<=60:
                            health=int(health)-int(monster_dmg)
                            print("The monster did "+ str(monster_dmg)+" damage")
                        else:
                            print("The monster missed!")

                        #loot and xp for normal monster
                        if int(monster_health) <= 0:
                              xp= int(xp)+int(monster_xp)
                              print("\nThe monster died\n")
                              print("XP gained: "+ str(monster_xp))
                              print("Your XP: "+ str(xp))
                              loot_chance=random.randint(1,100)

                              if int(loot_chance) <10:
                                  print("No loot :(")
                                  print("Your gold "+str(gold))
                              elif int(loot_chance) <70:
                                  print("Your gold sir. It this many..." +str(monster_loot))
                                  gold=int(gold)+int(monster_loot)
                                  print("Your gold "+str(gold))
                              elif int(loot_chance) <90:
                                  print("Rare loot! 1 potoin!")
                                  potions+=1
                                  print("\nYour total potions "+str(potions))

                              kill+=1

                        elif int(health) <= 0:
                              print("You died")

                elif int(encounter)<70:

                    loot=random.randint(1,100)
                    trap=random.randint(1,100)

                    if int(loot)>=60:
                        gold=int(gold)+int(lvl)
                        print("You found "+str(lvl)+" gold")
                        print("You now have a total of "+str(gold)+" gold")
                    elif int(loot)<=10:

                        if int(trap)>=50:

                            health=int(health)-10
                            print("You step on a trap")
                            print("You lost ten health")
                            print("Your total health is "+str(health))

                if int(turns)== 100:

                     #Boss fight

                     boss=random.randint(1,10)

                     if int(boss)>5:

                         print("Boss Fight!")
                         boss_health=int(health)
                         boss_xp=int(monster_xp)*3
                         boss_dmg=int(lvl)*3
                         boss_loot=int(lvl)*100
                         run=input("Do you fight or run?")

                         while int(boss_health)>0 and int(health) > 0 and run=="fight":

                            print("Your Health: "+str(health))
                            print("Boss Health: "+str(boss_health))
                            attack=input("Do you attack or use a potion? (attack or potion)")

                            if attack == "attack":

                                    hit=random.randint(1,100)

                                    if int(hit)<=75:

                                        dmg=random.randint(int(player_dmg_min),int(player_dmg_max))
                                        boss_health=int(boss_health)-int(dmg)
                                        print("\nYou did "+ str(dmg)+" damage")

                                    else:

                                        print("You missed!")

                            elif attack=="potion":

                                if potions >0:

                                    health=90+int(extra_health)
                                    print("Potions left... "+str(potions))

                                else:

                                    print("You have no potions... You just waisted your turn!")

                            else:

                                print("You sit there and take it")

                            boss_hit_chance=random.randint(1,100)

                            if int(boss_hit_chance)<=60:

                                health=int(health)-int(boss_dmg)
                                print("The boss did "+ str(boss_dmg)+" damage")

                            else:
                                print("The boss missed!")

                            if int(boss_health) <= 0:

                                xp= int(xp)+int(boss_xp)
                                print("\nThe boss died\n")
                                print("XP gained: "+ str(boss_xp))
                                print("Your XP: "+ str(xp))
                                loot_chance=random.randint(1,100)

                                if int(loot_chance) <10:

                                    print("No loot :(")
                                    print("Your gold "+str(gold))

                            elif int(loot_chance) <90:

                                    print("Your gold sir. It this many..." +str(boss_loot))
                                    gold=int(gold)+int(boss_loot)
                                    print("Your gold "+str(gold))

                            elif int(health) <= 0:

                                print("You died")

                            else:

                                    print("Rare loot! 10 potoin!")
                                    potions+=10
                                    print("\nYour total potions "+str(potions))

                            boss_kill+=1
                                
                
                print("End of turn "+ str(turns)+"\n")
                turns+=1
                time.sleep(1.0)
        else:
            print("That isnt a lvl... your just not going to explore...")

    elif explore=="info":
        print("Total kills",str(kill))
        print("Total boss kills",str(boss_kill))
    #Going to town (giggity)

    elif explore=="town":
        town=input("Where do you want to go in town? (shop, inspector, blacksmith, tavern)")

        if town=="shop":
            print("Your gold "+str(gold))
            print("The shopkeep says 'We only have potions of health! They are 20 gold each!'")
            shop=input("How many do you want?")
            cost=int(shop)*20

            if int(gold)>=int(cost):
                potions=int(potions)+int(shop)
                gold=int(gold)-int(cost)
                print("Gold left "+str(gold))
                print("Total potoins "+str(potions))

            else:
                print("'Your to poor! Come back with some gold fool!'\nThe shopkeeper kicks you out.")

        elif town=="inspector":
            print("Comeing soon")

        elif town=="blacksmith":
            print("Comeing soon")

        elif town=="tavern":

            print("Hello traveler, what can I do for you? A drink? Or the lates rumore?")
            bar_keep=input("Whats your choice? (drink, rumore, or leave)")

            if bar_keep=="drink":
                print("Drinks cost one gold.")
                drink=input("Do you want a drink?")

                if drink=="yes" and gold > 0:
                    gold=int(gold)-1
                    print("Your gold: "+str(gold))
                    print("You get drunk out of your mind.")

                else:
                    print("Goodbye")

    elif explore=="save":
	    #do you want extra_health or health saved?
	    f = shelve.open("save.dat")
	    attributes = {"Name":Name,"Race":Race,"Class":Class,"Weapon":Weapon,"xp":xp,"player_lvl":player_lvl,"gold":gold, "potions":potions}
	    f["attributes"] = attributes
	    f.sync()
	    f.close()
	    print("Game saved")
