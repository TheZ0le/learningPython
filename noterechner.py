def main():
    summe = 0
    i = 1

    while True:
        print("Bitte geben Sie die Note", i , "ein, wenn sie fertig sind geben sie ein '0' ein")
        note = float(input(">>"))
        if note == 0:
            break
        if note < 1 or note > 6:
            print("Ungültige Note. Bitte erneut eingeben.")
            continue
        summe = summe + note
        i = i + 1
    durchschnintt = summe / (i - 1)
    print("Der Durchschnitt beträgt:", round(durchschnintt, 1))

    nochmal = input("Möchtest du noch einen Durchschnitt berechen? (y/N)\n>>")
    if nochmal == "y":
        main()
    else:
         pass
main()