# student-management-api
FastAPI based Student Management REST API with HTML/CSS/JS frontend
# 🎓 Student Management System

A FastAPI-based Student Management REST API with HTML/CSS/JS frontend.

## 🌐 Live Demo
👉 [Click here to view the project](https://student-management-api-production-41d3.up.railway.app/app)

## 🚀 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /student | Get all students |
| GET | /student/{id} | Get student by ID |
| POST | /add | Add new student |
| DELETE | /student/{id} | Delete student |

## 🛠️ Tech Stack
- Python
- FastAPI
- HTML / CSS / JavaScript

## 💻 Run Locally
1. Clone the repo
   git clone https://github.com/hadiaazhar35-jpg/student-management-api.git

2. Install dependencies
   pip install -r requirements.txt

3. Run the server
   uvicorn main:app --reload

4. Open browser
   http://localhost:8000/app
