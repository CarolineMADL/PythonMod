vc:float = 0.00
def investimento(t,vl):
    if (t==1):
        vt=vl*1.03
        print("O valor do rendimento :")
    else:
        vt=vl*1.05
        print("O valor do rendimento :")
    return vt


def main():
    print("Escolha o tipo de investimento: ")
    print("[1] Poupança")
    print("[2] Renda Fixa")
    print("Se escolher outro número que não seja 1 ou 2 ele considera que é renda fixa.") 
    esc=int(input("Digite a opção desejada:"))
    vi=float(input("Digite o valor inicial investido:"))
    vc = investimento(esc,vi)
    print(f"{vc}")


if(__name__ == '__main__'):
    main();
    
    
    