#nv= número de voltas em=extensão do circurto em metros
#dt_km=distância em km t_h=tempo em horas t_m=tempo em minutos

def calc_vl(v,m,t):
    dt_km= ( v * m ) / 1000
    t_h= t/60
    vl = dt_km/t_h
    return vl

def main():
    nv=int(input("Adicione o número de voltas:  "))
    t_m=float(input("Adicione o tempo em minutos: "))
    em=float(input("Adicione a extensão do circurto em metros: "))
    vm = calc_vl(nv,em,t_m)
    print(f"Velocidade média é {vm} km/h")


if(__name__ == '__main__'):
    main();


    

