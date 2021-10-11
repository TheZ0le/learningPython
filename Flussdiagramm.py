# Aufgabe:
#       Erstelle Auf Basis eines Flussdiagrammes ein Python Skript
#       https://www.math.uni-bielefeld.de/~frettloe/teach/vorkurs/Aufgaben.pdf

def WorkingSys():
    print("Es gilt Ja = y / Nein = n") 
    status = input("Funktioniert das System?\n>>").lower()
    
    if status == "n":
        status = input("Bist du Schuld?\n>>").lower()
        if status == "y":
            print("Du Idiot")
            status = input("Hat es jemand gemerkt?\n>>").lower()
            if status == "y":
                print("Du bist am Arsch")
                status = input("Kannst du einem Anderen die Schuld zuschieben?\n>>")
                if status == "y":
                    print("Keine Sorge, jemand anderes ist am Arsch")
                else:
                    print("Du bist wirklich am Arsch")
            else:
                print("Man wird dich nicht finden")
        else:
            print("Dich trifft es nicht")
    else:
        print("Fummel nicht daran herum!\nAlles ist gut")

WorkingSys()