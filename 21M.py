n1:float = 0.0
n2:float = 0.0
n3:float = 0.0
n4:float = 0.0
média:float = 0.0


def média():
    global média
    m=(n1+n2+n3+n4)/4
    if(m>=6):
        print("Aprovado com média:",m)
    elif(m>=3 and m<3):
        print("Exame com média:",m)
    else:
        print("Retido com média:",m)


def main():
    global n1
    global n2
    global n3
    global n4
    n1=float(input("Adicione a primeira nota:"))
    n2=float(input("Adicione a segunda nota:"))
    n3=float(input("Adicione a terceira nota:"))
    n4=float(input("Adicione a quarta nota:"))
    média()


if(__name__ == "__main__"):
    main()

