#m=maior
n1:float = 0.0
n2:float = 0.0
m:float = 0.0

def m():
    global m
    if(n1>n2):
        m=n1
        print("O numero maior é",n1)
    else:
        m=n2
        print("O número maior é",n2)


def main():
    global n1
    global n2
    n1=float(input("Adicione um número: "))
    n2=float(input("Adicione outro número: "))
    m()

if (__name__ == "__main__"):
    main()
    