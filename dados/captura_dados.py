import requests
from bs4 import BeautifulSoup

def get_movie_request_data():
    """
    Obtendo os dados da pagina do IMDB
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get("https://www.imdb.com/chart/top", headers=headers, timeout=15)

    soup = BeautifulSoup(response.content, "html.parser")
    movies = soup.find_all(class_="ipc-metadata-list-summary-item")

    lista_filmes = []
    
    for movie in movies:
        try:
            metadata = movie.find_all("span", class_="cli-title-metadata-item")
            
            ano, duracao, classificacao = (meta.get_text(strip=True) 
                                            for meta in metadata[:3])
            
            classificacao = "L" if classificacao == "Livre" else classificacao

            nota = movie.find_all(class_="ipc-rating-star--rating")[0].text
            titulo = movie.find_all(class_="ipc-title__text")[0].text.split(". ")[1]
            
            lista_filmes.append({"Nome": titulo, "Nota": nota, "Lancamento": ano,
                                "Duracao": duracao, "Classificacao": classificacao})
            
        except (IndexError, AttributeError):
            continue
        
    return lista_filmes

__all__ = ['get_movie_request_data']