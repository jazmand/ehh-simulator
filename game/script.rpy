# The script of the game goes in this file.

init python:

# Scared/anxious animation    
    def _shake_function(trans, st, at, dt=None, start=1, end=8): 
        # @param:
        # dt = duration timebase
        # start = initial wobble distance
        # end = final wobble distance
        if not dt or st <= dt:
            dt = dt if dt else st if st else 1.0
            dist = start + ( ( end-start ) * ( st / dt ) )
            trans.xoffset = int(dist*(.5-renpy.random.random())*2)
            trans.yoffset = int(dist*(.5-renpy.random.random())*2)
            return .01
        else:
            return None
            
transform show_anxiety(dt=None, start=1, end=8): 
    function renpy.curry(_shake_function)(dt=dt, start=start, end=end)
# Eg: show rikona at show_anxiety(None, 5, 5)




# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ao = Character("aoi")
define a = Character("ayumi")
define ka = Character("katsumi")
define ke = Character("kenji")
define r = Character("rikona")
define t = Character("taigen")
define y = Character("yasuo")

# The game starts here.

label start:

    # Get user name, if nothing is entered, make it "Unkown".

    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Unknown"
    
    define p = Character("[povname]", color="#4346f1", what_italic=True)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg maseda

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    p "Wow, my first day at Maseda University! I worked hard my whole life, and now I’ve finally made it!"

    p "I can’t wait to study all kinds of new things! Meet all kinds of new people! And maybe… could this be the year I… fall in…"

    show kenji: 
        xpos 0.25 ypos 0.55
    show rikona: 
        xpos 0.5 ypos 0.64
    with dissolve

    stop music fadeout 1.0

    "Random Student 1" "EEEH! It\’s already 8:57am!? Quick, we\’re going to be late for the {b}first year orientation!{/b}"

    "Random Student 2" "EEEH! Yabai! Let\’s go!"

    show kenji at offscreenright with move 
    
    hide kenji

    show rikona at offscreenright with move

    hide rikona
    
    p "No way! I’m going to be late for first year orientation! Let me find my map and schedule…"

    play sound "<from 1 to 2>audio/paper-crumpling.mp3" volume 0.5 
    
    pause 1.0

    scene bg schedule

    p "Oh crap, my schedule is ruined! I’m going to be late! What should I do? Where should I go? Should I ask someone?"

    pause 0.5

    $ randRoomate = renpy.random.choice(['rm1', 'rm2', 'rm3','rm4', 'rm5', 'rm6', 'rm7'])
    if randRoomate == 'rm1' or randRoomate == 'rm2' or randRoomate == 'rm3':
        $ pronoun = 'her'
    elif randRoomate == 'rm4' or randRoomate == 'rm5':
        $ pronoun = 'him' 
    elif randRoomate == 'rm6' or randRoomate == 'rm7':
        $ pronoun = 'them'

    scene bg maseda

    show katsumi at right:
        zoom 0.5

    p "Right! I’ll ask [pronoun], [randRoomate]!"

    play sound "<from 1 to 2>audio/running-road.mp3" volume 0.2

    show katsumi:
        ease 0.5 xalign 0.5
        ease 0.5 zoom 1.0
    with vpunch
    with vpunch      
    with vpunch      

    pause 1.0

    p "{plain}{size=-10}ee… eee… ehh…{/size}{/plain}"

    p "Oh no… what’s happening? I… I want to ask where first year orientation is, but I can’t seem to find the right words…"

    randRoomate "Hi there! You look like you’re also a first year student! Are you lost?"

    p "{plain}ehh…{/plain}"

    randRoomate "Let’s go!"

    p "{plain}{size=+10}eeeeh!{/size}{/plain}"

    show katsumi at offscreenright with move

    hide katsumi

    play sound "<from 1 to 3>audio/running-road.mp3" volume 0.5 

    scene bg maseda
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    
    pause 0.5

    p "This is way too much for my first day! Holding hands with a cutie and running through a romantic, cherry-blossom filled campus? I think I’m going to have a heart attack."

    pause 0.5

    scene black with dissolve

    randRoomate "Here we are!"

    play sound "audio/wood-door-opening.mp3" volume 0.5
    
    pause 1.0

    scene bg lecture with dissolve

    queue sound "<from 1 to 3>audio/chatter.mp3" volume 0.5 

    pause 3.0

    p "Oh no… everyone’s staring at me… I… I can’t take this… I’m going to burst!"

    "Headmaster" "Ah, latecomers I see! Take a seat and try not to disturb any more of my welcome speech. I’ll be sure to keep an eye on you troublemakers."

    p "What? No! This can’t happen on my first day! This isn’t my fault! I - I don’t understand!"

    menu:
        "EEEEEEEEEEHHH?":
            p "EEEEEEEEEEHHH?"

    scene black with dissolve

    play music "audio/main_theme.mp3" fadein 1.0 volume 0.5

    centered "Ehh Simulator Demo v0.1 End"

    # This ends the game.

    return
