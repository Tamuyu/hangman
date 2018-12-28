#Hangman Game

import random

def hangman():
    questions = ["cat", "dog", "monkey", "rabbit"]
    random_number = random.randint(0,3)
    word = questions[random_number]
    wrong = 0
    stages = ["",
              "_____    ",
              "|   |    ",
              "|   |    ",
              "|   0    ",
              "|  /|\   ",
              "|  / \   ",
              "|        "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Please forecast one character."
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose! The answer is {}".format(word))

hangman()
