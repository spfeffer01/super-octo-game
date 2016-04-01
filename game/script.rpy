# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image xmysteryx normal = "masterpiece.png"
image xmysteryx blush = "masterpiece-blush.png"
image xmysteryx rage = "masterpiece-rage.png"

# Declare characters used by this game.
# define e = Character('Eileen', color="#c8ffc8")
define x = Character('MYSTERY', color="#836FFF")


# The game starts here.
label start:

    show xmysteryx normal 
    
    x "OH NO, THERE IS A CLONE OF ME."
    
    show xmysteryx blush
    
    x "I BETTER MAKE OUT WITH IT."
    
    show xmysteryx rage 
    
    x "INEXPLICABLE RAGE!"

#    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
