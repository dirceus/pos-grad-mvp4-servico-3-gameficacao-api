from pydantic import BaseModel
from typing import Optional, List


class PontuarRequestSchema(BaseModel):
    """ Define como deve ser a requisição de pontuação
    """
    id_usuario: int = 1


class PontuarResponseSchema(BaseModel):
    """ Define como deve reser a representação da pontuação
    """
    resultado: bool = True


class RankingResponseSchema(BaseModel):
    """ Define como deve ser representado um ranking
        """
    id_usuario: int = 1
    pontos: int = 100


def apresenta_ranking(itens: List):
    """ Retorna uma representação de lista de usuários
        RankingResponseSchema.
    """
    result = []
    for usuario in itens:
        result.append({
            "id_usuario": usuario[0],
            "pontos": usuario[1],
        })

    return result

