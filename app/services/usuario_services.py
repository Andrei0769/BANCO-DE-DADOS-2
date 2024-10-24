from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def init_(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)
            
            consulta_usuario = self.repository.pesquisar_usuario(usuario.email)

            if consulta_usuario:
                print("Usuario já existe no banco de dados.")
                return
            self.repository.salvar_usuario(usuario)
            print("Usuario salvo com sucesso!")
        except TypeError as error: 
            print(f"Error ao Salvar usuário: {error}")
        except Exception as error:
            print(f"Ocorreu um erro inespesrado")
    
    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuarios()
        