# - Write a function numere_pare(lista) what return a sum of all positive number from list

def suma_pozitive(lista):
    # Functia primeste o lista de numere si returneaza suma numerelor pozitive din lista.
    suma = 0
    for numar in lista:
        if numar > 0:
            suma += numar
    return suma

lista_numere = [-10, 5, -3, 2, 8, -1]

print("Lista de numere >>> " + str(lista_numere))
print("Suma cu numerelor pozitive din lista >>> ",suma_pozitive(lista_numere))"""
