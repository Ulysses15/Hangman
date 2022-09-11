import random
import string


def checking_letter(word, letter, guess):
    k = 0
    new_guess = ''
    while k < len(word):
        if guess[k] == '-':
            if word[k] == letter:
                new_guess = new_guess + word[k]
            else:
                new_guess = new_guess + '-'
            k += 1
        else:
            new_guess = new_guess + guess[k]
            k += 1
    return new_guess


def intro(start_word, win, lost):
    next_step = True
    print("H A N G M A N")
    options = ['play', 'results', 'exit']
    while next_step:
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        user_input = input()
        if user_input == options[0]:
            print('-' * len(start_word))
            next_step = False
        elif user_input == options[1]:
            print("You won: {} times.".format(win))
            print("You lost: {} times.".format(lost))
        elif user_input == options[2]:
            return 1
        else:
            continue


counter_won = 0
counter_lost = 0
words = ['python', 'java', 'swift', 'javascript']
hangman = True
# print(not intro(chosen_word, counter_won, counter_lost))
while hangman:
    chosen_word = words[random.randint(0, 3)]
    dashes = '-' * len(chosen_word)
    missing_letters = ''
    i = 0
    if intro(chosen_word, counter_won, counter_lost) == 1:
        hangman = False
    else:
        while i < 7:
            print('Input a letter:')
            letter = input()
            if len(letter) > 1 or len(letter) == 0:
                print("Please, input a single letter.")
                print(dashes)
            elif letter not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
                print(dashes)
            elif chosen_word.count(letter) == 0:
                if letter in missing_letters:
                    print("You've already guessed this letter.")
                    print(dashes)
                else:
                    i += 1
                    print("That letter doesn't appear in the word.")
                    print()
                    print(dashes)
                missing_letters += letter
            elif letter in dashes:
                print("You've already guessed this letter.")
                print()
                print(dashes)
                i += 1
            else:
                dashes = checking_letter(chosen_word, letter, dashes)
                if '-' not in dashes:
                    counter_won += 1
                    print(dashes)
                    print('You guessed the word {}!'.format(dashes))
                    print('You survived!')
                    break
                else:
                    print(dashes)
        while i < 8:
            if '-' not in dashes:
                break
            print('Input a letter:')
            letter = input()
            if len(letter) > 1 or len(letter) == 0:
                print("Please, input a single letter.")
                print(dashes)
            elif letter not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
                print(dashes)
            elif chosen_word.count(letter) == 0:
                if letter in missing_letters:
                    print("You've already guessed this letter.")
                else:
                    counter_lost += 1
                    print(dashes)
                    print("That letter doesn't appear in the word.")
                    print('You lost!')
                    break
            elif letter in dashes:
                counter_lost += 1
                print("No improvements.")
                print()
                print('You lost!')
                break
            else:
                dashes = checking_letter(chosen_word, letter, dashes)
                if '-' not in dashes:
                    counter_won += 1
                    print(dashes)
                    print('You guessed the word {}!'.format(dashes))
                    print('You survived!')
                    break
                else:
                    print(dashes)


