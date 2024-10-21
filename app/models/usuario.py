from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from config.connection import db

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(String(150), primary_key=True)  # Defina id como chave primária
    email = Column(String(150), unique=True)
    senha = Column(String(150))

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)  # Use engine aqui
