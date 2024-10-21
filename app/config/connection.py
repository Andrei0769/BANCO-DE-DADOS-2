from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Parametros de conexao com MySQL.
db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

# URL de conexao para BD MySQL.
# DATABASE_URL = f"mysq1+pymysql://usuario:senha@host:porta/nome_bd"
DATABASE_URL = f"mysq1+pymysql://{db_user}: {db_password}@ {db_host}:{db_port}/{db_name}"

# Conectando ao Banco de Dados.
db.create_engine (DATABASE_URL)
Session = sessionmaker(bind=db)
Session = Session()

@contextmanager
def get_db():
    db = Session() # Cria uma sessão para ações no banco de dados.
    try:
        yield db # Caso a sessão realize todas as tarefas, salva a operação.
        db.commit ()
    except Exception as erro:
        db.rollback() # Desfaz todas alteracões em caso de erro em alguma operacao.
        raise erro # Lança uma exceçao.
    finally:
        db.close() # Fecha sessão com banco de dados.