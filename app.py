from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades
app = Flask(__name__)
api = Api(app)


class Pessoa(Resource):
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
            return response
        except AttributeError:
            response = {'status': 'error',
                        'mensagem': f"Pessoa de nome '{nome}' nao foi encontrada no banco de dados."
                        }
            return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {'id': pessoa.id,
                    'pessoa': pessoa.nome,
                    'idade': pessoa.idade}
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = f"O registro do ID {pessoa.id} e nome '{pessoa.nome}' foi deletado."
        pessoa.delete()
        return {'status': 'sucesso', 'mensagem': mensagem}


class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]  # dict comprehension
        return response

    def post(self):
        data = request.json
        pessoa = Pessoas(nome=data['nome'], idade=data['idade'])
        pessoa.save()
        print(pessoa.id)
        response = {'id': pessoa.id,
                    'nome': pessoa.nome,
                    'idade': pessoa.idade}
        return response


class Atividade(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        atividades = Atividades.query.filter_by(pessoa_id=pessoa.id)
        responsive = {pessoa.nome: [i.nome for i in atividades]}
        return responsive
    def put(self, id):
        pass


class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        try:
            pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
            atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
            atividade.save()
            response = {
                'pessoa': atividade.pessoa.nome,
                'idade': atividade.pessoa.idade,
                'atividade': atividade.nome,
                'id': atividade.id}
            return response
        except AttributeError:
            response = {'status': 'falha',
                        'mensagem': f"a pessoa {dados['pessoa']} não está cadastrada."}


api.add_resource(Pessoa, '/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')
api.add_resource(Atividade, '/atividades/<string:nome>')
if __name__ == '__main__':
    app.run(debug=True)
