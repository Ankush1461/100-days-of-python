#PyCalculator Program

from art import logo

#install replit package before importing
from replit import clear

def sum(n1,n2):
	return n1+n2

def subtract(n1,n2):
	return n1-n2

def multiply (n1,n2):
	return n1*n2

def divide(n1,n2):
	return n1/n2

def remainder(n1,n2):
	return n1%n2

def power(n1,n2):
	return n1**n2
	
operations={
	"+": sum,
	"-": subtract,
	"*": multiply,
	"/": divide,
	"%": remainder,
	"^": power
}

def calculator():
	print(logo)
	num1=float(input("What's the first number?"))
	for operator in operations:
		print(operator)
	should_continue=True
	while should_continue:
		operation_symbol=input("Pick an operation: ")
		num2=float(input("What's the next number?"))
		calculation_function=operations[operation_symbol]
		answer= calculation_function(num1,num2)
		print(f"{num1} {operation_symbol} {num2} = {answer}")
		if input(f"Type 'y' to continue calculation with {answer} or 'n' to start a new calculation.")=="y":
			num1=answer
		else:
			should_continue=False
            clear()
			calculator()

calculator()