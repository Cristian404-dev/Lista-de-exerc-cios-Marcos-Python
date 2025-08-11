def extrair_nomes(lista_objetos):
    return [obj['nome'] for obj in lista_objetos if 'nome' in obj]

pessoas = [{'nome': 'Ana'}, {'nome': 'Carlos'}, {'idade': 30}, {'nome': 'João'}]
print(extrair_nomes(pessoas))