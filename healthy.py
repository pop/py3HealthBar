# v0.4 Displays 1 Hash Mark for every five minute increment you have been logged in.
# Resets after you have logged in.
# All values are static, but can be edited at the top of the file
# Written by Elijah Voigt and Lucy Wyman

from time import time
import subprocess
import os

# This is a list of the variables used in Py3HealthBar
# time_t gets the time on the scripts startup
time_t = time()
# TIMEOUT is the number of seconds it takes for a new symbols to be created
TIMEOUT = 300
# HEALTHY_INCREMENTS is the number of symbols created before they turn red
HEALTHY_INCREMENTS = 3
# LIMIT is the number of symbols spawned before your lock screen is starte
LIMIT = 12 
# This is weather or not you want colors.
# False gives white symbols
COLORS = True
# This is the symbol. It can be anything but '#' tends to work best
SYMBOL = "#"
# This is your lock screen.
# If you don't use i3lock please adjust this so your lock screen is started
# Simply put the terminal command used to start your lock screen between quotes
LOCK = "i3lock"

class Py3status:
    

    def py3HealthBar(self, i3status_output_json, i3status_config):
        # l_time is the current time
        l_time = time()
        # delta is the difference between the current time and when the script began
        delta = l_time - time_t
        # This cornverts delta from a floating point number to an integer
        delta = int(delta)

        # Initialize var to be a single SYMBOL
        var = SYMBOL 

        # 'x' is the number of SYMBOLS there should be
        x = delta/TIMEOUT
        # 'x' is converted to an integer
        x = int(x)
        # This for loop sets var to be the number of SYMBOLs it should be
        for i in range (0,x):
            var += str(SYMBOL)

        # 'condition' dictates weather the color should be red or green
        # true if green, false is red
        condition = (x < (HEALTHY_INCREMENTS))

        # This line converts 'var' to the an appropriate output for i3status
        status = '{}'.format(var)

        # Formats 'response' for i3status output
        response = {'name': 'healthbar', 'full_text': status}
        # Sets response's timeout to be the number of seconds dictated above
        response['cached_until'] = TIMEOUT 

        # 'COLORS' is weather the user wants green/red coloring.
        # If not, this step is skipped and the output is white
        if COLORS:
            if condition:
                response['color'] = i3status_config['color_good']
            else:
                response['color'] = i3status_config['color_bad']
        
        # If var is over 'LIMIT' characters long the lock screen is started and 'time_t' is reset
        if (len(var)> (LIMIT)):
            subprocess.call(LOCK)	
            global time_t 
            time_t = time()

        # returns 'response'
        return (0, response)


