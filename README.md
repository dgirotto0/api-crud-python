# Pet CRUD API 🐾

This is a sample CRUD (Create, Read, Update, Delete) application developed in Python using the Flask framework. The API allows managing pet information, such as adding, listing, updating, and deleting data.

## Features 🚀

- **Add a Pet:** Add new pets to the system.  
- **List All Pets:** Get a complete list of registered pets.  
- **Update Pet Information:** Update data for a specific pet by ID.  
- **Delete a Pet:** Remove a pet from the system using its ID.  

## Technologies Used 🛠️

- **Python** - Main programming language.  
- **Flask** - Framework for building the API.  
- **JSON** - For data exchange between client and server.  

## How to Run the Project 🖥️

1. **Clone the repository:**  
  ```bash
  git clone https://github.com/dgirotto0/api-crud-python.git
  ```
2. Access the project directory:
  ```bash<br/>
  cd api-crud-python
  ```
3. Install the required dependencies: Make sure Flask is installed. If not, install it with:
  ```bash<br/>
  pip install flask
  ```
4. Start the application:
  ```bash<br/>
  python pet.py
  ```
Access the API via browser or tools like Postman:
    
    http://127.0.0.1:5000

## API Endpoints 🛣️

### Add a Pet

  - Route: `/adicionar_pet`
  - Method: POST
  - Description: Adds a new pet.
  - JSON Example:
  ```json
    {
      "nome": "Rex",
      "tipo": "Cachorro",
      "idade": 3
    }
  ```

### List Pets

  - **Route**: `/listar_pets`<br/>
  - **Method**: GET<br/>
  - **Description**: Returns all registered pets.

### Uptade a Pet

  - **Route**: `/atualizar_pet/<id>`<br/>
  - **Method**: PUT<br/>
  - **Description**: Updates information for a specific pet.
  - **JSON Example**:<br/>
```json
    {
      "nome": "Rex",
      "tipo": "Cachorro",
      "idade": 4
    }
```
### Delete a Pet

  - **Route**: `/excluir_pet/<id>`<br/>
  - **Method**: DELETE<br/>
  - **Description**: Removes a pet by ID.

## Code Structure 🗂️

The code is simple and organized in a single class containing the API routes. It uses an in-memory list to store data, ideal for demonstration purposes.

## Lisense 📜

This project is licensed under the MIT License. See the LICENSE file for more details.
