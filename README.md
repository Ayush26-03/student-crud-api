# Student Management API

A RESTful API built using FastAPI and SQLite to manage student records
through CRUD operations.

## Live Demo

- **API:** https://student-crud-api-nxrk.onrender.com
- **Swagger Documentation:** https://student-crud-api-nxrk.onrender.com/docs

## Features

- Create student records
- Retrieve all students
- Retrieve a student by ID
- Update student information
- Delete student records
- Email validation using Pydantic
- Duplicate email detection
- SQLite database integration
- RESTful API endpoints
- HTTP error handling

## Tech Stack

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Check API status |
| POST | `/students` | Create a student |
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |

## Installation

1. Clone the repository:

   `git clone https://github.com/Ayush26-03/student-crud-api.git`

2. Navigate to the project directory:

   `cd student-crud-api`

3. Create a virtual environment:

   `python -m venv venv`

4. Activate it on Windows:

   `venv\Scripts\activate`

5. Install dependencies:

   `pip install -r requirements.txt`

6. Start the server:

   `uvicorn main:app --reload`

7. Open Swagger UI:

   `http://127.0.0.1:8000/docs`

## Database

SQLite is used to store student records. The database table is
created automatically when the application starts.

## Deployment

Deployed on Render.

## Author

Ayush Pandey
