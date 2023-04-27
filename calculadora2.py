unidades = ['bit', 'Byte', 'KB', 'MB', 'GB', 'TB', 'PB']

def converter(quantidade, unidade_inicial, unidade_final):
    indice_inicial = unidades.index(unidade_inicial)
    indice_final = unidades.index(unidade_final)
    if indice_inicial < indice_final:
        if unidade_inicial == "bit":
            numero = 1024 ** (indice_final - indice_inicial - 1)
            return (quantidade / 8) / numero
        else:
            numero = 1024 ** (indice_final - indice_inicial)
            return quantidade / numero
    elif indice_inicial > indice_final:
        if unidade_final == "bit":
            numero = 1024 ** (indice_inicial - indice_final - 1)
            return (quantidade * numero) * 8
        else:
            numero = 1024 ** (indice_inicial - indice_final)
            return quantidade * numero
    else:
        return quantidade

quantidade = float(input("Digite a quantidade a ser convertida: "))
unidade_inicial = input(f"Digite a unidade de entrada {unidades}:")

while not unidade_inicial in unidades:
    unidade_inicial = input(f"Valor invalido, digite a unidade de entrada {unidades}:")

unidade_final = input(f"Digite a unidade de saída {unidades}:")

while not unidade_final in unidades:
    unidade_final = input(f"Valor invalido, digite a unidade de saída {unidades}:")

print(f'{quantidade} {unidade_inicial} = {converter(quantidade, unidade_inicial, unidade_final):.14f} {unidade_final}')

