gehalt = 3000
dienstjahre = 5
geschlecht = 'd'

# Aufgabe 1a
if gehalt > 1000:
    gehalt = gehalt + 200
else:
    gehalt *= 1.25
print ("Aufgabe 1a:", gehalt)


# Aufgabe 1b
if gehalt >= 1000 and gehalt <= 3000:
    gehalt *= 1.1
elif gehalt < 1000:
    gehalt *= 1.25
print ("Aufgabe 1b:", gehalt)


# Aufgabe 1c
gehalt = 4000
dienstjahre = 5
if gehalt < 2500 and dienstjahre < 5:
    gehalt += 200
elif gehalt < 5000 and dienstjahre >= 5 and dienstjahre <= 20:
    gehalt *= 1+ dienstjahre / 100
print("Aufgabe 1c:", gehalt)




# Aufgabe 1d
if geschlecht == 'w' or geschlecht == "W":
    print("Sie sind weiblich")
elif geschlecht.lower() == 'm':
    print("Sie sind männlich")
elif geschlecht.upper() == 'D':
    print("Sie sind divers")
else:
    print("Kein gültiges Geschlecht angegeben.")





#Aufgabe 1e siehe integriert in 1d

# Aufgabe 1f
testzyklen, fehleranzahl, bestanden = 100000, 66, False
if testzyklen == 100000 and fehleranzahl < 100:
    bestanden = True
    print("Test bestanden")
else:
    print("Test nicht bestanden")



# Aufgabe 2
zahl = 142112
if zahl % 2 == 0:
    print("Zahl ist gerade")
else:
    print("Zahl ist ungerade")



# ternary operator -> a if condition else b
print("Zahl ist gerade") if zahl % 2 == 0 else print("Zahl ist ungerade")
# ABER:



# Aufgabe 3
umsatz = float(input("Umsatz?>> "))
if umsatz > 100:
    if umsatz > 500:
        rabatt = 0.10
    else:
        rabatt = 0.05
else:
    rabatt = 0
rechnungsbetrag = umsatz * (1-rabatt)
print("Aufgabe 3:", umsatz, rechnungsbetrag)


# alternative Kürzung
if umsatz > 500:
    rabatt = .10
elif umsatz > 100:
    rabatt = .05
else:
    rabatt = 0
rechungsbetrag = umsatz * (1-rabatt)
print("Aufgabe 3 alternativ:", umsatz, rechnungsbetrag)

# Aufgabe 4
n1, n2, n3 = 4, 5, -3
maximum = n1
if maximum < n2:
     maximum = n2
if maximum < n3:
    maximum = n3
print("Aufgabe 4:", maximum)

#Variante mit built-in-function max()
maximum = max(n1,n2,n3)
print("Aufgabe 4:", maximum)




# Aufgabe 5
print("Bitte geben Sie U (Spannung), R (Widerstand), I (Stromstärke) ein, für die zu berechnende Größe")
inp = input(">> ")
if (inp.lower() == "u"):
    r = float(input(">> R in Ohm: "))
    i = float(input(">> I in Ampere: "))
    out = r * i
elif (inp.lower() == "r"):
    u = float(input(">> U in Volt: "))
    i = float(input(">> I in Ampere: "))
    out = u / i
elif (inp.lower() == "i"):
    r = float(input(">> R in Ohm: "))
    u = float(input(">> U in Volt: "))
    out = u / r
else:
    print("Kein gültige Eingabe!")
print("Aufgabe 5:", inp, "=", out)