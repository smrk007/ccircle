import ccircle
import player

window = ccircle.Window()

# Objects in the environment
environment = []

character = player.Player()

while window.isOpen():
    window.clear(0,0,0)

    # Take player commands

    # Update environment depending on the player commands

    # Draw the objects of the environment

    window.update()