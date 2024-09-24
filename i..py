import time 
import sys
from turtle import delay
time.sleep



def print_lyrics():
    lines = [
        ("Romeo, take me somewhere we can be alone", 0.07),
        ("I'll be waiting, all there's left to do is run", 0.07),
        ("You'll be the prince and I'll be the princess", 0.07),
        ("It's a love story, baby, just say, Yes", 0.09),
        ("Romeo, save me, they're trying to tell me how to feel", 0.07),
        ("This love is difficult, but it's real", 0.09),
        ("Don't be afraid, we'll make it out of this mess", 0.07),
        ("It's a love story, baby, just say, Yes", 0.1),
        ("                                           LUV ", 0.0002),


    ]
    delay = [ 0.3, 0.5, 0.4, 0.3, 0.3, 0.3, 0.3 , 0.4 , 0.4]
    for i, (line, char_delay ) in enumerate(lines):
        for char in line :
            print ( char , end ='')
            sys.stdout.flush()
            time.sleep (char_delay)
        time.sleep(delay [i])

        print ("")

print_lyrics()
