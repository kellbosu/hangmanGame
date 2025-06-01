import random

# select a word
random_words = [
    "lantern", "glimpse", "echo", "velocity", "marble",
    "thread", "plume", "jungle", "ripple", "ember",
    "groove", "mantle", "quartz", "harvest", "wander",
    "breeze", "whistle", "crimson", "shatter", "latch"
]

game_word = random.choice(random_words)

print(game_word)

# display correct letters 
# Displays the number of letters in the player's word
num_letters = (len(game_word))
spaces = ""

x = range(1, num_letters + 1)
for n in x:
    spaces += "_ "
print(spaces)


# ask for user input to guess a letter



# notify when wrong letter is selected

# keep track of lives

# continue to do this until either game over or win
