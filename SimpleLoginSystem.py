# This code is for a simple login system in python

n = input("Enter your name: ")     # for entering name
p = input("Enter your password: ") # for entering password
if n == "Priyanshu": # pre-defined username
	if p == "pass123": # pre-defined password
		print("Access Granted") # If the credentials matches than this will be executed

	else:
		print("Opps! Please Enter the right password") # if password does not matched than this will execute

else:
	print("Enter the right username and password") # if non of the credentials not matches than this will execute
