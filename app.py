from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from sqlalchemy import text

from model import Session
from logger import logger
from model.pontuacao import Pontuacao
from schemas import *
from flask_cors import CORS

from schemas.pontuacao import PontuarRequestSchema, PontuarResponseSchema, RankingResponseSchema, apresenta_ranking

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
gamificacao_tag = Tag(name="Pontuação", description="Microserviço de Pontuação")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/api/pontuar_acerto', tags=[gamificacao_tag],
          responses={"200": PontuarResponseSchema, "409": ErrorSchema, "400": ErrorSchema})
def pontuar_acerto(body: PontuarRequestSchema):
    """Registra um acerto para o usuario informado
    """
    logger.debug(f"Pontuando acerto de questão para o usuário: '{body.id_usuario}'")

    pontos = Pontuacao(
        id_usuario=body.id_usuario,
        pontos=100)
    try:
        # criando conexão com a base
        session = Session()
        # adicionando pontuos
        session.add(pontos)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(
            f"Registrado os pontos para o usuário '{pontos.id_usuario}'")
        return "Sucesso", 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Erro ao registrar os pontos do usuário"
        return {"mesage": error_msg}, 400


@app.post('/api/pontuar_error', tags=[gamificacao_tag],
          responses={"200": PontuarResponseSchema, "409": ErrorSchema, "400": ErrorSchema})
def pontuar_error(body: PontuarRequestSchema):
    """Registra um acerto para o usuario informado
    """
    logger.debug(f"Pontuando acerto de questão para o usuário: '{body.id_usuario}'")

    pontos = Pontuacao(
        id_usuario=body.id_usuario,
        pontos=10)
    try:
        # criando conexão com a base
        session = Session()
        # adicionando pontuos
        session.add(pontos)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(
            f"Registrado os pontos para o usuário '{pontos.id_usuario}'")
        return "Sucesso", 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Erro ao registrar os pontos do usuário"
        return {"mesage": error_msg}, 400

@app.get('/api/ranking', tags=[gamificacao_tag],
         responses={"200": RankingResponseSchema, "400": ErrorSchema, "500": ErrorSchema})
def obter_ranking():

    """Obtem o ranking dos usuário que possuem pontuação
    """
    try:
        # criando conexão com a base
        session = Session()
        sql = text('SELECT id_usuario, sum(pontos) as pontos FROM pontuacao GROUP BY id_usuario ORDER BY pontos DESC')
        result = session.execute(sql)
        lista = list(result.fetchall())
        return apresenta_ranking(lista)
    except Exception as ex:
        print(ex)
        error_msg = "Erro ao consultar ranking"
        return {"mesage": error_msg}, 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)