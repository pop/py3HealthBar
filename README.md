Py3HealthBar
===========

**Py3HealthBar** is a **Py3Status** module for reminding you stay active while using **i3**.

Installation
===========

To use Py3HealthBar you must install  py3status through pip.

	$ sudo pip install py3status

Then clone this repo	

SSH:

	$ git clone git@github.com:ElijahCaine/py3HealthBar.git
	
HTPS:

	$ git clone https://github.com/ElijahCaine/py3HealthBar.git
	

Here's a quick rundown of what you'll need to do in order to get Py3HealthBar working:

First modify your i3status.conf. It may be located in /etc/ or you may have moved it. Either way change the `general` section so it looks similar to this:

	general {
		colors = true
		interval = 5
		output_format = "i3bar"
	}
	
The only line in that which matters is the `output_format = "i3bar"`. Everything else you can change to be whatever.

Next modify your the part of your i3config that looks like this:

	bar {
		position bottom
		status_command py3status -c [LOCATION OF 'i3status.conf'] -i [DIRECTORY FOR 'py3status' SCRTIPS]
	}
	
I suggest storing your i3 files in a '.i3' directory inside your home directory. If you do that, your code will look something like this:
	
	bar {
		position bottom
		status_command py3status -c ~/.i3/i3status.conf -i ~/py3HealthBar/
	}

Once you've told i3 where to find your i3status.conf and where you're storing your scripts py3Status should work fine.
To test out the sript restart i3 with `$mod + Shift + r`

FAQ:
====
**Q:** What is **Py3HealthBar**?

**A:** **Py3HealthBar** is a tool used with **Py3Status** in **i3** to encourage you to get up and move every 15 minutes.

**Q:** How does **Py3HealthBar** work?

**A:** It's a simply python script which conveys to you how long you've been working. By default it displays a new '#' symbol every 5 minutes. After 15 minutes the marks turn red. After 60 minutes the script launches i3lock.

**Q:** What should I do?

**A:** Anything is better than nothing. When **Py3HealthBar** tells you it's been 15 minutes at the very least stand up, take a breath, and walk around your chair. If you want to be more active, try doing some toe touches or even some jumping jacks. Don't forget to be mindful to those around you.

**Q:** My **Py3Status** doesn't work. Help?

**A:** I'd suggest you go look at the **Py3Status** github page found here: [https://github.com/ultrabug/py3status](https://github.com/ultrabug/py3status) There you can find a great setup tutorial and how to build your own **Py3Status** modules.

**Q:** Does **Py3HealthBar** have a config file? I really like config files.

**A:** At the moment I'm unable to create a working config file with **Py3HealthBar**, but you can change the values in the script to suite your lifestyle. All values are at the top of the script and are commented to help you make appropriate changes.

**Q:** I'm confused. Can I ask you a question?

**A:** Sure. Contact me through GitHub or on IRC. My nick is `pop_n_fesh` on `irc.freenode.net`

**Q:** I got up and moved when it turned red, but it's still growing and red. How do I change this?

**A:** In future versions I plan to make your lock program trigger a reset, but right now the only workaround is to reset **i3** with `$mod + Shift + r`. This shouldn't affect much besides the **Py3HealthBar** module.
