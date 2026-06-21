from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# ------------------------
# LOAD DATA FROM FILE
# ------------------------
def load_data():
    with open("students.json", "r") as file:
        return json.load(file)

# ------------------------
# SAVE DATA TO FILE
# ------------------------
def save_data(data):
    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

# ------------------------
# HOME ROUTE
# ------------------------
@app.get("/")
def greet():
    return "Welcome to Student Management System"

# ------------------------
# GET ALL STUDENTS
# ------------------------
@app.get("/student")
def all_students():
    return load_data()

# ------------------------
# GET STUDENT BY ID
# ------------------------
@app.get("/student/{id}")
def select_std(id: int):
    data = load_data()

    for student in data:
        if student["id"] == id:
            return student

    return {"error": "Student not found"}

# ------------------------
# ADD NEW STUDENT
# ------------------------
@app.post("/add")
def add_std(new_student: dict):
    data = load_data()

    data.append(new_student)

    save_data(data)

    return {
        "message": "Student added successfully",
        "student": new_student
    }

# ------------------------
# DEL ALL  STUDENTS
# ------------------------
@app.delete("/student/{id}")
def delete_student(id: int):
    data = load_data()

    for student in data:
        if student["id"] == id:
            data.remove(student)
            save_data(data)
            return {"message": "Student deleted successfully"}

    return {"error": "Student not found"}