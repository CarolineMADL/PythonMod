n1:int = 0
n2:int = 0


def oc():
    global oc
    if(n1==n2):
        print("Calculo invalido")
    elif(n1>n2):
        print(" A ordem crescente é",n2,n1)
    else:
        print("A ordem crescente é",n1,n2)


def main():
    global n1
    global n2
    n1=int(input("Coloque o primeiro número:"))
    n2=int(input("Coloque o segundo número:"))
    oc()


if(__name__ == "__main__"):
    main()