from execucao_dados.inclusao import adicao_tabela, cursor

class Funcoes:
    
    def __init__(self):
        adicao_tabela()
        self.cr = cursor


    def _executar_query(self, query, find_all_values=True):
        """ Função para executar as querys no banco de dados"""
        self.cr.execute(query)
        return self.cr.fetchall() if find_all_values else self.cr.fetchone()


    def lista_completa(self):
        filmes = self._executar_query("SELECT * FROM imdb_table")
    
        return "\n".join([f'{x[0]} ({x[2]}) Nota: {x[1]} Duração: {x[3]} Classificação: {x[4]}' for x in filmes])


    def melhor_opcao(self):
        """ Retorna o filme com a maior nota"""

        resp = self._executar_query(
            "SELECT nome,nota FROM imdb_table ORDER BY nota DESC", 
            find_all_values=False)

        return f"O filme com melhor nota é '{resp[0]}', com nota {resp[1]}"


    def pior_opcao(self):
        """ Retorna o filme com a menor nota"""

        resp = self._executar_query(
            "SELECT nome,nota FROM imdb_table ORDER BY nota ASC limit 1", 
            find_all_values=False)
        
        return f"O filme com a pior nota é '{resp[0]}', com nota {resp[1]}"


    def melhor_mais_recente(self):
        """ Retorna o filme mais recente"""

        resp = self._executar_query(
            "SELECT nome,lancamento FROM imdb_table ORDER BY lancamento DESC limit 1", find_all_values=False)
        
        return f"O filme mais recente é '{resp[0]}', lançado em {resp[1]}"
    

    def melhor_mais_antigo(self):
        """ Retorna o filme mais antigo"""

        filme = self._executar_query(
            "SELECT nome,lancamento FROM imdb_table ORDER BY lancamento ASC limit 1", 
            find_all_values=False)
        
        return f"O filme mais antigo é '{filme[0]}', lançado em {filme[1]}"


    def media_notas(self):
        """ Retorna a média das notas dos filmes """
        
        media = self._executar_query("SELECT AVG(nota) FROM imdb_table")
        return f'A nota média dos filmes é {round(media[0][0],2)}'


    def mais_longo(self):
        """ Retorna o filme mais longo """

        filme = self._executar_query(
                    "SELECT nome, duracao FROM imdb_table ORDER BY duracao DESC limit 1", 
                    find_all_values=False)
        
        return f"O filme mais longo é '{filme[0]}', com {filme[1]}"
     

    def mais_curto(self):
        """ Retorna o filme mais curto """

        filme = self._executar_query(
                    "SELECT nome, duracao FROM imdb_table ORDER BY duracao ASC limit 1", 
                    find_all_values=False)
        
        return f"O filme mais curto é '{filme[0]}', com {filme[1]}"
     

    def buscar_nome(self, nome):
        """ Retorna os filmes pelo nome """

        filmes = self._executar_query(
            f'SELECT nome,lancamento from imdb_table WHERE lower(nome) LIKE "%{nome.lower()}%"')
        
        if filmes:
            return f'Os filmes que possuem o nome {nome} são:\n'\
                f"{'\n'.join([f'{x[0]} ({x[1]})' for x in filmes])}"    
        
        return f"Lamento, mas o filme '{nome}' não foi encontrado"


    def buscar_classificacao(self, classf):
        """ Retorna os filmes pela classificação """

        filmes = self._executar_query(
            f'SELECT nome,lancamento from imdb_table WHERE lower(classificacao) LIKE "%{classf.lower()}%"')
        
        if filmes:

            return f'Os filmes que possuem a classificação {classf} são:\n'\
                f'{"\n".join([f'{x[0]} ({x[1]})' for x in filmes])}'

        return f"Lamento, mas a classificação '{classf}' não foi encontrada"


    def media_classificacao(self):
        """ Retorna a média das notas de cada classificação """

        filmes = self._executar_query("""
            SELECT classificacao, AVG(nota) as media_classficacao 
            from imdb_table group by classificacao
            """
        )
        
        return "\n".join([f'Classificação: {x[0]} Media Nota: {round(x[1],2)}' for x in filmes])

    def filmes_decada(self, decada): 
        """ Retorna os filmes pela decada """

        query = f"""
            SELECT nome,lancamento,classificacao from imdb_table
            WHERE lancamento >= {decada} and lancamento < {decada+10}
        """

        filmes = self._executar_query(query)

        return f'Nenhum filme da década de {decada} foi encontrado' if len(filmes) == 0 \
            else \
            f"Filmes lançados na decada de {decada}:"\
            f'\n{"\n".join([f"{x[0]} ({x[1]}) - {x[2]}" for x in filmes])}'

    def encerrar(self):
        self.cr.close()