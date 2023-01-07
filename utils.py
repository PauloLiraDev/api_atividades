from models import Pessoas


# Insere dados na tabela <Pessoas>
def insere_pessoas():
    pessoa = Pessoas(nome='Paulo', idade=27)
    pessoa.save()
    pass

# Insere dados na tabela <Pessoas>
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoas = Pessoas.query.filter_by(nome='Paulo').first()
    print(pessoas.idade)
# Insere dados na tabela <Pessoas>
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Paulo').first()
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Paulo').first()
    pessoa.delete()

if __name__ == '__main__':
    altera_pessoa()
    consulta_pessoas()
