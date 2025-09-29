# - Modify suma_pozitive(lista) that can return and avg a positive numbers

def suma_pozitive(lista):
    # Functia primeste o lista de numere si returneaza suma numerelor pozitive din lista si media aritmetica a numerelor pozitive.
    suma = k = 0
    for numar in lista:
        if numar > 0:
            suma += numar
            k += 1
    return suma, suma/k

lista_numere = [-10, 5, -3, 2, 8, -1]
print("Lista de numere >>> " + str(lista_numere))
suma, media = suma_pozitive(lista_numere)
print("Suma cu numerelor pozitive din lista >>> ",suma)
print("Media aritmetica a numerelor pozitive din lista >>> ",media)
