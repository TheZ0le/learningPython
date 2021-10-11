# Aufgabe:
#       Das ist ein kurzes Script um festzustellen ob das
#       abgefragte Jah ein Schaltjahr ist oder nicht
#       beruht auf der Tatsache,
#       dass das Schaltjahr 1582 eingefuert wurde
#       und alle 4 Jahre ein schaltjahr ist
#       aber nicht wenn es durch 100 teilbar ist
#       aber doch wieder wenn es durch 400 teilbar ist

def SchaltJahr(Jahr):
    if Jahr < 1582:
        return False
    elif Jahr % 400 == 0:
        return True
    elif Jahr % 100 == 0:
        return False
    elif Jahr % 4 == 0:
        return True
    else:
        return False


print("------------------------Skript zur Berechnung von Schaltjahren.------------------------")
iJahr = int(input("Welches Jahr willst du Ueberpruefen?\n>>"))
print(SchaltJahr(iJahr))