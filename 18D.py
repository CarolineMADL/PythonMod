x:int = 0
y:int = 0
r:int = 0


def r():
    global r 
    if(x>y):
        r = x - y
        print("A diferença é:",r)
    elif(y>x):
        r = y - x
        print("A diferença é:",r)
    else:
        r = 0
        print("A diferença é:",r)

def main():
    global x
    global y
    x=int(input("Adicione um número: "))
    y=int(input("Adicione outro número: "))
    r()

if (__name__ == "__main__"):
    main()
