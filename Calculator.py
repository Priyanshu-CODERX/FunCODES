while True:
	print("Options: ")
	print("Enter 'add' for addition ")
	print("Enter 'sub' for substraction ")
	print("Enter 'mul' for multiply ")
	print("Enter 'div' for divide ")
	print("Enter 'quit' to Quit the program ")
	print("\n\n")
	ch = input("Enter Your Choice: ")
	print("\n")
	if ch == 'quit':
		break
	if ch == 'add':
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter another number: "))
		res = num1 + num2
		print("The addition of ", num1, "&", num2,": ", res,"\n\n")
	elif ch == 'sub':
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter another number: "))
		res = num1 - num2
		print("The substraction of ", num1, "&", num2,": ", res,"\n\n")
	elif ch == 'mul':
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter another number: "))
		res = num1 * num2
		print("The multiplication of ", num1, "&", num2,": ", res,"\n\n")
	elif ch == 'div':
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter another number: "))
		res = num1 / num2
		print("The division of ", num1, "&", num2,": ", res,"\n\n")
	else:
		print("Wrong Input\n\n")
