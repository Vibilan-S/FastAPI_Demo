# 📦 FastAPI Product Management System (Rest API using Python)

A professional RESTful API built with **FastAPI** and **PostgreSQL**. This project manages a product inventory using **SQLAlchemy ORM** for database interaction and **Pydantic** for strict data validation.

---

## 🛠️ Tech Stack
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Database:** [PostgreSQL](https://www.postgresql.org/)
* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Validation:** [Pydantic](https://docs.pydantic.dev/)

---

## 📁 Project Structure
* `model.py` - The main application entry point with API routes and logic.
* `database_models.py` - SQLAlchemy models defining the PostgreSQL table structure.
* `models.py` - Pydantic schemas for request/response data validation.
* `database.py` - Database engine configuration and session management.

---

## 🚀 Key Features
- **Automatic DB Seeding:** On startup, the system checks if the database is empty and populates it with initial products (Phone, Laptop, Pen, Table).
- **CRUD Operations:**
    - **Create:** Add new products via POST requests.
    - **Read:** Fetch all products or a specific product by ID.
    - **Update:** Modify existing product details using PUT.
    - **Delete:** Remove products from the inventory.
- **Auto-Generated Docs:** Full Swagger UI documentation available out of the box.

---

## ⚙️ Setup and Installation

### 1. Clone the repository
    git clone https://github.com/Vibilan-S/FastAPI_Demo.git
    cd FastAPI_Demo

### 2. Install Dependencies
    pip install fastapi uvicorn sqlalchemy psycopg2 pydantic

### 3. Configure Database
Ensure your PostgreSQL server is running. Update the db_url in database.py:
    db_url = "postgresql://vibilan:Vibilan%40123@127.0.0.1:5432/my_project"

### 4. Run the Server
    uvicorn model:app --reload

---

## 🚦 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/` | Welcome Greeting |
| **GET** | `/products` | Get list of all products |
| **GET** | `/product/{id}` | Get a single product by ID |
| **POST** | `/product` | Add a new product |
| **PUT** | `/product` | Update product details |
| **DELETE** | `/product` | Delete a product |

---

## 📖 API Documentation
Once the server is running, view the interactive API docs at:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---
*Developed by Vibilan*
