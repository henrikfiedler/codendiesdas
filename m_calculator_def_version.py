print("Geben Sie 2 Zahlen ein")
e1 = int(input("Zahl1 "))
e2 = int(input("Zahl2 "))
Operation=str(input("Welche Operation soll durchgeführt werden? "))
def add(e1,e2):
    Ausgabe=e1+e2
    return(Ausgabe)
def sub(e1,e2):
    Ausgabe=e1-e2
    return(Ausgabe)
def mul(e1,e2):
    Ausgabe=e1*e2
    return(Ausgabe)
def div(e1,e2):
    Ausgabe=e1/e2
    return(Ausgabe)
if(Operation == "+"):
    print(add(e1,e2))
elif(Operation == "-"):
    print(sub(e1,e2))
elif(Operation == "*"):
    print(mul(e1,e2))
elif(Operation == "/"):
    print(div(e1,e2))
    