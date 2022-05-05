import math

liczba_figur = int(input())
suma = 0

def oblicz_pole(*args):
        if len(args) == 1:
            result = math.pi*args[0]**2
        elif len(args) == 2:
            result = args[0] * args[1]
        elif len(args) == 3:
            p = (args[0] + args[1] + args[2]) / 2
            result = math.sqrt(p*(p-args[0])*(p - args[1])*(p-args[2]))
        elif len(args) >= 4:
            print('Błąd: można podać maksymalnie 3 liczby')

        return result

for i in range(liczba_figur):
    try:
            x = input()
            x = x.split()
            x = [float(i) for i in x]
            suma += oblicz_pole(*x)
            print(round(suma, 2))
    except:
        pass

   