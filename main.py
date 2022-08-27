from Pila import Pila

if __name__ == "__main__":
    una_pila = Pila(int, 100)
    numero = int(input("Ingresa el numero: "))
    if numero == 0:
        una_pila.apilar(0)
    else:
        while numero != 0:
            bit = numero % 2
            numero = numero // 2
            una_pila.apilar(bit)
        cadena = ""
    while not una_pila.vacia():
        cadena += "{0}".format(una_pila.desapilar())
    print(cadena)