import random

# continue to do this until either game over or win
game_over = False
lives = 6

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

# Concatenates  for UI
def concat_word():
    working_word = ""
    for letter in spaces_left:
        working_word += letter
    print(working_word)

concat_word()
# ask for user input to guess a letter

guess = input("guess a letter: ")
for i, letter in enumerate(game_word):
    if letter == guess:
        print(f"Index {i}: {letter}")
        spaces_left[i] = guess
concat_word()


 

        



    

# display correct letters 

# notify when wrong letter is selected

# keep track of lives


