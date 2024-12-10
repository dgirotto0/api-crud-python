# API CRUD de Animais de Estimação 🐾

Este é um exemplo de aplicação CRUD (Create, Read, Update, Delete) desenvolvido em Python utilizando o framework Flask. A API permite gerenciar informações de animais de estimação, como adicionar, listar, atualizar e excluir dados.

## Funcionalidades 🚀

- **Adicionar um animal de estimação:** Adicione novos pets ao sistema.
- **Listar todos os animais:** Obtenha uma lista completa dos pets cadastrados.
- **Atualizar informações de um animal:** Atualize dados de um pet específico pelo ID.
- **Excluir um animal:** Remova um pet do sistema utilizando seu ID.

## Tecnologias Utilizadas 🛠️

- **Python** - Linguagem de programação principal.
- **Flask** - Framework para construção da API.
- **JSON** - Para troca de dados entre cliente e servidor.

## Como Rodar o Projeto 🖥️

1. **Clone o repositório:**
  ```bash<br/>
  git clone https://github.com/dgirotto0/api-crud-python.git
  ```
2. Acesse o diretório do projeto:
  ```bash<br/>
  cd api-crud-python
  ```
3. Instale as dependências necessárias: Certifique-se de ter o Flask instalado. Caso contrário, instale com o comando:
  ```bash<br/>
  pip install flask
  ```
4. Inicie a aplicação:
  ```bash<br/>
  python pet.py
  ```
Acesse a API no navegador ou em ferramentas como Postman:
    
    http://127.0.0.1:5000

## Endpoints da API 🛣️

#### Adicionar um Pet

   - **Rota**: ```/adicionar_pet<br/>
   - **Método**: POST<br/>
   - **Descrição**: Adiciona um novo animal de estimação.<br/>
   - **Exemplo de JSON**:<br/>
  ```json
    {
      "nome": "Rex",
      "tipo": "Cachorro",
      "idade": 3
    }
  ```

#### Listar Pets

  - **Rota**: ```/listar_pets```<br/>
  - **Método**: GET<br/>
  - **Descrição**: Retorna todos os animais cadastrados.<br/>

#### Atualizar um Pet

  - **Rota**: ```/atualizar_pet/<id>```<br/>
  - **Método**: PUT<br/>
  - **Descrição**: Atualiza as informações de um pet específico.<br/>
  - **Exemplo de JSON**:<br/>
```json
    {
      "nome": "Rex",
      "tipo": "Cachorro",
      "idade": 4
    }
```
#### Excluir um Pet

  - **Rota**: ```/excluir_pet/<id>```<br/>
  - **Método**: DELETE<br/>
  - **Descrição**: Remove um animal de estimação pelo ID.

## Estrutura do Código 🗂️

O código é simples e organizado em uma única classe, contendo as rotas da API. Ele utiliza uma lista em memória para armazenar os dados, ideal para fins de demonstração.

## Licença 📜

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
