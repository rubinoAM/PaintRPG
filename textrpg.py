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
print ("On thine travels through the kingdom, thou happen upon a giant.")
print ("What shalt thou do? \n1.Fight\n2.Flee\n3.Dance")

choice = int(input(">"))

def fight():
    print ("Godspeed you, oh brave %s!" % hero['Name'])

    hero_health = 10 # Only accessible inside of fight() since they're only in the function scope
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    while hero_health > 0 and goblin_health > 0:
        print ("You have %d health and %d power." % (hero_health, hero_power))
        print ("The goblin has %d health and %d power." % (goblin_health, goblin_power))
        print ("What shalt thou do? \n1.Fight\n2.Flee\n3.Dance")

        choice = int(input(">"))


def flee():
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
    choice = int(input(">"))