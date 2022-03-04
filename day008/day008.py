# Caeser Cipher Program

import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Create a function called 'caeser' that takes the 'text' and 'shift' as inputs.
 	#e.g.	"encode":	"hello" [5] => "mjqqt"
	#		"decode":	"mjqqt" [5] => "hello"
def caeser(start_text,shift_amount,cipher_direction):
	end_text=""
	if cipher_direction=="decode":
			shift_amount*=-1
	for char in start_text:
		if char in alphabet:
			position=alphabet.index(char)
			new_position=position+shift_amount
			end_text+=alphabet[new_position]
		else :
			end_text+=char				
	print(f"The {cipher_direction}d text is {end_text}")

print(art.logo)
#Try creating a while loop that continues to execute the program if the user types 'yes' and stop if 'no'. 
should_continue=True
while should_continue:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	#Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.
	shift%=25
	caeser(text,shift,direction)
	result=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
	if result=='no':
		should_continue=False
		print("Goodbye")