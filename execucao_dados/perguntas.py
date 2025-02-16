from inclusao import adicao_tabela, cursor

class Funcoes:
    
    def __init__(self):
        adicao_tabela()
        self.cr = cursor

    def lista_completa(self):
        self.cr.execute("SELECT * FROM imdb_table")
        resp = self.cr.fetchall()
        lt = [f'Nome: {x[0]}, Nota: {x[1]}, Lancamento: {x[2]}, Duracao: {x[3]}, Classificacao: {x[4]}' for x in resp]

        return lt
    
    def melhor_mais_recente(self):
        self.cr.execute("SELECT * FROM imdb_table ORDER BY lancamento DESC LIMIT 1")
        resp = self.cr.fetchall()
        return f'O filme mais recente é {resp[0][0]}, lancado em {resp[0][2]} com {resp[0][1]} de nota'

    def melhor_mais_antigo(self):
        self.cr.execute("SELECT * FROM imdb_table ORDER BY lancamento LIMIT 1")
        resp = self.cr.fetchall()

        return f'O filme mais antigo é {resp[0][0]}, lancado em {resp[0][2]} com {resp[0][1]} de nota'

    def media_notas(self):
        self.cr.execute("SELECT AVG(nota) FROM imdb_table")
        resp = self.cr.fetchall()[0][0]
        return f'A média das notas é {round(resp,2)}'
    
    def mais_longo(self):
        self.cr.execute("SELECT nome, duracao FROM imdb_table order by duracao desc" )
        dur = self.cr.fetchall()[0]
        return f'O filme mais longo é {dur[0]}, com {dur[1]}'
    
    def mais_curto(self):
        self.cr.execute("SELECT nome, duracao FROM imdb_table order by duracao asc")
        dur = self.cr.fetchall()[0]
        return f'O filme mais curto é {dur[0]}, com {dur[1]}'
    

    def buscar_nome(self, filme):
        self.cr.execute(f'SELECT * FROM imdb_table WHERE lower(nome) LIKE "%{filme.lower()}%"')
        resp = self.cr.fetchall() 
        return f'Lamento, mas o filme {filme} não foi encontrado' \
            if len(resp) == 0 else f'Os filmes que possuem o nome {filme} são:\n {resp}'
    

    def buscar_classificacao(self, classf):
        self.cr.execute(f'SELECT * FROM imdb_table WHERE lower(classificacao) LIKE "%{classf.lower()}%"')
        resp = self.cr.fetchall() 
        return f'Lamento, mas os filmes de classificação {classf} nao foram encontrados' \
                if len(resp) == 0 else f'Os filmes de classificação {classf} são:\n {resp}'


    def encerrar(self):
        self.cr.close()
