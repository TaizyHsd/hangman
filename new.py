import random

def hangman():
    key_words = ["Athena", "Aphrodite", "Apollon", "Artemis", "Ares", "Zeus",
                "Demeter", "Hestia", "Hephaistos", "Hera", "Hermes", "Poseidon",
                "Dionysos", "Hades", "Persephone"]
    random_number = random.randint(0,15)
    word = key_words[random_number]
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|       |       ",
              "|       0       ",
              "|      /|＼     ",
              "|      / ＼     ",
              "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}。".format(word))

print(hangman())
