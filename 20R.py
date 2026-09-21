a:int= 0
b:int= 0
c:int= 0
x1:int= 0
x2:int = 0
def raizes():
    global a
    global b
    global c
    if(a==0):
        print("Valor invalido")
    else:
        delta = b**2 - 4 * a * c
        if delta < 0:
            print("Não existem raízes reais.")
        elif delta == 0:
            x = -b / (2 * a)
            print("Raiz única:", x)
        else:
            x1 = (-b + delta**0.5) / (2 * a)
            x2 = (-b - delta**0.5) / (2 * a)
            print("Raízes: X1 =", x1, "e X2 =", x2)


def main():
    global a
    global b
    global c
    a = float(input("Coeficiente A: "))
    b = float(input("Coeficiente B: "))
    c = float(input("Coeficiente C: "))
    raizes()


if __name__ == "__main__":
    main()