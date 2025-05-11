import sys 
import os 

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from dados.captura_dados import get_movie_request_data
from dados.conexao_mysql import cursor

def adicao_tabela():
    
    for x in get_movie_request_data():

        cursor.execute(
            """
            INSERT INTO imdb_table (nome, nota, lancamento, duracao, classificacao) 
            VALUES (%s, %s, %s, %s, %s) 
            ON DUPLICATE KEY UPDATE 
                nome = %s, nota = %s, 
                lancamento = %s, duracao = %s, 
                classificacao = %s
            """, 
            (x['Nome'], float(x['Nota']), x['Lancamento'], 
            x['Duracao'], x['Classificacao'], 
            x['Nome'], float(x['Nota']), x['Lancamento'], 
            x['Duracao'], x['Classificacao']
            )
        )

__all__ = ['adicao', 'cursor']
