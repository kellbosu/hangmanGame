import random
import os
import time


random_words = [
    "lantern", "glimpse", "echo", "velocity", "marble",
    "thread", "plume", "jungle", "ripple", "ember",
    "groove", "mantle", "quartz", "harvest", "wander",
    "breeze", "whistle", "crimson", "shatter", "latch"
]

# Selects a random word from list random_words
game_word = random.choice(random_words)
print(game_word)

# Displays the number of letters in the player's word
num_letters = (len(game_word))

# Stores spaces and correctly guessed letters
spaces_left = []
x = range(1, num_letters + 1)
for n in x:
    spaces_left.append("_ ")

####### Functions ##################
# Concatenates for UI
# display correct letters 
def concat_word():
    working_word = ""
    for letter in spaces_left:
        working_word += letter
    print(working_word)

# Clears screen for better UI
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


####### Game Functionality ##########
game_over = False
you_won = False
# keep track of lives
lives = 6

# Main loop. Continues until Game over or win.
while game_over is not True:
    clear_screen()
    print(game_word)
    lives_left = f"\nYou have {lives} lives left."
    print(lives_left)
    concat_word()
    if lives == 0:
        game_over = True
        break
    
    guess = input("\nguess a letter: ")
    # checks to see if the input letter has been guessed before
    if guess in spaces_left:
        lives -= 1
        # notify when wrong letter is selected
        print(f"Sorry, you've already guessed {guess}.")
        time.sleep(1)
    elif guess not in game_word:
        lives -= 1
        print(f"Sorry, {guess} is not one of the letters")
        time.sleep(1)
    else:
        for i, letter in enumerate(game_word):
            if letter == guess:
                spaces_left[i] = guess
        if "_ " not in spaces_left:
            concat_word()
            you_won = True
            game_over = True
            break

if you_won == True:
    print("""
      //////////
      YOU WON!
    //////////
      """)
else:
    print("""
    //////////
    GAME OVER
    //////////
        """)



 

        



    








