def rechner():

    # Zahlen und operator eingeben
    Zahl1 = int(input('Erste Zahl: '))

    operation = input('''
   ..............................
   : Was möchtest du rechnen?:  :
   :     + für Addition         :
   :     - für Subtraktion      :
   :     * für Multiplikation   :
   :     / für Division         :
   ..............................
   Ihr Operator:    ''')

    Zahl2 = int(input('Zweite Zahl: '))

    # Addition
    if operation == '+':
        print('{} + {} = '.format(Zahl1, Zahl2))
        print(Zahl1 + Zahl2)

    # Subtraktion
    elif operation == '-':
        print('{} - {} ='.format(Zahl1, Zahl2))
        print(Zahl1 - Zahl2)

    # Multiplikation
    elif operation == '*':
        print('{} * {} ='.format(Zahl1,Zahl2))
        print(Zahl1 * Zahl2)

    # Division
    elif operation == '/':
        print('{} / {} ='.format(Zahl1, Zahl2))
        print(Zahl1 / Zahl2)

    # Falscher Operator
    else: print('Rechnung konnte aufgrund eines falschen Operators nicht durchgeführt werden')

    abfrage()

#Nochmal rechnen?
def abfrage():
    nochmal = input('Möchtest du noch etwas rechen? [y/n]: ').lower()

    if nochmal == 'y':
        rechner()
    
    else: exit

rechner()