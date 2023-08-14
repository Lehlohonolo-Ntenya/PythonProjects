import random

from arts import logo
print(logo)
# Randomly choose a word from a list of words
word_list = ['cat','car','dog','doctor','cow','elephant','lion','tiger','mouse','snake','chicken','sheep','goat','pig','horse','donkey','rat']
chosen_word = random.choice(word_list)

lives = 6

# guess the letters in the word

display = []
for _ in range(len(chosen_word)):
    display += '_'
print(display)
end_game = False

while not end_game:
    guess = input("What is your guess of the letter in the word? ").lower()
# replace the '_' with the letter iif the letter is in the word.
    for position in range(len(chosen_word)):

        letter = chosen_word[position]

        if guess == letter:
            display[position] = letter
    print(display)
    if '_' not in display:
        print("Congradulations, you win!!")
        end_game = True
    from arts import life
    if guess not in chosen_word:
        lives -=1
        print("Try again! You have lost a life!")
        print(life[lives])
        if lives==0:
            print("You lose !!!!!!")
            end_game =True










# Repeat this until all the '_' are replaced with letters. Prompt user they win
