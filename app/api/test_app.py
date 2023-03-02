import json
from .crawler_extratoclube import get_auth_token
from .matricula import consulta_matricula_cpf

def teste_login_invalido_extratoclube():
	token = get_auth_token('testekonsi_', 'testekonsi_')
	assert token == None, "teste falhou"

def teste_login_valido_extratoclube():
	token = get_auth_token('testekonsi', 'testekonsi')
	assert token != None, "teste falhou"
	assert 'Bearer' in token, "teste falhou"

def teste_consulta_matricula_cpf_invalido():
	consulta = {"cpf": "111.111.111-11", "usuario": "testekonsi", "senha": "testekonsi"}
	response = consulta_matricula_cpf(consulta)
	result = json.loads(response.get_data(True))["result"]
	assert result == "Matrícula não encontrada!", "teste falhou"

def teste_consulta_unica_matricula_cpf_valido():
	consulta = {"cpf": "810.693.915-49", "usuario": "testekonsi", "senha": "testekonsi"}
	response = consulta_matricula_cpf(consulta)
	result = json.loads(response.get_data(True))["result"]
	is_integer = True
	try:
		int(result)
	except:
		is_integer = False
	assert is_integer, "teste falhou"

def teste_consulta_matriculas_cpf_valido():
	consulta = {"cpf": "927.100.938-04", "usuario": "testekonsi", "senha": "testekonsi"}
	response = consulta_matricula_cpf(consulta)
	result = json.loads(response.get_data(True))["result"]
	assert isinstance(result, list), "teste falhou"