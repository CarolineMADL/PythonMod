def fat(n1):
    ft=1
    for a in range (1,n1+1,1):
        ft= ft * a
    return ft

def main():
    n=int(input("Adicione um número: "))
    nu=fat(n)
    print(f"O fatorial desse número é {nu}")

if(__name__ == '__main__'):
    main();
