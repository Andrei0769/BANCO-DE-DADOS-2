import os 
from services.usuario_services import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session

os.system("cls || clear")
def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Criando um Usuário.
    service.criar_usuario("Ana Vitoria", "Vitoria@gmail.com", "123")

    #Lisitano todos os Usuarios.
    print("/nListando todos os Usuários.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

if __name__ == "__main__":
    main() #CHAMANDO A FUNÇÃO