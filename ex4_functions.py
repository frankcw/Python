
def helloWorld(myString):
	print (myString)
	myName = input("What is your name? ")
	myVar = input("Enter a number: ")
	if(myName == "Frank" and myVar != 0):
		print("Frank is great!")
	elif(myName == "Juan"):
		print("You dont work")
	else:
		print("You are ok")

helloWorld("Hello Function World")
helloWorld("Hello 2nd Function")


#mySting is defined under the argument being executed next to the function "helloWorld"