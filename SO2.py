def fatorial(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    return f

def divisão(a,b):
    return a/b

def main():
    n=int(input("Adicione o número para obter a soma em serie fatorial: "))
    soma=1.0
    for i in range(1,n+1):
        fat=fatorial(i)
        termo=divisão(1,fat)
        soma = soma + termo
    print("A soma fatorial em série é :", round(soma,4))


if(__name__ == '__main__'):
    main();

