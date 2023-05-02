from pydantic import BaseModel, EmailStr, Field
from datetime import date

data = date.today()
data_texto = f'{data.day}/{data.month}/{data.year}'

class Venda(BaseModel):
    id: int | None | str
    item: str
    tipo: str
    tamanho: str
    valor: float
    quantidade: int
    forma_pagamento: str
    data_venda: str | None
    usuario_id: int | str | None

    @classmethod
    def fromDict(cls, venda_dict):
        venda = Venda(
            id=str(venda_dict['_id']),
            item=venda_dict['item'],
            tipo=venda_dict['tipo'],
            tamanho=['tamanho'],
            valor=venda_dict['valor'],
            quantidade=venda_dict['quantidade'],
            forma_pagamento=venda_dict['forma_pagamento'],
            data_venda=venda_dict['data_venda'],
            usuario_id=str(venda_dict['usuario_id'])
            )
        return venda
    
    def toDict(self):
        return{
            "item":self.item,
            "tamanho":self.tamanho,
            "valor":self.valor,
            "quantidade":self.quantidade,
            "forma_pagamento":self.forma_pagamento,
            "data_venda":self.data_venda,
            "usuario_id":self.usuario_id,
        }

class UsuarioSimples(BaseModel):
    id: int | None | str
    nome: str = Field(min_length=3)
    usuario: str = Field(min_length=5)
    email: EmailStr

    def toDict(self):
        return {
            "nome": self.nome,
            "usuario": self.usuario,
            "email": self.email,
            "senha": self.senha,
        }


class Usuario(UsuarioSimples):
    senha: str = Field(min_length=6)

    @classmethod
    def fromDict(cls, usuario_dict):
        return Usuario(**usuario_dict, id=str(usuario_dict['_id']))


class CriarUsuario(Usuario):
    confirmacao_senha: str


class LoginData(BaseModel):
    usuario: str = Field(min_length=5)
    senha: str = Field(min_length=6)