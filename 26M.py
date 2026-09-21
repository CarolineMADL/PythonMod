#ma=maior me=menor

n1:int = 0
n2:int = 0


def multiplo():
    global multiplo
    global ma
    global me
    if (n1>n2):
        ma=n1
        me=n2
    else:
        ma=n2
        me=n1
    if(me==0):
        print("Não é possível verificar")
    else:
        if(ma%me==0):
            print(f"{ma} é multiplo de {me}")
        else:
            print(f"{ma} não é multiplo de {me}")


def main():
    global n1
    global n2
    global ma
    global me
    n1=int(input("Adicione um primeiro número:"))
    n2=int(input("Adicione um segundo número:"))
    multiplo()


if(__name__ == "__main__"):
    main()