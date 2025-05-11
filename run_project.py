from execucao_dados.perguntas import Funcoes
from time import sleep


def obter_resposta():
    print("\n1 - Lista dos Filmes\n2 - Melhor Nota\n3 - Pior Nota\n4 - Melhor Mais Antigo\n5 - Melhor Mais Recente\n6 - Média das Notas\n7 - Mais Longo\n8 - Mais Curto\n9 - Buscar Filme\n10 - Buscar Classificação\n11 - Filmes por Década\n12 - Média por Classificação\n13 - Encerrar\n")

    try:
        opcao = int(input("Escolha uma opção: "))
        return opcao
    except ValueError:
        print("Opção inválida. Digite um número.\n")


def busca_filme(func):
    try:
        nome = input("Digite o nome do filme: ")
        return func.buscar_nome(nome)
    except ValueError:
        print("Opção inválida. Deveria ser um nome")


def classificacao(func):
    try:
        classf = input("Digite a classificação: ")
        return func.buscar_classificacao(classf)
    except ValueError:
        print("Entrada inválida. Deveria ser uma string")


def busca_decada(func):
    try:
        decada = int(input("Digite a decada: "))
        if decada % 10 == 0 and decada >= 1900:
            return func.filmes_decada(decada)  
        
    except ValueError:
        print("Entrada inválida. Deveria ser uma decada depois ou igual a 1900")


def main():
    func = Funcoes()

    opcoes = {
        "1": func.lista_completa,
        "2": func.melhor_opcao,
        "3": func.pior_opcao,
        "4": func.melhor_mais_antigo,
        "5": func.melhor_mais_recente,
        "6": func.media_notas,
        "7": func.mais_longo,
        "8": func.mais_curto,
        "9": lambda: busca_filme(func),
        "10": lambda: classificacao(func),
        "11": lambda: busca_decada(func),
        "12": func.media_classificacao,
        "13": func.encerrar
    }

    while True:
        sleep(5)
        opcao = obter_resposta()
        
        if opcao == 13:
            opcoes[str(opcao)]()
            break
        else:
            try:
                resposta = opcoes[str(opcao)]()
                print("\n",resposta)
            except ValueError:
                print("Entrada inválida. Deveria ser um número.")
            except KeyError:
                print("Opção invá1lida. Escolha um número entre 1 e 11.")
            
if __name__ == "__main__":
    main()
