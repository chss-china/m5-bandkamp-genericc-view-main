# M5 - BandKamp Generic View
#deploy https://django-bandkamp.onrender.com/api/users/
## Instalação dos pacotes de teste
##Decrição
Nessa entrega, tive que fazer alguns debugs em um projeto que já veio pronto para nós, mas não estava funcionando corretamente. Também realizamos uma modelagem do nosso banco de dados. O projeto permite que os usuários se cadastrem, criem álbuns e associem músicas e álbuns ao usuário.
O projeto foi feito com Django, utilizando APIView, Serializer e SQLite3. Tive que fazer uma refatoração, aplicando os conceitos de Generic View, Model Serializer e alterando o banco de dados para o PostgreSQL. Tivemos um total de 22 testes e conseguimos passar em todos eles.

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:
```shell
pip list
```
- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:
```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```


```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```


4. Agora é só rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```

5. Caso queira um log mais resumido, basta executar com os testes sem as flags **verbose**:
```shell
pytest --testdox
```

## Rodando os testes por partes

Caso você tenha interesse em rodar apenas um diretório de testes específico, pode utilizar o comando:

- Rodando testes de users:
```python
pytest --testdox -vvs tests/users/
```

- Rodando testes de albums:
```python
pytest --testdox -vvs tests/albums/
```

- Rodando testes de songs:
```python
pytest --testdox -vvs tests/songs/
```
