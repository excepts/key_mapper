d = {}

import itertools, time, keyboard

for k in d:

    keyboard.block_key(k)

while True:

    for k in d:

        if keyboard.is_pressed(k):

            keyboard.press_and_release(d[k])

    time.sleep(0.03)