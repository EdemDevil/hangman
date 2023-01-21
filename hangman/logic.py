import random as r
import art as a
import words as w


end_of_game = False
lives = 6
chosen_word = r.choice(w.word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

print(a.logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        print('Вы угадали!')
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print('Этой буквы нет в слове')
        lives -= 1
    print(a.stages[lives])

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("\nYou win.")
    elif lives == 0:
        end_of_game = True
        print(f"Загаданное слово - {chosen_word}\nYou lose.")