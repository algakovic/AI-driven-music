import winsound
import numpy as np
from numpy import random


def song(start, end):
    winsound.Beep(int(start), np.random(500, 1000)
    for note in [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]:
	    winsound.Beep(int(note+.5), 500)
    winsound.Beep(int(end), np.random(500, 1000))

song(349.23, 329.63)

#Check pyaudiere for next steps
