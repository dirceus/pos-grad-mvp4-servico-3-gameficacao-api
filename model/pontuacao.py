from sqlalchemy import Column, String, Integer, DateTime, Float, Boolean
from datetime import datetime
from typing import Union

from model import Base


class Pontuacao(Base):
    __tablename__ = 'pontuacao'

    id = Column("pk_pontuacao", Integer, primary_key=True)
    id_usuario = Column(Integer)
    pontos = Column(Integer)
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, id_usuario:int, pontos:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Resgistra uma pontuacao

        Arguments:
            id_usuario: identificador da usuário que receberá a pontuacao.
            pontos: quantidade de pontos que será atribuída ao usuário
            data_insercao: data de quando os pontos foi concedido
        """
        self.id_usuario = id_usuario
        self.pontos = pontos

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao