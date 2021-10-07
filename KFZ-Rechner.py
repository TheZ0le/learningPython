import math

def Benzin_Diesel():
    """
    Asks ccm, emission values and calculates and prints the vehicle tax
    """
    # Import Tax from global
    global tax

    # Checking for Benzin or Diesel price
    if drive_type == "benzin" or drive_type == "b":
        emission_price = 2
    else:
        emission_price = 9.5

    # Asking for arguments
    ccm = int(input("Wie viel ccm hat dein Fahrzeug?(Fahrzeugschein P.1)\n>>"))
    emission_value = int(input("Wie viel beträgt der Emmissionswert nach CO2-Ausstoß(Fahrzeugschein V.7)\n>>"))

    # Prepare to calc
    ccm = ccm // 100 + 1
    math.ceil(ccm)

    if emission_value <= 95:
        emission_value = 0
    else:
        emission_value = emission_value - 95

    # calc
    tax = emission_price * ccm + 2 * emission_value

    # prepare for printing
    round(tax)
    tax = str(tax)

    # Print tax
    print("----------------------------------------\n"
          "Du musst " + tax + " Euro Steuern zahlen!\n"
          "----------------------------------------")


def Elektro():

    """
        Asks  values and calculates and prints the vehicle tax
    """

    # Import tax from global
    global tax

    # Asking for arguments
    mass = int(input("Wie viel Gesamtmasse hat dein Auto?(Fahrzeugschein F.2)\n>>"))

    # Checking the tax class
    if mass >= 2000:
        mass = mass - 2000
        tax = 56.25
        if mass >= 1000:
            tax = tax + 30.05
            status = 1
            mass = mass - 1000
            if mass >= 501:
                print("Du befindest dich Ausserhalb der Elektro-Auto Klasse")
            else:
                pass
        else:
            status = 1
            pass
    else:
        status = 0
        pass

    mass = mass + 200


    # Calculate the tax
    if status == 0:
        while mass >= 200:
            tax = tax + 5.625
            mass = mass - 200
    elif status == 1:
        while mass >= 200:
            tax = tax + 6.01
            mass = mass - 200
    else:
        while mass >= 200:
            tax = tax + 6.39
            mass = mass - 200

    # Prepare to print
    tax = tax // 1
    tax = str(tax)

    # Print tax
    print("----------------------------------------\n"
          "Du musst " + tax + " Euro Steuern zahlen!\n"
          "----------------------------------------")






# Printing The Header
print("--------------------------------KFZ Steurrechner--------------------------------")

# Set global tax to 0
tax = 0

# Checking the car class
while True:
    drive_type = input("Für welche Art von Auto willst du dir Steuer berechnen?(Benzin / B, Diesel / D, Elektro / E)\n>>").lower()

    # Checking drive type
    if drive_type == "benzin" or drive_type == "diesel" or drive_type == "b" or drive_type == "d":
        Benzin_Diesel()
        break
    elif drive_type == "elektro" or drive_type == "e":
        Elektro()
        break
    else:
        print("Bitte gib ein passenden Typen an!")
        continue