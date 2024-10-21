from models.usuario import Usuario
from sqlalchemy.orm import Session


class UsuarioRepository:
    def __init__(self, session):
        self.session = session  # Atribui a sessão para ser usada nos métodos

    def criar_usuario(self, usuario):
        self.session.add(usuario)
        self.session.commit()

    def listar_todos(self):
        return self.session.query(Usuario).all()  # Certifique-se de que 'Usuario' é um modelo definido

    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh()

    def pesquisar_usuario(self, email: str):
        return self.session.query(Usuario).filter_by(email = email).first()

    def excluir_usuario(self, usuario: Usuario):
        self.session.delete(usuario)
        self.session.commit()
        self.session.refresh()

    def listar_todos_usuarios(self):
        return self.session.query(Usuario).all()