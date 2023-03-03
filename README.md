# desafio-konsi

Projeto com solução para desafio proposto durante processo seletivo da Konsi.

<a href="https://gist.github.com/gustavoaraujofe/265c43b8b1df2dc4d6dd7e28959371d4">Link com instruções do desafio</a>

# Pré-requisitos

## Docker 

### Instalação

    https://docs.docker.com/engine/install/

# Instruções para execução do projeto (local)

### Clonar projeto a partir do Github

    docker run --name desafiokonsi -p 8000:8000 -d vitorbrando/dev:desafiokonsi

### Acessar através do browser a interface do Swagger para testes

    http://localhost:8000/api/ui/

# API

<table>
<tr>
    <th>Método</th>
    <th>Endpoint</th>
    <th>Endpoint</th>
</tr>
<tr>
    <td>POST</td>
    <td>​/api/matricula</td>
    <td>Retorna código de matrícula a partir de um CPF</td>
</tr>
</table>

    JSON body:

    {
        "cpf": "810.693.915-49",
        "usuario": "testekonsi"
        "senha": "testekonsi",  
    }

# Testes

Conectar ao container que está executando o projeto.

    docker exec -i -t desafiokonsi /bin/sh

Executar os testes.

    py.test

# Projeto em execução disponível 

Disponibilizei uma versão do projeto já em execução no endereço.

    http://desafio-konsi.brando.dev.br/api/ui/


Projeto do Postman para testes:

    https://github.com/vitorbrando/desafio-konsi/blob/main/Konsi.postman_collection.json
