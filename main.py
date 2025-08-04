from Chapter_1.pesquisa_binaria import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    lista_nomes_telefone = [
        {"nome": "Ana Flavia", "telefone": "(11) 98765-4321", "operadora": "Vivo"},
        {"nome": "Douglas Ide", "telefone": "(21) 99123-4567", "operadora": "TIM"},
        {"nome": "Fernanda Ribeiro", "telefone": "(31) 99876-1234", "operadora": "Claro"},
        {"nome": "Thiago Vasques", "telefone": "(41) 99654-7890", "operadora": "Oi"},
        {"nome": "Juliana Castro", "telefone": "(61) 98456-3210", "operadora": "Vivo"},
        {"nome": "Marcos da Silva", "telefone": "(51) 99777-8888", "operadora": "TIM"},
        {"nome": "Sabrina Moura", "telefone": "(71) 99333-2222", "operadora": "Claro"},
        {"nome": "Eduardo Martins", "telefone": "(91) 99900-1100", "operadora": "Oi"},
        {"nome": "Patrícia Nogueira", "telefone": "(85) 99888-6655", "operadora": "Claro"},
        {"nome": "Rafael Antunes", "telefone": "(27) 99666-4433", "operadora": "Vivo"}
    ]

    nome = input("Digite o nome que deseja encontrar na lista telefonica")

    # Tratar os dados para garantir que procure de forma correta na lista
    nome = nome.lower().replace(" ","")

    # Resolvendo o exercício 1 dos Algoritmos
    encontrar_numero_por_nome(lista_nomes_telefone, nome)