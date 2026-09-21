n1:int = 0
n2:int = 0
n3:int = 0
n4:int = 0


def notas():
    global notas
    if(n4>n3):
        print(n1,n2,n3,n4)
    elif(n4>n2):
        print(n1,n2,n4,n3)
    elif(n4>n1):
        print(n1,n4,n2,n3)
    else:
        print(n1,n2,n3,n4)


def main():
    global n1
    global n2
    global n3
    global n4
    n1=int(input("Adicione o primeiro número em ordem crescente:"))
    n2=int(input("Adicione o segundo número em ordem crescente:"))
    n3=int(input("Adicione o terceiro número em ordem crescente:"))
    n4=int(input("Adicione outro número qualquer:"))
    notas()


if(__name__ == "__main__"):
    main()