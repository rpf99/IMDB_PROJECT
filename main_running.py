from execucao_dados.perguntas import Funcoes


def obter_resposta():
    while True:
        print("\n1 - Lista dos Filmes\n2 - Melhor Nota\n3 - Pior Nota\n4 - Melhor Mais Antigo\n5 - Melhor Mais Recente\n6 - Média das Notas\n7 - Mais Longo\n8 - Mais Curto\n9 - Buscar Filme\n10 - Buscar Classificação\n11 - Encerrar\n")
        try:
            opcao = int(input("Escolha uma opção: "))
            if 1 <= opcao <= 11:
                return opcao
            else:
                print("Opção inválida. Escolha um número entre 1 e 11.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def buscar_classificacao(fnc):
    try:
        classf = input("Digite a classificação: ")
        return fnc.buscar_classificacao(classf)
    except ValueError:
        print("Opção Errada tente novamente")


def buscar_nome(fnc):
    try:
        nome = input("Digite o nome do filme que queira localizar: ")
        return fnc.buscar_nome(nome)
    except ValueError:
        print("Opção Errada tente novamente")



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
        "9": buscar_nome,
        "10": buscar_classificacao,
        "11": func.encerrar
    }

    while True:
        opcao = obter_resposta()
        
        if opcao == 11:
            opcoes[str(opcao)]()
        elif opcao in (9,10): 
            print(opcoes[str(opcao)](func))
        else:
            try:
                resposta = opcoes[str(opcao)]()
                print(resposta)
            except KeyError:
                print("Opção inválida. Escolha um número entre 1 e 11.")


if __name__ == "__main__":
    main()
