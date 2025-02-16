from dotenv import load_dotenv
from mysql.connector import connect
import os 

diretorio = os.path.join(os.path.dirname(__file__).replace("dados", ""), 'base_info.env')

load_dotenv(diretorio)

connection = connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),
  database=os.getenv("DB_NAME")
)

cursor = connection.cursor()

__all__ = ['cursor']
