print("Geben Sie 2 Zahlen ein")
Eingabe1 = int(input("Zahl1 "))
Eingabe2 = int(input("Zahl2 "))
Operation=str(input("Welche Operation soll durchgeführt werden? "))
if(Operation == "+"):
    Ausgabe = Eingabe1+Eingabe2
    print(Ausgabe)
elif(Operation == "-"):
    Ausgabe=Eingabe1+Eingabe2
    print(Ausgabe)
elif(Operation == "/"):
    Ausgabe=Eingabe1/Eingabe2
    print(Ausgabe)
elif(Operation == "*"):
    Ausgabe=Eingabe1*Eingabe2
    print(Ausgabe)
else:
    print("falsche Eingabe")