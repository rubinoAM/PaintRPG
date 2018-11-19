import os
import random

player = {
    "Name":"",
    "Health":100,
    "Power":50
}

canvas = {
    "Health":60,
    "Power":20
}

min_roll = 1
max_roll = 6
roll_it = False

print ("""
            :
   `.       ;        .'
     `.  .-'''-.   .'
       ;'  __   _;'
      /   '_    _`\`
     |  _( a (  a  |
'''''| (_)    >    |``````
      \    \    / /
       `.   `--'.'
      .' `-,,,-' `.
    .'      :      `.  
            :

> Howdy there! I'm the sun, but my friends call me Al, and you can too.
> Welcome to Paint Attack!
> You're a just humble artist who recently has been struck with a bad case of artist's block.
> But today's the day you finally fight back and create another masterpiece.
> The object of the game is to work on your piece (i.e. fight your canvas) until it's completed.
""")

player_name = input("> Soooooooo... what's your name? ")
player['Name'] = player_name.capitalize()

print ("""
            :
   `.       ;        .'
     `.  .-'''-.   .'
       ;'  __   _;'
      /   '       `\`
     |  _( O (  O  |
'''''| (_)  __>__  |``````
      \    \    / /
       `.   `--'.'
      .' `-,,,-' `.
    .'      :      `.  
            :
""")
print ("> Well alrighty, %s! Let's get a move on!" % player['Name'])
print ("> On thine travels through the kingdom, thou should happen upon a canvas.")

def fight():
    print ("Godspeed you, oh brave %s!" % player['Name'])

    player_health = 10
    player_power = 5
    canvas_health = 6
    canvas_power = 2

    fool_hardy = False

    while player_health > 0 and canvas_health > 0:
        if(not fool_hardy):
            print ("You have %d health and %d power." % (player_health, player_power))
            print ("The canvas has %d health and %d power." % (canvas_health, canvas_power))
            print ("What shalt thou do? \n1.Fight\n2.Flee\n3.Dance")

        choice = int(input("> "))

        if choice not in range(1,4):
            print ("To the beasts with this asinine foolishness! Thou must choose!\n1.Fight\n2.Flee\n3.Dance")
            fool_hardy = True
        else:
            fool_hardy = False
            if choice == 1:
                canvas_health -= player_power
                print ("You have done %d damage to the canvas!" % player_power)
            elif choice == 2:
                print ("Goodbye, %s... you cowardly sod!" % player['Name'])
                break;
            elif choice == 3:
                player_health += 3
                print ("The canvas stares dazed and confused at your spontaneous dancing.\nHis delayed assault allows you time to regain 3 health points.")
                print ("Your health is now at %d points." % player_health)

        if canvas_health >= 0:
            player_health -= canvas_power
            print ("The canvas hits you for %d damage" % canvas_power)
            if player_health <= 0:
                print ("Thou hast been slain.")
        else:
            os.system("say Huzzah!")
            print ("Huzzah! The canvas hast been slain!")

        input("Please press enter to continue.")
        os.system("clear")
fight()