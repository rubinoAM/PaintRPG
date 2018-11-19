import os
import random

player = {
    "Name":"",
    "Health":100,
    "Power":15,
    "Laziness":0
}

canvas = {
    "Health":100,
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
      \    \____/ /
       `.       .'
      .' `-,,,-' `.
    .'      :      `.  
            :
""")
print ("> Well alrighty, %s! Let's get a move on!" % player['Name'])
print ("> Saturday is the day for me. Not a cloud in sight!")

def play():
    print ("It's game time, %s!" % player['Name'])

    wont_play = False
    jerk_pts = 0

    while player['Health'] > 0 and canvas['Health'] > 0:
        if(not wont_play):
            print ("> You have %d energy and can get %d work done right now." % (player['Health'], player['Power']))
            print ("> The canvas needs %d more work and will drain %d energy." % (canvas['Health'], canvas['Power']))
            print ("> What'll you do? \n1.Paint\n2.Procrastinate\n3.Thumbnail")

        choice = int(input("> "))

        if choice not in range(1,4):
            if jerk_pts < 3:
                jerk_pts += 1
                print ("""
            :
   `.       ;        .'
     `.  .-'''-.   .'
       ;'  __   _;'
      /   '\    / `\`
     |  _( \ (  /  |
'''''| (_)    >    |``````
      \    xxxxx  /
       `.       .'
      .' `-,,,-' `.
    .'      :      `.  
            :
""")
                print ("> Don't be a jerk! Pick something! \n1.Paint\n2.Procrastinate\n3.Thumbnail")
            else:
                os.system("clear")
                os.system("say DIE!")
                print ("""
                        |
                    .   |
                        |
          \    *        |     *    .  /
            \        *  |  .        /
         .    \     ___---___     /    .  
                \.--         --./     
     ~-_    *  ./               \.   *   _-~
        ~-_   /    \         /    \   _-~     *
   *       ~-/    __\       /__    \-~        
     .      |    (_O_)     (_O_)    |      .
         * |        /   |   \       | *     
-----------|           |             |-----------
  .        |           |             |        .    
        *   |           --          | *
           _-\ ____________________/-_    *
     .  _-~ . \     |    |    |    /   ~-_     
     _-~       `\   |    |    |  /'*      ~-_  
    ~           /`--|__  |___-|'\           ~
           *  /        ---     .  \       .
            /     *     |           \`
          /             |   *         \`
                     .  |        .
                        |
                        |

__    ______  _____  _____  _____  _____  _  _  _  _ 
\ \   |  _  \|_   _||_   _||_   _||  ___|| || || || |
 \ \  | | | |  | |    | |    | |  | |__  | || || || |
  > > | | | |  | |    | |    | |  |  __| | || || || |
 / /  | |/ /  _| |_  _| |_  _| |_ | |___ |_||_||_||_|
/_/   |___/   \___/  \___/  \___/ \____/ (_)(_)(_)(_)
                """)
                print ("Well unfortunately you're dead now.\nGood job aggravating the sun, idiot!")
            wont_play = True   
        else:
            wont_play = False
            if choice == 1:
                canvas['Health'] -= player['Power']
                print ("You've made %d progress on your artwork!" % player['Power'])
            elif choice == 2:
                roll_it = True
                while roll_it:
                    roll_res = random.randint(min_roll,max_roll)
                    roll_crit = random.randint(min_roll,max_roll)
                    if roll_res == roll_crit:
                        player['Laziness'] = 0
                        player['Health'] += 80
                        print ("Amazingly your procrastination led to some inspiration!")
                        print ("You've regained 80 points of energy.\nYou're now at %d energy points." % player['Health'])
                        roll_it = False
                    else:
                        player['Laziness'] += 10
                        print ("Nothing was accomplished... but you feel a little better.")
                        roll_it = False
            elif choice == 3:
                player['Health'] += 50
                print ("Thumbnailing the ideas you had in your head has helped your resolve.\nYou've regained 30 energy through your problem solving.")
                print ("Your energy is now at %d points." % player["Health"])

        if canvas["Health"] >= 0:
            player['Health'] -= canvas['Power']
            print ("Time has passed.\nYou feel a bit more tired. You've lost %d energy points." % canvas["Power"])
            if player["Health"] <= 0:
                os.system("clear")
                print ("""
            :
   `.       ;        .'
     `.  .-'''-.   .'
       ;'        ;'
      /   '/    \ `\`
     |  _( / (  \  |
'''''| (_)    >  ' |``````
      \      ~~  '/
       `.       .'
      .' `-,,,-' `.
    .'      :      `.  
            :
""")
                print ("> You're all out of energy and with no finished piece to show for it.")
                print ("> Better luck next time!")
                break
            elif player["Laziness"] == 30:
                os.system("clear")
                print ("""
            :
   `.       ;        .'
     `.  .-'''-.   .'
       ;'  __   _;'
      /   '_    _ `\`
     |  _( v (  v  |
'''''| (_)    >    |``````
      \      ___  /
       `.       .'
      .' `-,,,-' `.
    .'      :      `.  
            :
""")
                print ("> Your laziness has gotten the better of you and you've given up for today.")
                print ("> Smooooooooth.")
                break
        else:
            os.system("clear")
            print ("""
            :
   `.       ;        .'
     `.  .-'''-.   .'
       ;'  ^    ^;'
      /   '       `\`
     |  _( ^ (  ^  |
'''''| (_)  __>__  |``````
      \    \    / /
       `.   `--'.'
      .' `-,,,-' `.
    .'      :      `.  
            :
""")
            os.system("say Yay!")
            print ("Yay! Your masterpiece is finally completed!")
            print ("You feel a tremendous wave of confidence overcome you as you marvel at the finished piece.")
            break

        input("Please press enter to continue.")
        os.system("clear")
play()