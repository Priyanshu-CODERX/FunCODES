print("\n\nWelcome to P&A Tech Courses\n\n")
username = input("Username: ")
psswd = input("Password: ")
regpw = "pass123"
print("\n\n\n")
if username == "Priyanshu":
	if psswd == regpw:
		print("Welcome", username, "to our advance Programming Course system")
		print("1.Programming & Web Development Courses.....")
		print("2.Game Developement Courses")
		print("3.Graphic Designing & 3D Modelling & Sculpting")
		print("4.About")
		ch = int(input("Enter your choice: "))
		if ch == 1:
			print("\n\nWelcome to Programming Courses\n\n")
			print("1: Python: Full Course\n2: Java: Full Course\n3: C++: Full Course\n4: SqL: Full Course\n5: HTML & CSS: Full Course\n6: JavaScript: Full Course\n\n\n\nNote: More Courses are Coming Soon.....\n\n\n\nNote: Enter the following label to access the course....")
			numin = int(input("Enter the course ID: "))
			#Programming Course Options
			if numin == 1:
				print("Welcome to Python: Full Course")
				print("Price: Rs 3,999")
				print("Thanks, for buying this course")

			if numin == 2:
				print("Welcome to Java: Full Course")
				print("Price: Rs2,999")
				print("Thanks, for buying this course")		
	
			if numin == 3:
				print("Welcome to C++: Full Course")
				print("Price: Rs4,000")
				print("Thanks, for buying this course")		

			if numin == 4:
				print("Welcome to SqL: Full Course")
				print("Price: Rs2,999")
				print("Thanks, for buying this course")	
		
			if numin == 5:
				print("Welcome to HTML & CSS: Full Course")
				print("Price: Rs2999")
				print("Thanks, for buying this course")	

			if numin == 6:
				print("Welcome to JavaScript: Full Course")
				print("Price: Rs2999")
				print("Thanks, for buying this course")
			
		if ch == 2:
			print("1. Unity: Begineer\n2. Godot Engine: Full Course\n3. Unreal Engine: Begineer\n4. Cry Engine: Full Course")
			ch2 = int(input("Enter the course ID: "))
			if ch2 == 1:
				print("Welcome to Unity: Full Course")
				print("Price: Rs10,999")
				print("Thanks, for buying this course")

			if ch2 == 2:
				print("Welcome to Godot Engine: Full Course")
				print("Price: Rs4,999")
				print("Thanks, for buying this course")
			if ch2 == 3:
				print("Welcome to Unreal Engine: Begineer")
				print("Price: Rs5,999")
				print("Thanks, for buying this course")
			if ch2 == 4:
				print("Welcome to Cry Engine: Full Course")
				print("Price: Rs12,999")
				print("Thanks, for buying this course")
	
		
		if ch == 3:
			print("1.Photoshop & Illustrator: Full Course\n2.Blender: Basics - Advance\n3.Maya 3D: Full Course\n ")
			ch3 = int(input("Enter the course ID: "))	
			if ch3 == 1:
				print("Welcome to Photoshop & Illustrator: Full Course")
				print("Price: Rs12,999")
				print("Thanks, for buying this course")
			if ch3 == 2:
				print("Welcome to Blender: Basics - Advance course")
				print("Price: 5,999")
				print("Thanks! For buying this course")
			if ch3 == 3:
				print("Welcome to MAYA 3D: Full Course")
				print("Price: 7,500")
				print("Thanks! for buying this course")

		if ch == 4:
			print("\n\nHello I am a 15 year old student who loves programming and exploring new technologies")			
	else:
		print("Enter the right Username/Password")

else:
	print("Enter the right Username/Password")
