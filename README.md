Py3HealthBar
===========

Py3HealthBar is a Py3Status module for reminding you stay active while inside of i3

Installation
===========

To use Py3HealthBar you must install the python3 version of py3status through pip.

	$ sudo pip install py3status

After you have done that clone this repo	

SSH:

	$ git clone git@github.com:ElijahCaine/py3HealthBar.git
	
HTPS:

	$ git clone https://github.com/ElijahCaine/py3HealthBar.git
	

Here's a quick rundown of what you'll need to do in order to make py3status work:

Modify your the part of your i3config that looks like this:

	bar {
		position bottom
		status_command py3status -c [LOCATION OF 'i3status.conf'] -i [DIRECTORY FOR 'py3status' SCRTIPS]
	}
	
I suggest storing your i3 files in a '.i3' directory inside your home directory. If you do that, your code will look something like this:
	
	bar {
		position bottom
		status_command py3status -c ~/.i3/i3status.conf -i ~/py3HealthBar/
	}

Once you've told i3 where to find your i3status.conf and where your're storing your scripts py3Status should work fine.
To test out the sript restart i3 with `$mod + Shift + r`
