from main import play, set_lang
from sys import argv
from os import system

def run():
	menu = "\n 1: Play\n 2: Settings\n 3: Exit\n"

	while True:
		print(menu)
		while True:
			try:
				choice = int(input("Please enter your choice: "))
			except:
				print("Please enter a valid number")
			if choice in [1,2,3]:
				break
			else:
				print("Please enter a valid choice (1,2,3)")


		if choice == 1:
			play()
			continue
			cont = input("Continue playing?: ")
			while cont not in ['y', 'n']:
				print("Please enter a valid choice")
				cont = input("Continue playing?: ")
		elif choice == 2:
			if input("Would you like to change language (y/n): ").lower() == "y":
				while True:
					l = input("What language do you want? (eng/de): ")
					if l not in ["eng", "de"]:
						print("Enter a valid language")
						continue
					else:
						set_lang(l)
						break
			else:
				continue
		elif choice == 3:
			print("Thanks for playing")
			break

if "t" in argv:
	system("python points.py")
if "r" in argv:
	run()
