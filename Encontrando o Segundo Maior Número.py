def segundo_maior(lista):
    return sorted(set(lista))[-2]

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999,
           5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
print(segundo_maior(numeros))