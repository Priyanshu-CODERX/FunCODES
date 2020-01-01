# Guessing Game using for-loop

import random

print("Hint: The value is an integer and lies between 1-10")
guess_num = random.randint(1, 10)
for i in range(0,3):
	guess = int(input("Guess: "))
	if guess == guess_num:
		print("Right Guess")
		break
	else:
		print("TryAgain!\n Wrong Guess")
		if i == 2:
			print("The answer was:", guess_num)
