def bmi_auswertung_m():

    '''Abgleich mit BMI Tabelle für Männer und das Ergebnis schreiben'''

    if BMI < 20:
        auswertung = "Du hast Untergewicht"
    elif BMI < 25:
        auswertung = "Du hast ein Normales Gewicht"
    else:
        auswertung = "Du hast Übergewicht"
    print(auswertung)

def bmi_auswertung_f():

    '''Abgleich mit BMI Tabelle für Frauen und Ergebnis schreiben'''

    if BMI < 19:
        auswertung = "Du hast Untergewicht"
    elif BMI < 24:
        auswertung = "Du hast ein Normales Gewicht"
    else:
        auswertung = "Du hast Übergewicht"
    print(auswertung)

# Einfuehrungstext des Programmes
print("Dieses Programm rechnet Ihren BMI(Body-Mass-Index) aus.")

# Fragt das Geschlecht ab
while True:
    geschlecht = input("Bist du Maskulin oder Feminin?(M/F):\n>> ").lower()
    if "m" == geschlecht or "f" == geschlecht:
        break
    else:
        print("Das ist kein Gültiges Geschlecht, bitte benutze M für Maskulin und F für Feminin")
        continue

# Fragt das Gewicht ab
gewicht = input("Dein Gewicht in Kilogramm\n>>")
gewicht = gewicht.replace(",", ".")
gewicht = float(gewicht)

# Fragt die Groesse ab
groesse = input("Deine Größe in Meter\n>>")
groesse = groesse.replace(",", ".")
groesse = float(groesse)

#Rechnet mit den Werten
BMI = gewicht / (groesse ** 2)

# Ausgabe des Ergebnisses der drüberliegenden Rechnung
print("Dein BMI beträgt:", round(BMI, 2))
if geschlecht == "m":
    bmi_auswertung_m()
else:
    bmi_auswertung_f()