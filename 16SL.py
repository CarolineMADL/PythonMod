#d=desconto sb=salario bruto sl=salario liquído
#pd= percentual de desconto 
#ht=horas trabalhadas vh=valor por hora
#nd=número de dependentes


ht:int = 0
vh:int = 0
pd:int = 0
nd:int = 0
sl:float = 0.0
sb:float=0.0


def sl():
   global sl
   sb=ht*vh
   d=sb*(pd/100)
   sl=(sb-d)+ (nd*100)
   print("O salario liquído é ",sl)

def main():
  global ht
  global vh
  global pd
  global nd 
  ht=int(input("Horas Trabalhadas:  "))
  vh=int(input("Valor por horas:  "))
  pd=int(input("Percentual de desconto:  "))
  nd=int(input("Número de dependentes:  "))
  sl()

if (__name__ == "__main__"):
  main()

  
  

