import os
# os.system() Takes any linux command. If python can run it, it will.

hero = {    # Global, meaning anyone can see it
    "Name":"",
    "Health":100,
    "Power":50
}

goblin = {
    "Health":60,
    "Power":20
}

player_name = input("Pray thee. What is thine name, oh brave adventurer? > ")
hero['Name'] = player_name.capitalize()

print ("Good day to you, valiant %s! May thine conquest be bountiful and may thine travels be safe." % hero['Name'])
print ("On thine travels through the kingdom, thou should happen upon a goblin.")

def fight():
    print ("Godspeed you, oh brave %s!" % hero['Name'])

    hero_health = 10 # Only accessible inside of fight() since they're only in the function scope
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    fool_hardy = False

    while hero_health > 0 and goblin_health > 0:
        if(not fool_hardy):
            print ("You have %d health and %d power." % (hero_health, hero_power))
            print ("The goblin has %d health and %d power." % (goblin_health, goblin_power))
            print ("What shalt thou do? \n1.Fight\n2.Flee\n3.Dance")

        choice = int(input("> "))

        if choice not in range(1,4):
            print ("To the beasts with this asinine foolishness! Thou must choose!\n1.Fight\n2.Flee\n3.Dance")
            fool_hardy = True
        else:
            fool_hardy = False
            if choice == 1:
                goblin_health -= hero_power
                print ("You have done %d damage to the goblin!" % hero_power)
            elif choice == 2:
                print ("Goodbye, %s... you cowardly sod!" % hero['Name'])
                break;
            elif choice == 3:
                hero_health += 3
                print ("The goblin stares dazed and confused at your spontaneous dancing.\nHis delayed assault allows you time to regain 3 health points.")
                print ("Your health is now at %d points." % hero_health)

        if goblin_health >= 0:
            hero_health -= goblin_power
            print ("The goblin hits you for %d damage" % goblin_power)
            if hero_health <= 0:
                print ("Thou hast been slain.")
        else:
            os.system("say Huzzah!")
            print ("Huzzah! The goblin hast been slain!")

        input("Please press enter to continue.")
        os.system("clear")
fight()

""" def flee():
    print ("Goodbye, coward!")

def dance():
    print ("Do the hussle!")

if(choice == 1):
    fight()
elif(choice == 2):
    flee()
elif(choice == 3):
    dance()
else:
    print ("That's not a choice! Pick an actual option!\n1.Fight\n2.Flee\n3.Dance")
    choice = int(input("> ")) """