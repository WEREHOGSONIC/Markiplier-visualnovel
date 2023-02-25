# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Markiplier" , color= "#ffa9f4")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg church

    # This scows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show markiplier talking 
    with dissolve
    # These display lines of dialogue.

    m "Helloeverybody, my names Markiplier"

    m "BUY MY ONLYFANS"

    menu: 
        "Yes":
            jump yesbuy 

        "No":
            jump nobuy

label yesbuy:
    show markiplier yah 
    with dissolve
    m  "😏, :smirkingemoji:"
    return

label nobuy: 
    show markiplier angry 
    with vpunch
    m "Im angry"
    show markiplier talking
    m "Please,<3333333 "
    menu: 
        "Okay, fine":
            jump yesbuy 
        "I'm too broke":
            jump brokehoe

label brokehoe:
    show markiplier cry
    with move 
    m "Cries"
    return
    # This ends the game.

    return
