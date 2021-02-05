def lerArquivo(nome_arquivo):
    try:
        ref_arquivo = open(nome_arquivo, 'r')
        data = ref_arquivo.read()
    except ValueError:
        print('Erro ao tentar manipular arquivo {}'.format(ValueError))
    finally:
        ref_arquivo.close()
    return data


def escreverArquivo(nome_arquivo, novo_model):
    try:
        arquivo = open(nome_arquivo, 'w')
        arquivo.write(novo_model)
    except ValueError:
        print('Erro ao tentar manipular arquivo {}'.format(ValueError))
    finally:
        arquivo.close()


def escrever_abaixo(nome_arquivo, novo_model):
    try:
        arquivo = open(nome_arquivo, 'a')
        arquivo.write(novo_model)
    except ValueError:
        print('Erro ao tentar manipular arquivo {}'.format(ValueError))
    finally:
        arquivo.close()