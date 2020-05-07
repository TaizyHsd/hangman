import random

def hangman():
    key_words = ["Athena", "Aphrodite", "Apollon", "Artemis", "Ares", "Zeus",
                "Demeter", "Hestia", "Hephaistos", "Hera", "Hermes", "Poseidon",
                "Dionysos", "Hades", "Persephone"]
    word = random.choice(key_words)
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
    print("ハングマンへようこそ！お題はギリシア神話の神々の一人です")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね: "
        char = input(msg)
        if char in rletters:
            c_idx = rletters.index(char)
            board[c_idx] = char
            rletters[c_idx] = "$"
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
