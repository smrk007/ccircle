import ccircle

def keyDown(): # Returns string of whatever key is down, None if no key

    letters = 'abcdefghijklmnopqrstuvwxyz'
    for char in letters:
        if ccircle.isKeyDown(char):
            return char

    etc = ['backspace','enter','esc','space','left','right','up','down']
    for key in etc:
        if ccircle.isKeyDown(key):
            return key

    return None # If no key is down