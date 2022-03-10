#Higher Lower Game

from art import logo, vs
from game_data import data
import random

#install replit package before importing
from replit import clear

#Generate a random account from the game data
def get_random_account():
  """Get data from random account"""
  return random.choice(data)
	

# Format the account data into printable format
def format_data(account):
	"""Format account into printable format: name, description and country"""
	name = account["name"]
	description = account["description"]
	country = account["country"]
	return f"{name}, a {description}, from {country}"

##Use if statement to check if user is correct.
def check_answer(guess, a_followers, b_followers):
	"""Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
	if a_followers > b_followers:
		return guess == "a"
	else:
		return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

	#Make the game repeatable
  while game_should_continue:

	#Making account at position B become the next account at position A.
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
	#Ask user for a guess
    guess=input("Who has more followers? Type 'A' or 'B': ").lower()

	#Check if the user is right.
	##Get the follower count of each account.
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
	
	
	#Clear the screen between the rounds.
    clear()
	
	#Display art
    print(logo)
	
	#Give user feedback on their guess.
    if is_correct:
                
        #Score keeping
        score+=1
        print(f"You are right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue=False

game()