from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.presentation.controllers import venda_controller

app = FastAPI()

origins = ['http://127.0.0.1:5500/']

app.add_middleware(CORSMiddleware,
               allow_origins=origins,
               allow_credentials=True,
               allow_methods=['*'],
               allow_headers=['*']
               )
#pode adicionar uma captura de log(logmiddleware) para capturar informações importantes


# adicionar rotas controllers
app.include_router(venda_controller.routes, prefix=venda_controller.prefix)
