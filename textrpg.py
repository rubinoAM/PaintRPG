# Preliminary Declarations
import os
import random
from player import Player
from canvas import Canvas
from secretboss import Secret_Boss
from mrsun import Mr_Sun

player = Player("")
canvas = Canvas()
secret_boss = Secret_Boss()
al = Mr_Sun()

min_roll = 1
max_roll = 6
roll_it = False
enable_secret = False

# Game Begins
al.cool_face()
print ("""
> Howdy there! I'm the sun, but my friends call me Al, and you can too.
> Welcome to Paint Attack!
> You're a just humble artist who recently has been struck with a bad case of artist's block.
> But today's the day you finally fight back and create another masterpiece.
> The object of the game is to work on your piece (i.e. fight your canvas) until it's completed.
""")

player_name = input("> Soooooooo... what's your name? ")
player.name = player_name.capitalize()

al.happy_face()
print ("> Well alrighty, %s! Let's get a move on!" % player.name)
print ("> Saturday is the day for me. Not a cloud in sight!")

def play():
    print ("> It's game time, %s!" % player.name)

    wont_play = False
    jerk_pts = 0

    while player.health > 0 and canvas.health > 0:
        if(not wont_play):
            print ("> You have %d energy and can get %d work done right now." % (player.health, player.power))
            print ("> The canvas needs %d more work and will drain %d energy." % (canvas.health, canvas.power))
            print ("> What'll you do? \n1.Paint\n2.Procrastinate\n3.Thumbnail")

        choice = int(input("> "))

        if choice not in range(1,4):
            if jerk_pts < 3:
                jerk_pts += 1
                al.angry_face()
                print ("> Don't be a jerk! Pick something! \n1.Paint\n2.Procrastinate\n3.Thumbnail")
            else:
                os.system("clear")
                os.system("say DIE!")
                al.die_face()
                print ("Well unfortunately you're dead now.\nGood job aggravating the sun, idiot!")
                break
            wont_play = True   
        else:
            wont_play = False
            if choice == 1:
                canvas.health -= player.power
                print ("You've made %d progress on your artwork!" % player.power)
            elif choice == 2:
                roll_it = True
                while roll_it:
                    roll_res = random.randint(min_roll,max_roll)
                    roll_crit = random.randint(min_roll,max_roll)
                    if roll_res == roll_crit:
                        player.laziness = 0
                        player.health += 80
                        print ("Amazingly your procrastination led to some inspiration!")
                        print ("You've regained 80 points of energy.\nYou're now at %d energy points." % player.health)
                        roll_it = False
                    else:
                        player.laziness += 10
                        print ("Nothing was accomplished... but you feel a little better.")
                        roll_it = False
            elif choice == 3:
                player.health += 50
                print ("Thumbnailing the ideas you had in your head has helped your resolve.\nYou've regained 30 energy through your problem solving.")
                print ("Your energy is now at %d points." % player.health)
        if wont_play == False:
            if canvas.health >= 0:
                player.health -= canvas.power
                print ("Time has passed.\nYou feel a bit more tired. You've lost %d energy points." % canvas.power)
                if player.health <= 0:
                    os.system("clear")
                    al.sad_face()
                    print ("> You're all out of energy and with no finished piece to show for it.")
                    print ("> Better luck next time!")
                    break
                elif player.laziness == 30:
                    os.system("clear")
                    al.exasperated_face()
                    print ("> Your laziness has gotten the better of you and you've given up for today.")
                    print ("> Smooooooooth.")
                    break
            else:
                os.system("clear")
                al.ecstatic_face()
                os.system("say Yay!")
                print ("> Yay! Your masterpiece is finally completed!")
                print ("> You feel a tremendous wave of confidence overcome you as you marvel at the finished piece.")
                roll_it = True
                while roll_it:
                    roll_one = random.randint(min_roll,max_roll)
                    roll_two = random.randint(min_roll,max_roll)
                    roll_three = random.randint(min_roll,max_roll)
                    roll_total =  roll_one + roll_two + roll_three

                    if roll_total > 14:
                        enable_secret = True
                        break
                    else:
                        break

            input("Please press enter to continue.")
            os.system("clear")

def boss_fight():
    os.system("clear")
    secret_boss.printImage()
    print ("> Suddenly a wizard appeared!")
    print ("> Why is there a wizard?! Who knows?! I dunno!!\n You still gotta fight him!!")

    while player.health > 0 and secret_boss.health > 0:
        print ("What will you do? 1. Attack 2. Wait 3. Heal")
        choice = int(input("> "))

        if choice == 1:
            canvas.health -= player.power
            print ("You attacked the wizard for %d damage!" % player.power)
        elif choice == 2 or choice not in range(1,4):
            roll_it = True
            while roll_it:
                roll_res = random.randint(min_roll,max_roll)
                roll_crit = random.randint(min_roll,max_roll)
                if roll_res == roll_crit:
                    player.health += 80
                    print ("The wizard has goofed up his spell and ended up healing you instead.")
                    print ("You've regained 80 points of energy.\nYou're now at %d energy points." % player.health)
                    roll_it = False
                else:
                    print ("You waited for his next attack.")
                    roll_it = False
        elif choice == 3:
            player.health += 50
            print ("You've healed yourself for 30 energy.")
            print ("Your energy is now at %d points." % player["Health"])

        if secret_boss.health >= 0:
                player.health -= secret_boss.power
                print ("You've lost %d energy points from the wizard's attack!" % secret_boss.power)
                if player.health <= 0:
                    os.system("clear")
                    al.sad_face()
                    print ("> You were brutally murdered by a wizard.")
                    print ("> Never trust a wizard.")
                    break
        else:
            os.system("clear")
            al.ecstatic_face()
            os.system("say Congratulations!")
            print ("> Congratulations! You just killed a wizard")
            print ("> I'm so proud of you %s." % player.name)
            break

        input("Please press enter to continue.")
        os.system("clear")

play()
if enable_secret:
    boss_fight()