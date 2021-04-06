import ttg

"""Função que realiza a conversão da tabela, recebendo  """
def conversao(valor, *list):

    convert = ttg.Truths([*list], [f"{valor}"])

    return convert

"""Função chama a função que realiza a conversão, passando como parametro a string digitada e a quantidade de caracter"""
def entrada_valor(entrada, validacao):

    if validacao == 5:
        return conversao(entrada, 'a', 'b','c','d','e')
    if validacao == 4:
        return conversao(entrada, 'a', 'b','c','d')
    if validacao == 3:
        return conversao(entrada, 'a', 'b','c')
    if validacao == 2:
        return conversao(entrada, 'a', 'b')
    if validacao == 1:
        return conversao(entrada, 'a')

