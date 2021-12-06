import random

def Ex1a():
    i = 1
    while i <=10:
        print(i)
        i = i + 1

def Ex1b():
    i = 1
    for i in range(1, 11):
        print(i)

def Ex2a():
    for i in range(4, 10):
        print(i)

def Ex2b():
    for i in range(4, 50, 5):
        print(i)

def Ex2c():
    for i in range(42, -8, -7):
        print(i)

def Ex3():
    zahl = int(input("1x1 von welcher Zahl?\n>>"))

    for i in range(1, 11):
        print(zahl * i)

def Ex5():
    print("Das hier ist ein Spiel wo du die Zahl von 1 - 100 erraten musst.")

    zahl = random.randrange(1, 101, 2)
    meine_zahl = 0
    dauer = 0

    while zahl != meine_zahl:
        dauer = dauer + 1
        meine_zahl = int(input("Welche Zahl denkst du ist es?\n>>"))

        if meine_zahl < zahl:
            print("Deine Zahl ist kleiner als die gegebene")
        elif meine_zahl > zahl:
            print("Deine Zahl ist größer als die gegebene")
        elif meine_zahl == zahl:
            print("Du hast die Zahl nach ", dauer, " versuch/en erraten")

def Ex6():
    eingabe = input("Bitte gebe eine Zahl an: ")

    try:
        zahl = int(eingabe)
    except:
        print("Error: Not accepted input")
    else:
        primzahl = True

    for i in range(2, zahl):
        if zahl % i == 0:
            primzahl = False
            break

    if primzahl:
        print("Es ist eine Primzahl!")
    else:
        print("Es ist keine Primzahl!")

def Ex7():
    print("---Schere, Stein, Papier---\n"
          "---------Best of 5---------\n")
    score_bot = 0
    score_p1 = 0

    while True:
        choice_bot = random.sample(("papier", "stein", "schere"),1)[0]

        print("------Scoreboard------\n"
              "Computer: ", score_bot, "You: ", score_p1)

        choice_p1 = input("Was möchtest du spielen (schere, stein, papier)\n>>").lower()
        print("Der Computer hat: ", choice_bot, " gespielt." )

        if choice_bot == "schere":
            if choice_p1 == "schere":
                print("Unentschieden, nocheinmal")
            elif choice_p1 == "stein":
                print("Du hast eine Runde Gewonnen")
                score_p1 = score_p1 + 1
            elif choice_p1 == "papier":
                print("Du hast eine Runde verloren")
                score_bot = score_bot + 1
        elif choice_bot == "stein":
            if choice_p1 == "stein":
                print("Unentschieden, nocheinmal")
            elif choice_p1 == "papier":
                print("Du hast eine Runde Gewonnen")
                score_p1 = score_p1 + 1
            elif choice_p1 == "schere":
                print("Du hast eine Runde verloren")
                score_bot = score_bot + 1
        elif choice_bot == "papier":
            if choice_p1 == "papier":
                print("Unentschieden, nocheinmal")
            elif choice_p1 == "schere":
                print("Du hast eine Runde Gewonnen")
                score_p1 = score_p1 + 1
            elif choice_p1 == "stein":
                print("Du hast eine Runde verloren")
                score_bot = score_bot + 1
        if score_bot == 3:
            print("Du hast verloren ", score_p1, " - ", score_bot)
            break
        elif score_p1 ==3:
            print("Du hast gewonnen ", score_p1, " - ", score_bot)
            break
        else:
            continue


while True:
    choose = input("Welche Aufgabe willst du ausfuehren?: (1a, 1b, 2a, 2b, 3, 5, 6, 7)\n>>")

    try:
        if choose == "1a":
            Ex1a()
        elif choose == "1b":
            Ex1b()
        elif choose == "2a":
            Ex2a()
        elif choose == "2b":
            Ex2b()
        elif choose == "3":
            Ex3()
        elif choose == "6":
            Ex6()
        elif choose == "7":
            Ex7()
    except:
        print("Ungültige eingabe")