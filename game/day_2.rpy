label day_2:
    stop music
    play sound "audio/door_closing.mp3" volume 0.5 
    
    scene bg communal with dissolve

    p "What an exhausting day. But… I’m excited to meet my new roommates!"

    "Girl's Voice(?)" "Oh, that must be them - our last roommate!"

    p "E-eh? Am I late again?"

    "Guy's Voice(?)" "Huzzah! Let us greet them!"

    p "Oh no… I’m not ready to meet them all at once!"

    scene black with dissolve

    show sprite_animation:
        xalign 0.8
        yalign 0.5

    centered "{color=#FFFFFF}NAME: KATSUMI\n
    AGE: 19\n
    PRONOUNS: SHE/HER/HERS\n
    HEIGHT: 5’11\n
    MAJOR: SPORTS SCIENCE\n
    BLOOD TYPE: B+\n
    ZODIAC SIGN: ARIES\n
    BIRTHDAY: MARCH 21ST\n
    LIKES: pork bowl, judo, k-dramas\n
    DISLIKES: soup, losing, lazy mornings{/color}" 

    scene bg communal with dissolve

    katsumi "HI! Nice to meet you! I’m Katsumi! What’s your name?"

    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Unknown"

    # ----------CHOICE HERE----------

    p "{plain}Eeeeh…{/plain}"

    katsumi "Oh, [p], huh?"

    p "Huh? Is she psychic?"

    p "..."

    p "Oh, right, I\’m still wearing my name-tag from orientation."

    katsumi "This year is going to be so much fun. Everyone in this house seems so interesting, and so…"

    p "..."

    katsumi "..."

    katsumi "WEAK!"

    katsumi "We\’ve got to get to work on training! 6am, tomorrow morning, WEIGHTS!"

    katsumi "Especially you, Yasuo."

    yasuo "I don’t need to train my muscles. Only my mind."

    scene black with dissolve

    show sprite_animation:
        xalign 0.8
        yalign 0.5

    centered "{color=#FFFFFF}NAME: YASUO\n
    AGE: 20\n
    PRONOUNS: HE/HIM/HIS\n
    HEIGHT: 5’5\n
    MAJOR: RELIGIOUS STUDIES\n
    BLOOD TYPE: O+\n
    ZODIAC SIGN: PISCES\n
    BIRTHDAY: FEBRUARY 29TH\n
    LIKES: Vegetarian food, quiet time, true crime documentaries\n
    DISLIKES: loud noises, deep water, sinus infections{/color}" 

    scene bg communal with dissolve

    yasuo "You should all join me. Really, zazen can work absolute wonders for the mind."

    katsumi "I -"

    yasuo "And body."
    
    katsumi "..."

    yasuo "I’m truly grateful to meet you all today, and I hope that we can become great friends and even better spiritual mentors to each other this year."

    yasuo "Are you spiritual, [p]?"

    # ----------CHOICE HERE----------

    p "{plain}Eeeh...{/plain}"

    "Girl's Voice(?)" "Heehee, no need to be so serious, Yasuo-senpai! <3"

    "Girl's Voice(?)" "This is supposed to be a FUN meeting of new pals! (and maybe more…) <3"
