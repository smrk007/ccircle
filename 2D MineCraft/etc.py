import ccircle

def keyDown(): # Returns string of whatever key is down, None if no key

    out = {}

    letters = 'abcdefghijklmnopqrstuvwxyz'
    for char in letters:
        if ccircle.isKeyDown(char):
            out[char] = True
        else:
            out[char] = False

    etc = ['backspace','enter','esc','space','left','right','up','down']
    for key in etc:
        if ccircle.isKeyDown(key):
            out[key] = True
        else:
            out[key] = False

    return out

def camShift(player, center):
    x = center[0] - player.posX
    y = center[1] - player.posY
    return (x,y)