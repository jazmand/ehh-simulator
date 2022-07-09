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

define aoi = Character("Aoi", color="#6f00ff")
define ayumi = Character("Ayumi", color="#39FF14")
define katsumi = Character("Katsumi", color="#ffffff")
define kenji = Character("Kenji", color="#e62121")
define rikona = Character("Rikona", color="#ffe714")
define taigen = Character("Taigen", color="#0034e0")
define yasuo = Character("Yasuo", color="#ff5100")
define characterStats = Character(None, 
    what_font = "/fonts/TitanOne-Regular.ttf", 
    what_color = "ffffff",
    what_size = 45, 
    what_drop_shadow = (2, 2,),
    what_xpos = 0.5,
    what_ypos = 1.8,
    window_background = None, 
    window_bottom_margin = 600,)
image sprite_animation = anim.Filmstrip("sprite_animation.png",(280, 385), (5,2), 0.125, loop=True)


# The game starts here.

label start:

    #run day_1.rpy file
    jump day_1

    # This ends the game.

    return
