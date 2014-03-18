
## Currently this script only displays the number of seconds that have passed since you started the script.

from time import time
import os


TIME = time()   #Gets time at startup
TIMEOUT = 1     #Sets cache dump timeout to 1 second

# Begin Py3status stuffs
class Py3status:
    def test(self, i3status_output_json, i3status_config):
        l_time = time()     #Gets new time
        delta = l_time - TIME   # Calculates delta since startup time
        delta = int(delta)  #Sets delta time to int
        status = '{}'.format(delta) #formats output for py3status
        response = {'name': 'healthbar', 'full_text': status}   #This line is magic
        response['cached_until'] = TIMEOUT  # sets cache timeout to TIMEOUT 
        return (0, response)    # returns values to be printed on the bar
