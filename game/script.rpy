# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("pc")
define ao = Character("aoi")
define a = Character("ayumi")
define ka = Character("katsumi")
define ke = Character("kenji")
define r = Character("rikona")
define t = Character("taigen")
define y = Character("yasuo")

# The game starts here.

label start:

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

    show kenji

    stop music fadeout 1.0

    ke "Hi! I'm Kenji."

    # This ends the game.

    return
