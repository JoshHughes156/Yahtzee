
def test(fnc, test_data, expected_output, name="Test", test_value=0):
	global passes
	global tests
	result = fnc(test_data, test_value)
	if result == expected_output:
		print(name + ": ✔")
		passes += 1
	else:
		print(name + ": ❌")
	tests += 1

def upper_selection(hold, value):
	return hold.count(value) * value

def three_of_a_kind(hold, value=0):
	for i in range(1, 7):
		if hold.count(i) >= 3:
			return sum(hold)
	return 0

def four_of_a_kind(hold, value=0):
	for i in range(1, 7):
		if hold.count(i) >= 4:
			return sum(hold)
	return 0

def full_house(hold, value=0):
	if three_of_a_kind(hold) > 0:
		for i in range(1, 7):
			if hold.count(i) == 2:
				return 25
	return 0

def small_straight(hold, value=0):
	for i in range(0,2):
		seqs = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
		if(hold[i:i+4] in seqs):
			return 30
	return 0

def large_straight(hold, value=0):
	if hold in [[1,2,3,4,5], [2,3,4,5,6]]:
		return 40
	return 0

def yahtzee(hold, value=0):
	if len(list(set(hold))) == 1:
		return 50
	return 0

def chance(hold, value=0):
	return sum(hold)

if __name__ == "__main__":

	passes = 0
	tests = 0

	test(upper_selection, [1,1,1,3,5], 3, "Aces", test_value=1)
	test(upper_selection, [2,2,2,5,6], 6, "Twos", test_value=2)
	test(upper_selection, [3,3,3,3,4], 12, "Threes", test_value=3)
	test(upper_selection, [4,4,5,5,5], 8, "Fours", test_value=4)
	test(upper_selection, [1,1,2,2,5], 5, "Fives", test_value=5)
	test(upper_selection, [3,3,6,6,6], 18, "Sixes", test_value=6)

	test(three_of_a_kind, [2,3,4,4,4], 17, "Three of a kind")
	test(three_of_a_kind, [2,3,4,5,6], 0, "Three of a kind null")

	test(four_of_a_kind, [4,5,5,5,5], 24, "Four of a kind")
	test(four_of_a_kind, [2,3,4,5,6], 0, "Four of a kind null")

	test(full_house, [2,2,5,5,5], 25, "Full house")
	test(full_house, [2,3,4,5,6], 0, "Full house null")

	test(small_straight, [1,2,3,4,4], 30, "Small straight")
	test(small_straight, [1,1,1,1,1], 0, "Small straight null")

	test(large_straight, [1,2,3,4,5], 40, "Large straight")
	test(large_straight, [1,1,1,1,1], 0, "Large straight null")

	test(yahtzee, [5,5,5,5,5], 50, "Yahtzee")
	test(yahtzee, [1,2,3,1,4], 0, "Yahtzee null")

	test(chance, [1,2,3,4,5], 15, "Chance")

	print("\nPasses:")
	print(f"{passes}/{tests} = {int(passes/tests * 100)}%")
