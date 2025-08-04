

# 1 - Encontrar o número de telefone para esse nome
def encontrar_numero_por_nome(lista, nome):
    inicio = 0
    fim = len(lista) - 1
    chutes = 0

    while inicio <= fim:
        chutes += 1
        meio = (inicio + fim) // 2
        nome_lista = lista[meio]["nome"].lower().replace(" ", "")

        if nome_lista == nome:
            nome = lista[meio]["nome"].title()
            print(f"O(a) usuário(a) {nome} tem o número de telefone: {lista[meio]['telefone']}")
            print(f"O algoritmo chutou {chutes} vezes")
            break
        elif nome_lista < nome:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None

