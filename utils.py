from models import Pessoas


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


if __name__ == '__main__':
    insere_pessoas()
