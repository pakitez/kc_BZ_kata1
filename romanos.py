simbolos = {
    "unidades" : ["","I", "II", "III", "IV","V", "VI","VII", "VIII", "IX" ],
    "decenas" : ["","X", "XX", "XXX", "XL","L", "LX","LX", "LXXX", "XC" ],
    "centenas" : ["","C", "CC", "CCC", "CD","D", "DC","DCC", "DCCC", "CM" ],
    "millares" : ["","M", "MMM", "MMM" ],
}

def validar(n):
    if not isinstance(n, int):
        raise ValueError("{} debe ser un entero".format(n))

    if n<0 or n > 3999:
        raise ValueError("{} debe estar dentro de rango".format(n))



def a_romano(n):

    validar(n)
    c = str(n)
    unidades = decenas = centenas = millares = 0
    
    if len(c) >=1:
        unidades = int(c[-1])

    if len(c) >=2:
        decenas = int(c[-2])

    if len(c) >=3:
        centenas = int(c[-3])

    if len(c) >=4:
        millares = int(c[-4])

    return simbolos["millares"][millares]+simbolos["centenas"][centenas]+simbolos["decenas"][decenas]+simbolos["unidades"][unidades]
