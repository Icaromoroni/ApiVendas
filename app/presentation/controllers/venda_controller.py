from fastapi import APIRouter, Depends, HTTPException, status
from app.persistence.repository_venda_mongodb import RepositoryVendaMongoDB
from ..viewmodels import Venda

print('Venda controller ok!')
routes = APIRouter()
prefix = '/vendas'

repository_venda = RepositoryVendaMongoDB()

@routes.get('/')
def obter_vendas():
    pass

@routes.post('/', status_code=status.HTTP_201_CREATED)
def nova_venda(venda: Venda):
    return repository_venda.salvar(venda)
