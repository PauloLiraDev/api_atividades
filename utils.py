from models import Pessoas, Usuarios


# Insere dados na tabela <Pessoas>
def insere_pessoas():
    pessoa = Pessoas(nome='Miguel', idade=34)
    pessoa.save()
    pass


# Consulta dados na tabela <Pessoas>
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoas = Pessoas.query.filter_by(nome='Paulo').first()
    print(pessoas.idade)


# Altera dados na tabela <Pessoas>
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Paulo').first()
    pessoa.idade = 21
    pessoa.save()

# Altera dados na tabela <Pessoas>
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Paulo').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


if __name__ == '__main__':
    #insere_usuario('paulo', 123)
    #insere_usuario('lira', 321)
    insere_usuario('pedro', 123)