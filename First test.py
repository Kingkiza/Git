#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.

a = input("what is your first number?")
b = input("what is your second number?")

a = int(a)
b = int(b)
c = (a+b)
message = f"the sum of {a} and {b} is {c}."
print(message)