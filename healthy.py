
#v 0.1 Currently displays an additional '#' for every five minutes i3status has been running.

from time import time


TIME = time()   #Gets time at startup
TIMEOUT = 1     #Sets cache dump timeout to 1 second

# Begin Py3status stuffs
class Py3status:

    def test(self, i3status_output_json, i3status_config):
        l_time = time()     #Gets new time
        delta = l_time - TIME   # Calculates delta since startup time
        delta = int(delta)  #Sets delta time to int
        
        var = "" #Var is waht's getting passed to i3status eventually

        x = delta/600 #x is the number of 5 minute increments that have passed since the bar began.
        for i in range (0,x): #This increments through the x times and adds a # for every 5minute increment that has passed
            var += str("#") #Actual assignment of var
            
        status = '{}'.format(var) #formats output for py3status

        response = {'name': 'healthbar', 'full_text': status}   #This line is magic
        response['cached_until'] = TIMEOUT  # sets cache timeout to TIMEOUT 

        return (0, response)    # returns values to be printed on the bar
