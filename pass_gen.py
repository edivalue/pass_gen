#EDIVALUE
import random
import sys
from math import log

#Check the Python Version installed
if sys.version_info < (3, 0):
    input = raw_input

# Just some colors and shit
white = '\033[1;97m'
green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que =  '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'

print ('''%s     __   	__           
█▀▀ █▀▀▄ █ █░░█ █▀▀█ █░░ █░░█░█▀▀
█▀▀ █░░█ █ █░░█ █▄▄█ █░░ █░░█░█▀▀
▀▀▀ ▀▄▄▀ █ ▀▄▄▀ ▀░░▀ █▄▄ █▄▄█░█▄▄


%s\n''' % (green, end))
       
name = input('%s Name of a RANDOM person: ' % que).lower()
choice = input('%s Obsfucate the name? [Y/n] ' % que).lower()
if choice == 'n':
	obsfucate = False
else:
	obsfucate = True

first = ['had', 'plays', 'buys', 'love', 'tops', 'press', 'likes', 'load', 'learns', 'has', 'uploads', 'wants', 'runs', 'flys', 'stops', 'pull', 'hacks', 'picks', 'clears', 'types', 'draws', 'cuts']

second = ['your', 'our', 'purple', 'yellow', 'many', 'green', 'blue', 'all', 'three', 'five', 'hundred', 'fine', 'my', 'black', 'nice', 'small', 'gas', 'nine', 'ten', 'two', 'six', 'password', 'super']

third = ['book', 'apples', 'pens', 'ballot', 'keys', 'hanger', 'stars', 'trees','stones', 'cars', 'apps', 'computers', 'mangoes', 'caps', 'poles', 'buttons', 'drinks', 'papers', 'hackers', 'broom',]

seperators = ['-', '.', '*', '+', '~', '_', '@']

generated_passwords = []

def generate(name):
	wordlist = []
	wordlist.append(random.choice(first))
	wordlist.append(random.choice(second))
	wordlist.append(random.choice(third))
	seperator = random.choice(seperators)
	name = name.title()
	if obsfucate:
		name = name.replace('a', '4').replace('h', '#').replace(
			'e', '3').replace('i', '!').replace('l', '1').replace(
				't', '7').replace('s', '$').replace('o', '0').replace(
					'b', '6').replace('g', '9')
	password = name + seperator + seperator.join(wordlist)
	generated_passwords.append(password)
	print (' %s|%s %-35s%s|%s %-20s%s|%s' % (green, end, password, green, end, (log(82)/log(2)) * len(password), green, end))

def initiate():
	print ('')
	print (' %s+------------------------------------+---------------------+%s' % (green, end))
	print (' %s| Passwords                          | Entropy             |%s' % (green, end))
	print (' %s+------------------------------------+---------------------+%s' % (green, end))
	for y in range(0, 10):
		generate(name)
	print (' %s+--------------------------+-------------------------------+%s' % (green, end))
	choice = input('\n%s Generate more passwords? [y/N] ' % que).lower()
	if choice == 'y':
		initiate()
	else:
		quit()

initiate()