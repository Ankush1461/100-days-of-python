############DEBUGGING#####################

# # Describe Problem
def my_function():
  for i in range(1, 21): #Prev: for i in range(1,20)=> range doesn't include the end limit.
    if i == 20:
      print("You got it")
my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 5) #Prev: dice_num = randint(1, 6) => dice_images can go only from 0 to 5 and randint gives random value between the two numbers including them
print(dice_imgs[dice_num])

# # Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994: #Prev: elif year > 1994: => If year=1994, all conditions get skipped
  print("You are a Gen Z.")

# # Fix the Errors
age = int(input("How old are you?")) #Prev: age = input("How old are you?")=> input function takes input as string.
if age > 18:
 print(f"You can drive at age {age}.") # Prev: Wrong Indentation and fstring was not used

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) #Prev: word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)

# #Use a Debugger
def mutate(a_list):
	b_list = []
	for item in a_list:
		new_item = item * 2
		b_list.append(new_item) #Prev: Wrong indentation putting this line out of the loop resulting b_list=[26]
	print(b_list)

mutate([1,2,3,5,8,13])


#Exercise 1:
num = int(input("Which number do you want to check?"))

if num % 2 == 0: #Prev: if num % 2 = 0: => "=" is an assignment operator
  print("This is an even number.")
else:
  print("This is an odd number.")


#Exercise 2:
year = int(input("Which year do you want to check?")) #Prev: year = input("Which year do you want to check?") => input function takes input as string.

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

#Exercise 3:
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: #Prev: if number % 3 == 0 or number % 5 == 0: => "or" executes statement if any of the conditions are True.
    print("FizzBuzz")
  elif number % 3 == 0: #Prev: if number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0: #Prev: if number % 5 == 0:
    print("Buzz")
  else:
    print(number) #Prev: print([number])