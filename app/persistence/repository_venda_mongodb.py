from bson.objectid import ObjectId
from decouple import config
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from ..presentation.viewmodels import Venda, data_texto

class RepositoryVendaMongoDB():

    def __init__(self) -> None:

        try:
            uri = config('MONGODB_URL')
            client = MongoClient(uri)
            db = client['vendasapp']
            self.vendas = db['vendas']
            print('MongoDB vendas Conectado!')
        except ConnectionFailure as e:
            print(f'Não foi possível conectar ao MongoDB: {e}')
        
    def obter_todas(self):
        pass

    def salvar(self, venda:Venda):
        venda.data_venda = data_texto
        _id = self.vendas.insert_one(venda.toDict()).inserted_id
        venda.id = str(_id)
        return venda
    def remover(self, venda_id):
        pass

    def atualizar(self, venda_id, venda):
        pass
