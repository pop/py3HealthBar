# v0.4 Displays 1 Hash Mark for every five minute increment you have been logged in.
# Resets after you have logged in.
# All values are static, but can be edited at the top of the file
# Written by Elijah Voigt and Lucy Wyman

from time import time
import subprocess
import os

os.system('killall i3lock')

time_t = time()
TIMEOUT = 300 
HEALTHY_INCREMENTS = 3
LIMIT = 12 
COLORS = True
SYMBOL = "#"
LOCK = "i3lock"

class Py3status:

    def test(self, i3status_output_json, i3status_config):
        l_time = time()
        delta = l_time - time_t
        delta = int(delta)

        var = SYMBOL 

        x = delta/TIMEOUT
        x = int(x)
        for i in range (0,x):
            var += str(SYMBOL)

        condition = (x < (HEALTHY_INCREMENTS))

        status = '{}'.format(var)

        response = {'name': 'healthbar', 'full_text': status}
        response['cached_until'] = TIMEOUT 

        if COLORS:
            if condition:
                response['color'] = i3status_config['color_good']
            else:
                response['color'] = i3status_config['color_bad']

        #if(os.system('pidof i3lock') == 256):
        #    global time_t
        #    time_t = time()

        if (len(var)> (LIMIT)):
            subprocess.call(LOCK)	
            global time_t 
            time_t = time()

        return (0, response)


