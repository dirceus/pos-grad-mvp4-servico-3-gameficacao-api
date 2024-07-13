# pos-grad-mvp4-respondarapido-api
Esse componente faz parte do MVP da disciplina de Arquitetura de Software do cursos de Pós Graduação em Engenhiria de software.

## Objetivo
Objetivo desse componente é fornecer uma API registrar as pontuações de usuário do aplicativo Responda Rápido (API responsável pela gamificação do aplicativo)

## Tecnlogias

* Pyhon
* Flask
* SQLite

## Arquitetura

Esse componente faz ṕarte de uma arquitetura de microserviços

![image](https://github.com/user-attachments/assets/949e089f-151f-4ea7-a32e-412040b45a5b)

Para mais informações sobre arquitetura do MVP consultar: https://github.com/dirceus/pos-grad-mvp4-servico_principal-frontend

## Como executar localmente esse componente

    Baixe ou clone este repositório usando git clone

    Crie um ambiente virtual do tipo virtualenv.

    No ambiente virtual, instale as dependências através do comando:

```(env)$ pip install -r requirements.txt ```

    Execute a API através do comando

```(env)$ flask run --host 0.0.0.0 --port 5002 ```

    Com a aplicação rodando, abra no navegador a url: http://localhost:5002/#/
