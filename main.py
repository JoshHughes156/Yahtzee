from random import randint
from os import system
from points import *
import json

lng = 'eng'
def set_lang(l):
	global lng
	lng = l

language_file = 'language.json'
lang = 0
with open(language_file, 'r') as f:
	lang = json.load(f)

hold = []
prev_rolls = []

def num_to_die(num):
	dice = [
		'   \n • 1\n   ', '  •\n   2\n•  ', '  •\n • 3\n•  ', '• •\n   4\n• •',
		'• •\n • 5\n• •', '•••\n   6\n•••'
	]
	return dice[num - 1]


def play_round():
	global hold
	global prev_rolls
	global score

	iters = 5 - len(hold)
	for j in range(0, iters):
		print(f'{lang["misc"][4][lng]} (' + str(j + 1) + '/' + str(iters) + '): ')
		roll = randint(1, 6)
		prev_rolls.append(roll)
		print(num_to_die(roll))
		choice = 0
		while choice not in ['y', 'n']:
			choice = input(f'{lang["misc"][5][lng]} (y/n)?: ')
		if choice == 'y':
			hold.append(roll)
			hold = sorted(hold)

		system('clear')
		print(f'{lang["misc"][6][lng]}: ')
		print(hold)


def score_options():
	global choosen
	global score
	global hold

	scores = [
		upper_selection(hold, 1),
		upper_selection(hold, 2),
		upper_selection(hold, 3),
		upper_selection(hold, 4),
		upper_selection(hold, 5),
		upper_selection(hold, 6),
		three_of_a_kind(hold),
		four_of_a_kind(hold),
		full_house(hold),
		small_straight(hold),
		large_straight(hold),
		yahtzee(hold),
		chance(hold)
	]

	system('clear')
	print(f'{lang["misc"][7][lng]}: {choosen}')
	print(f'{lang["misc"][6][lng]}: {hold}\n')
	
	print(f'1) {lang["upper_section"][1][lng]}: {scores[0]}')
	print(f'2) {lang["upper_section"][2][lng]}: {scores[1]}')
	print(f'3) {lang["upper_section"][3][lng]}: {scores[2]}')
	print(f'4) {lang["upper_section"][4][lng]}: {scores[3]}')
	print(f'5) {lang["upper_section"][5][lng]}: {scores[4]}')
	print(f'6) {lang["upper_section"][6][lng]}: {scores[5]}')

	print(f'7) {lang["lower_section"][1][lng]}: {scores[6]}')
	print(f'8) {lang["lower_section"][2][lng]}: {scores[7]}')
	print(f'9) {lang["lower_section"][3][lng]}: {scores[8]}')
	print(f'10) {lang["lower_section"][4][lng]}: {scores[9]}')
	print(f'11) {lang["lower_section"][5][lng]}: {scores[10]}')
	print(f'12) {lang["lower_section"][6][lng]}: {scores[11]}')
	print(f'13) {lang["lower_section"][7][lng]}: {scores[12]}')

	choice = 0
	while True:
		try:
			choice = int(input(f'\n{lang["misc"][8][lng]}?: '))
		except:
			continue
		if choice not in range(1, 14):
			print(f'{lang["misc"][10][lng]}')
			continue
		if choice in choosen:
			print(f"{lang['misc'][11][lng]}")
			continue

		choosen.append(choice)
		score += scores[choice - 1]
		break


choosen = []
score = 0


def whole_round():
	global hold
	for i in range(0, 3):
		if len(hold) != 5:
			play_round()

	while len(hold) < 5:
		hold.append(prev_rolls.pop())

	score_options()
	hold = []


def play():
	for i in range(0, 13):
		print(f'{lang["misc"][2][lng]}: {score}')
		print(f'\n ### {lang["misc"][3][lng]} {i+1} ###\n')
		whole_round()
		system('clear')

	print(f'{lang["misc"][2][lng]}: ' + str(score))
