label day_2:
    stop music
    play sound "audio/door_closing.mp3" volume 0.5 
    
    scene bg communal with dissolve

    p "What an exhausting day. But… I’m excited to meet my new roommates!"

    # ----------TUTORIAL OF EHH SYSTEM HERE----------

    "Random Character" "Are you ok? You’ve just been standing there, blankly, saying ‘eeeh’ over and over again…"

    "Girl's Voice(?)" "Oh, that must be them - our last roommate!"

    p "E-eh? Am I late again?"

    "Guy's Voice(?)" "Huzzah! Let us greet them!"

    p "Oh no… I’m not ready to meet them all at once!"

    window hide

    scene bg stats with dissolve

    # show sprite_animation:
    #     xalign 0.8
    #     yalign 0.5

    show katsumi:
        xpos 0.1 zoom 1.2

    characterStats "
    {size=+40}KATSUMI{/size}\n
    \n
    AGE: 19\n
    PRONOUNS: SHE/HER/HERS\n
    HEIGHT: 5’11\n
    MAJOR: SPORTS SCIENCE\n
    BLOOD TYPE: B+\n
    ZODIAC SIGN: ARIES\n
    BIRTHDAY: MARCH 21ST\n
    LIKES: pork bowl, judo, k-dramas\n
    DISLIKES: soup, losing, lazy mornings"

    scene bg communal with dissolve

    window show

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

    window hide

    scene bg stats with dissolve

    show yasuo:
        xpos 0.1 zoom 1.2

    characterStats "
    {size=+40}YASUO{/size}\n
    \n
    AGE: 20\n
    PRONOUNS: HE/HIM/HIS\n
    HEIGHT: 5’5\n
    MAJOR: RELIGIOUS STUDIES\n
    BLOOD TYPE: O+\n
    ZODIAC SIGN: PISCES\n
    BIRTHDAY: FEBRUARY 29TH\n
    LIKES: Vegetarian food, quiet time,\n
    true crime documentaries\n
    DISLIKES: loud noises, deep water,\n
    sinus infections"

    scene bg communal with dissolve

    window show

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

    window hide

    scene bg stats with dissolve

    show ayumi:
        xpos 0.1 ypos 0.1 zoom 1.2

    characterStats "
    {size=+40}AYUMI{/size}\n
    \n
    AGE: 18\n
    PRONOUNS: SHE/HER/HERS\n
    HEIGHT: 5’0\n
    MAJOR: ART\n
    BLOOD TYPE: AB-\n
    ZODIAC SIGN: LEO\n
    BIRTHDAY: August 5th\n
    LIKES: cute animals, bubblegum\n
    pop songs, dating sims\n
    DISLIKES: Gabriel’s horn, bowl cuts,\n
    house chores"
    
    scene bg communal with dissolve

    window show

    # ----------DIALOGUE HERE----------

    window hide

    scene bg stats with dissolve

    show rikona:
        xpos 0.1 ypos 0.1 zoom 1.2

    characterStats "
    {size=+40}RIKONA{/size}\n
    \n
    AGE: 18\n
    PRONOUNS: SHE/HER/HERS\n
    HEIGHT: 5’6\n
    MAJOR: MATHEMATICS\n
    BLOOD TYPE: A-\n
    ZODIAC SIGN: SCORPIO\n
    BIRTHDAY: October 30th\n
    LIKES: logic puzzles, jell-o, nail polish\n
    DISLIKES: irrational numbers,\n
    people who set world records,\n
    cup ramen"
    
    scene bg communal with dissolve

    window show

    # ----------DIALOGUE HERE----------

    window hide

    scene bg stats with dissolve

    show taigen:
        xpos 0.1 zoom 1.2

    characterStats "
    {size=+40}TAIGEN{/size}\n
    \n
    AGE: 18\n
    PRONOUNS: HE/HIM/HIS\n
    HEIGHT: 5’2\n
    MAJOR: BUSINESS STUDIES\n
    BLOOD TYPE: A+\n
    ZODIAC SIGN: VIRGO\n
    BIRTHDAY: September 12th\n
    LIKES: 0110001001110101011101000111010001110011, batteries, money\n
    DISLIKES: clowns, slow walkers, crystal pepsi"
    
    scene bg communal with dissolve

    window show

    # ----------DIALOGUE HERE----------

    window hide

    scene bg stats with dissolve

    show kenji:
        xpos 0.1 zoom 1.2

    characterStats "
    {size=+40}KENJI{/size}\n
    \n
    AGE: 18\n
    PRONOUNS: HE/HIM/HIS\n
    HEIGHT: 6’1\n
    MAJOR: WASTE MANAGEMENT\n
    BLOOD TYPE: O-\n
    ZODIAC SIGN: SAGITTARIUS\n
    BIRTHDAY: December 10th\n
    LIKES: corn mayonnaise pizza, 90s sitcoms, recycling\n
    DISLIKES: off-brand cereals, trash, slobs"
    
    scene bg communal with dissolve

    window show

    # ----------DIALOGUE HERE----------

    window hide

    scene bg stats with dissolve

    show aoi:
        xpos 0.1 zoom 1.2

    characterStats "
    {size=+40}AOI{/size}\n
    \n
    AGE: 24\n
    PRONOUNS: THEY/THEM/THEIRS\n
    HEIGHT: 5’9\n
    MAJOR: LITERATURE AND SCIENCE DUAL\n
    BLOOD TYPE: AB+\n
    ZODIAC SIGN: GEMINI\n
    BIRTHDAY: June 3rd\n
    LIKES: ice cream, finding loose coins, death metal\n
    DISLIKES: the FBI, film noir, WWE smackdown"
    
    scene bg communal with dissolve

    window show


    # ----------DIALOGUE HERE----------

    window hide

    scene bg stats with dissolve

    show coffee:
        xpos 0.1 zoom 1.2

    characterStats "
    {size=+40}COFFEE-KUN{/size}\n
    \n
    AGE: ???\n
    PRONOUNS: COFFEE/COFFEE/COFFEE\n
    HEIGHT: 1’3\n
    MAJOR: COFFEE\n
    BLOOD TYPE: COFFEE\n
    ZODIAC SIGN: TAURUS\n
    BIRTHDAY: April 20TH\n
    LIKES: coffee, texting, you\n
    DISLIKES: tea, consequences, sexism"
    
    scene bg communal with dissolve

    window show



