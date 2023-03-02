from .crawler_extratoclube import get_auth_token
from .consts import URL_EXTRATO
from flask import Response
import requests, json

tokens_cache = {}

def consulta_matricula_cpf(consulta):
    global tokens_cache
    cpf = consulta['cpf']
    usuario = consulta['usuario']
    senha = consulta['senha']

    if tokens_cache.get(usuario) == None:
        tokens_cache[usuario] = get_auth_token(usuario, senha)
      
    endpoint = "{}{}{}{}".format("http://", URL_EXTRATO, "/offline/listagem/", cpf)
    headers = {"Authorization": tokens_cache[usuario]}

    resp = requests.get(endpoint, headers=headers)
    if resp.status_code == 200:
        try:
            resp_json = resp.json()
        except:
            resp_json = None

        if resp_json != None:
            if len(resp_json['beneficios']) > 1:
                nb = []
                for b in resp_json['beneficios']:
                    nb.append(b['nb'])
            else:
                nb = (resp.json()['beneficios'][0]['nb'])
            return Response(json.dumps({"result": nb}), status=200, mimetype='application/json')

    tokens_cache[usuario] = None
    return Response(json.dumps({"result": "Falha ao buscar informação"}), status=400, mimetype='application/json')