# desafio-konsi

Projeto com solução para desafio proposto durante processo seletivo da Konsi.

<a href="https://gist.github.com/gustavoaraujofe/265c43b8b1df2dc4d6dd7e28959371d4">Link com instruções do desafio</a>

# Pré-requisitos

## Python 

### Ubuntu

    $ sudo apt update -y
    $ sudo apt install python3

### Windows e MacOS

Download do instalador: 

    https://www.python.org/downloads/release/python-31010/

## Pip 

### Ubuntu

    $ sudo apt update -y
    $ sudo apt python3-pip

### Windows e MacOS

Instruções em: 

    https://pip.pypa.io/en/stable/installation/

## Virtualenv 

### Ubuntu

    $ sudo apt install python3-virtualenv

### Windows e MacOS

    pip install virtualenv

## Chrome

Download do instalador: 

    https://www.google.com/chrome/

### Ubuntu

    $ sudo dpkg -i google-chrome-stable_current_amd64.deb


## Chrome Driver 

Verificar a versão do Crhome digitando na barra de navegação: 

    chrome://settings/help

Baixar o Driver correto da versão e SO em: 

    https://chromedriver.chromium.org/downloads

Descompactar e mover o executável 'chromedriver' para uma pasta onde o python possa encontrá-lo (ex.: pasta bin do virtualenv)

### Exemplo Ubuntu
    cd ~/Downloads
    unzip chromedriver_linux64.zip
    sudo mv chromedriver ~/desafio-konsi/env/bin

# Instruções para execução do projeto

### Clonar projeto a partir do Github

    $ git clone https://github.com/vitorbrando/desafio-konsi.git
    cd desafio-konsi

### Criar ambiente virtual dentro da pasta do projeto

    $ pip install virtualenv
    $ virtualenv env

### Ativar ambiente virtual

    $ source env/bin/activate (Linux ou MacOS)

    $ env/Scripts/Activate (Windows)

### Instalar bibliotecas

    $ pip install -r requirements.txt

### Executar projeto

    $ python main.py

### Acessar através do browser a interface do Swagger para testes

    $ http://localhost:8000/api/ui/

# API

<table>
<tr>
    <th>Método</th>
    <th>Endpoint</th>
    <th>Endpoint</th>
</tr>
<tr>
    <td>POST</td>
    <td>​/api/beneficio</td>
    <td>Retorna código de benefício a partir de um CPF</td>
</tr>
</table>

    JSON body:

    {
        "cpf": "810.693.915-49",
        "senha": "testekonsi",
        "usuario": "testekonsi"
    }

# Testes

Após ativar o ambiente virtal, navegar até a pasta do projeto e executar:

    py.test

# Projeto em execução disponível 

Disponibilizei uma versão do projeto já em execução.

    http://desafio-konsi.brando.dev.br/api/ui/


Projeto do Postman para testes:

    https://github.com/vitorbrando/desafio-konsi/blob/main/Konsi.postman_collection.json