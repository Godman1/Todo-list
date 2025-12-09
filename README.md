

Django Todo API

A simple and secure **Todo List REST API** built with **Django REST Framework (DRF)** and **JWT Authentication**.
Users can register, log in, and manage their personal todo items.



Features

✔ User Registration (returns JWT access token)
✔ User Login (returns JWT access token)
✔ Create, Read, Update & Delete Todo items
✔ Only authenticated users can access their todos
✔ Pagination for listing todos
✔ Error handling & validation
✔ Fully built using Class-Based Views (CBV) and DRF



Tech Stack

* **Python 3**
* **Django**
* **Django REST Framework**
* **SimpleJWT**
* **SQLite / MySQL**
* **Postman / DRF interface for testing**



Authentication

This API uses **JWT (JSON Web Token)** for authentication.

Include your token in the `Authorization` header:


Authorization: Bearer <your_token_here>




API Endpoints

**Auth**

| Method | Endpoint         | Description                          |
| ------ | ---------------- | ------------------------------------ |
| POST   | `/api/register/` | Register a new user + token returned |
| POST   | `/api/login/`    | Login user + token returned          |

---

 **Todos**

| Method | Endpoint          | Description                   |
| ------ | ----------------- | ----------------------------- |
| GET    | `/api/todo/`      | List user's todos (paginated) |
| POST   | `/api/todo/`      | Create a new todo             |
| GET    | `/api/todo/<id>/` | Retrieve a todo               |
| PUT    | `/api/todo/<id>/` | Update a todo                 |
| DELETE | `/api/todo/<id>/` | Delete a todo                 |


Example Todo JSON

POST /api/todo/**

json
{
  "title": "Buy groceries",
  "description": "2kg rice and beans"
}

 Project Structure


todo-api/
│── todo/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── users/
│── settings.py
│── README.md
│── manage.py

Author

Godman Ajadi
Backend Developer (Django & Spring Boot)



✅ Add badges (Python version, last update, license)
✅ Add screenshots
✅ Add setup instructions for deployment
✅ Improve styling (emoji version / professional version)

Just tell me!
