v1:int = 0


def divisivel():
    global divisivel
    if(v1 % 2 == 0 and v1 % 3 == 0):
        print(f"{v1} é divisivel por 2 e 3")
    else:
        if(v1 % 2 == 0):
            print(f"{v1} é divisivel por 2")
        elif(v1 % 3 == 0):
            print(f"{v1} é divisivel por 3")
        else:
            print(f"{v1} não é divisivel nem por 2 nem por 3")


def main():
    global v1
    v1=int(input("Adicione um valor:"))
    divisivel()


if(__name__ == "__main__"):
    main()

