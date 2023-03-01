import pytest
from .crawler_extratoclube import get_auth_token
from .beneficio import consulta_cpf

def teste_login_invalido_extratoclube():
	token = get_auth_token('testekonsi_', 'testekonsi_')
	assert token == None, "teste falhou"

def teste_login_valido_extratoclube():
	token = get_auth_token('testekonsi', 'testekonsi')
	assert token != None, "teste falhou"
	assert 'Bearer' in token, "teste falhou"

def teste_consulta_cpf_invalido():
	consulta = {"cpf": "111.111.111-11", "usuario": "testekonsi", "senha": "testekonsi"}
	response = consulta_cpf(consulta)
	status_code = response.status_code
	assert status_code == 400, "teste falhou"

def teste_consulta_cpf_valido():
	consulta = {"cpf": "810.693.915-49", "usuario": "testekonsi", "senha": "testekonsi"}
	response = consulta_cpf(consulta)
	status_code = response.status_code
	assert status_code == 200, "teste falhou"
