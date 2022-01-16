
# Frexco - Desafio Automação e Desenvolvimento de Software

Desafio Tech (Python)

- Criar uma API usando a linguagem Python, frameworks: Django e Django Rest Framework.
- A API deverá realizar a comunicação com um banco de dados SQL qualquer (pode ser SQLite)
- O banco deverá ter pelo menos duas tabelas: 
         - Uma tabela chamada “Region” que conterá apenas uma coluna “name” com informação dos nomes das regiões do Brasil ( Norte, Nordeste, etc.)
         - Uma tabela chamada “Fruit” que conterá colunas “name” (o nome da fruta) e uma coluna de associação por chave estrangeira (foreign key) com a tabela “Region” associando cada fruta a uma região existente na primeira tabela.
- Para cada tabela, a API deve conter os quatro métodos GET, POST, PUT e DELETE.





## Running the Application


```bash
  cd desafiofrexco/
  source venv/bin/activate
  python3 manage.py runserver
```
## Endpoints

| Endpoint  |  HTTP Method  | CRUD Method  |  Result  |
| ------------------- | ------------------- | ------------------- | ------------------- |
|  api/region |  GET |  READ |  Get all regions |
|  api/region/:id |  GET |  READ |  Get a single region |
|  api/region |  POST |  CREATE |  Create a new region |
|  api/region/:id |  PUT |  UPDATE |  Update a region |
|  api/region/:id |  DELETE |  DELETE |  Delete a region |
|  api/fruit |  GET |  READ |  Get all fruits |
|  api/fruit/:id |  GET |  READ |  Get a single fruit |
|  api/fruit |  POST |  CREATE |  Create a new fruit |
|  api/fruit/:id |  PUT |  UPDATE |  Update a fruit |
|  api/fruit/:id |  DELETE |  DELETE |  Delete a fruit |
