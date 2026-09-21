#t=tempo vm=velocidade média l=litros d= distancia

t:float = 0.0
d:float = 0.0
vm:float= 0.0
l:float = 0.0


def l():
    global l
    d = t * vm
    l = d/12
    print("A quantidade de litros gastado na viagem foi:",l)

def main():
    global t
    global d
    global vm
    t=float(input("Tempo de viagem em horas:  "))
    vm=float(input("Velocidade média:  "))
    l()

if (__name__ == "__main__"):
    main()

