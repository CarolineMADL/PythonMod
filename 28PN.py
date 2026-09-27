pr_n:float = 0.00
def pa(m,a):
    if(m < 500 and a < 30):
        n=a*1.10
    elif(m>=500 and m<1000 and a>=30 and a<80):
        n=a*1.15
    elif(m>=1000 and a>=80):
        n=a*0.95
    else:
        n=a

    return n


def main():
    vm=int(input("Adicione o venda mensal:"))
    pr_a=int(input("Adicione o valor atual:"))
    pr_n=pa(vm,pr_a)
    print(f"O valor novo é {pr_n}")


if(__name__ == '__main__'):
    main();

