def obtain_moneyWeek(dinero, porcentaje):
    numPorcentaje = dinero * ( porcentaje / 100)
    return round(dinero + numPorcentaje, 2), round(numPorcentaje, 2)

def dc (num):
    n1, n2 = str(num).split('.')
    text = ''
    
    for x, y in enumerate( n1[::-1] ):
        if x % 3 == 0:
            text += '\'' if x%6 == 0 else '.'
        text += y

    return text[1:len(text)][::-1] + ',' + n2

def print_weeks(semanas, dinero, porcentaje):
    meses = 0
    for x in range(semanas):
        ganancia, nump = obtain_moneyWeek(dinero, porcentaje)

        if x % 4 == 0: 
            meses += 1
            print(f'\n Mes {meses}')


        print(
        f'Semana {x+1}: {dc(dinero)} + {dc(nump)} ({porcentaje}%) = {dc(ganancia)}'
        )
        
        dinero = ganancia
    print()

# COP
print_weeks(
    semanas = 4 * 12,
    dinero = 1000.00 * 300.00,
    porcentaje = 7
)

# USD
# print_weeks(
#     semanas = 4 * 12,
#     dinero = 100.00,
#     porcentaje = 25
# )

# Semana 1:     300.000,0 +   75.000,0 (25%) = 375.000,0
# (N. Semana): (invertir) + (ganancia) (25%) = (dinero total para re-invertir)
