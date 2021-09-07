# Einfuehrungstext des Prgrammes
print("Dieses Programm rechnet Ihren BMI(Body-Mass-Index) aus.")

# Daten: gewicht, groesse abfragen und in Variablen schreiben
gewicht = float(input("Dein Gewicht in Kilogramm: "))
groesse = float(input("Deine Größe in Meter: "))

# Erechnung des BMI
BMI = gewicht / (groesse ** 2)

# Ausgabe des Ergebnisses der drüberliegenden Rechnung
print("Dein BMI beträgt:")
print(BMI)
