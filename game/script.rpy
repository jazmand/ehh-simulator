# The script of the game goes in this file.

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
    
    define p = Character("[povname]", color="#4346f1")

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg maseda
    play music "<from 5>audio/main_theme.mp3" fadein 1.0 volume 0.5
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    p "Wow, my first day at Maseda University! I worked hard my whole life, and now I’ve finally made it!"

    p "I can’t wait to study all kinds of new things! Meet all kinds of new people! And maybe… could this be the year I… fall in…"

    show kenji:
        xpos 500 ypos 500

    show rikona:
        xpos 1000 ypos 550

    stop music fadeout 1.0

    Character("Random Student 1", color="#000000") "EEEH! It\’s already 8:57am!? Quick, we\’re going to be late for the first year orientation!"

    Character("Random Student 2", color="#000000") "EEEH! Yabai! Let\’s go!"

    show kenji at right with move

    hide kenji

    show rikona at right with move

    hide rikona
    
    p "No way! I’m going to be late for first year orientation! Let me find my map and schedule…"

    # This ends the game.

    return
