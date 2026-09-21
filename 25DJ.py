#hi=hora incial hf=hora final mi=minuto inicial mf=minutos final dur_h=duração em horas dur_m=duração minutos
hi:int = 0
hf:int = 0
mi:int = 0
mf:int = 0
dur_h:int = 0
dur_m:int = 0

def duração():
    global duração
    global hf
    global mf
    global mi
    if(hf<hi):
        hf = hf + 24
    else:
        hf=hf
    if(mf<mi):
        mf=mf+60
        hf=hf-1
    dur_h=hf-hi
    dur_m=mf-mi
    print("O jogo durou %d hora(s) e %d minuto(s)"%(dur_h,dur_m))


def main():
    global hi
    global hf
    global mi
    global mf
    hi=int(input("Adicione a hora de inicio do jogo:"))
    hf=int(input("Adicione a hora final do jogo:"))
    mi=int(input("Adicione os minutos inciais:"))
    mf=int(input("Adicione os minutos finais:"))
    duração()


if (__name__ == "__main__"):
    main()