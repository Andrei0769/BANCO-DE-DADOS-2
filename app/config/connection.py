from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# URl de Conexão para BD MySQL
DATABASE_URL = f"mysql+pymsql://usuario:senha@host:porta/nome_bd"  ## PRECISO DE TUDO ISSO PARA DEFINIR O BANCO DE DADOS