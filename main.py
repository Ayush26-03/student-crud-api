import sqlite3
from datetime import date

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field, field_validator

from database import get_connection, create_table


app = FastAPI(
    title="Student Management API",
    description="A Student Database CRUD Application using FastAPI and SQLite",
    version="1.0.0"
)


# Create the database table when the application starts
@app.on_event("startup")
def startup():
    create_table()


# Student input model with validation
class Student(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    date_of_birth: date
    email: EmailStr
    phone: str | None = Field(default=None, max_length=20)
    course: str | None = Field(default=None, max_length=100)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Name cannot be empty")

        return value

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, value):
        if value > date.today():
            raise ValueError("Date of birth cannot be in the future")

        return value


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Student Management API is running!"
    }


# Create a student
@app.post("/students", status_code=201)
def create_student(student: Student):
    conn = get_connection()

    try:
        cursor = conn.execute(
            """
            INSERT INTO students
            (name, date_of_birth, email, phone, course)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                student.name,
                student.date_of_birth.isoformat(),
                str(student.email),
                student.phone,
                student.course
            )
        )

        conn.commit()

        return {
            "message": "Student created successfully",
            "student_id": cursor.lastrowid
        }

    except sqlite3.IntegrityError as e:
        conn.rollback()

        if "UNIQUE constraint failed" in str(e):
            raise HTTPException(
                status_code=409,
                detail="A student with this email already exists"
            )

        raise HTTPException(
            status_code=400,
            detail="Database constraint violation"
        )

    except sqlite3.Error:
        conn.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database operation failed"
        )

    finally:
        conn.close()


# Get all students
@app.get("/students")
def get_students():
    conn = get_connection()

    try:
        cursor = conn.execute(
            "SELECT * FROM students ORDER BY id"
        )

        students = cursor.fetchall()

        return {
            "total_students": len(students),
            "students": [dict(student) for student in students]
        }

    except sqlite3.Error:
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve students"
        )

    finally:
        conn.close()


# Get a student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn = get_connection()

    try:
        cursor = conn.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return dict(student)

    except sqlite3.Error:
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve student"
        )

    finally:
        conn.close()


# Update a student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    conn = get_connection()

    try:
        cursor = conn.execute(
            "SELECT id FROM students WHERE id = ?",
            (student_id,)
        )

        existing_student = cursor.fetchone()

        if existing_student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        conn.execute(
            """
            UPDATE students
            SET name = ?,
                date_of_birth = ?,
                email = ?,
                phone = ?,
                course = ?
            WHERE id = ?
            """,
            (
                student.name,
                student.date_of_birth.isoformat(),
                str(student.email),
                student.phone,
                student.course,
                student_id
            )
        )

        conn.commit()

        return {
            "message": "Student updated successfully",
            "student_id": student_id
        }

    except HTTPException:
        raise

    except sqlite3.IntegrityError as e:
        conn.rollback()

        if "UNIQUE constraint failed" in str(e):
            raise HTTPException(
                status_code=409,
                detail="A student with this email already exists"
            )

        raise HTTPException(
            status_code=400,
            detail="Database constraint violation"
        )

    except sqlite3.Error:
        conn.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database operation failed"
        )

    finally:
        conn.close()


# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = get_connection()

    try:
        cursor = conn.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        conn.commit()

        return {
            "message": "Student deleted successfully",
            "student_id": student_id
        }

    except HTTPException:
        raise

    except sqlite3.Error:
        conn.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database operation failed"
        )

    finally:
        conn.close()