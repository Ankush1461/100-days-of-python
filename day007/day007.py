
import random
import hangman_art
import hangman_words

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives=6

print(hangman_art.logo)


print(f"Chosen word:{chosen_word}")

#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display=[]
for _ in range(word_length):
	display+="_"



#Use a while loop to let the user guess again. 
#The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
#Then you can tell the user they've won.
end_of_game=False
while not end_of_game:
  #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  guess=input("Guess a letter: ").lower()
  #If the user has entered a letter they've already guessed, print the letter and let them know.
  if guess in display:
    print(f"You've already guessed {guess}")
  #Loop through each position in the chosen_word;
  #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
  #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
  for position in range(word_length):
    letter = chosen_word[position]
    # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
      display[position] = letter
  #If guess is not a letter in the chosen_word,
  #Then reduce 'lives' by 1. 
  #If lives goes down to 0 then the game should stop and it should print "You lose."
  if guess not in chosen_word:
    #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives-=1
    if lives==0:
      end_of_game=True
      print("You lost!")

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
        end_of_game = True
        print("You win.")

  #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
  print(hangman_art.stages[lives])
