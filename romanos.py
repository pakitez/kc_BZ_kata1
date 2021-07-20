simbolos = {
    "unidades" : ["","I", "II", "III", "IV","V", "VI","VII", "VIII", "IX" ],
    "decenas" : ["","X", "XX", "XXX", "XL","L", "LX","LX", "LXXX", "XC" ],
    "centenas" : ["","C", "CC", "CCC", "CD","D", "DC","DCC", "DCCC", "CM" ],
    "millares" : ["","M", "MMM", "MMM" ],
}

diccionario = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000,}

def validar(n):
    if not isinstance(n, int):
        raise ValueError("{} debe ser un entero".format(n))

    if n<0 or n > 3999:
        raise ValueError("{} debe estar dentro de rango".format(n))

"""def validarRomano(cadena):
    contadorCaract = 0
    if len(caracter)>15:
        raise ValueError("{} no puede tener más de 15 caracteres".format(cadena))
    for caracter in cadena:
        if caracter 
    
"""


def a_romano(n):

    validar(n)
    c = str(n)
    unidades = decenas = centenas = millares = 0

    
    c4digitos = ("{:04d}".format(n))
    unidades = int(c4digitos[-1])
    decenas = int(c4digitos[-2])
    centenas = int(c4digitos[-3])
    millares = int(c4digitos[-4])

    """
    
    if len(c) >=1:
        unidades = int(c[-1])

    if len(c) >=2:
        decenas = int(c[-2])

    if len(c) >=3:
        centenas = int(c[-3])

    if len(c) >=4:
        millares = int(c[-4])

"""

    return simbolos["millares"][millares]+simbolos["centenas"][centenas]+simbolos["decenas"][decenas]+simbolos["unidades"][unidades]

def a_numero(romano):
    total = 0
    valorAnt = 0
    for caracter in romano:
        valor = diccionario[caracter]
        if valor > valorAnt:
            if valorAnt in(5,50,500):
                raise ValueError("{} No se puede restar V, L, D ".format(romano))

            if valorAnt > 0 and valor > 10 * valorAnt:
                raise ValueError("{} No se puede restar con un salto mayor a un orden de magnitud ".format(romano))
            
            total -= valorAnt
            total += valor - valorAnt
        else:
            total += valor 

        valorAnt = valor
    
    return total
