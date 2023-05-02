from fastapi import APIRouter, Depends, HTTPException, status
from app.persistence.repository_venda_mongodb import VendaRepositoryMongoDB
from ..viewmodels import Venda

print('Venda controller ok!')
routes = APIRouter()
prefix = '/vendas'

venda_repository = VendaRepositoryMongoDB()

@routes.get('/')
def obter_vendas(skip: int | None = 0, take: int | None = 0):
    vendas = venda_repository.todas(skip,take)
    return vendas

@routes.post('/', status_code=status.HTTP_201_CREATED)
def nova_venda(venda: Venda):
    return venda_repository.salvar(venda)
