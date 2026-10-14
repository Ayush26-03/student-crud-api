# Student Management API

A RESTful Student Management API built using FastAPI and SQLite.
This project demonstrates CRUD operations, data validation, and database integration.

## Features

- Create a new student
- Retrieve all students
- Retrieve a student by ID
- Update student details
- Delete a student
- Email validation
- Date of birth validation
- Duplicate email prevention
- SQLite database integration
- Interactive API documentation using Swagger UI

## Technologies Used

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

## Project Structure

```text
student-crud-api/
├── main.py
├── database.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.10 or later
- pip

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd student-crud-api
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Run the Application

Start the development server:

```bash
python -m uvicorn main:app --reload
```

The API will run at:

http://127.0.0.1:8000

## API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

Alternative documentation:

http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Check API status |
| POST | `/students` | Create a student |
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PUT | `/students/{student_id}` | Update student details |
| DELETE | `/students/{student_id}` | Delete a student |

## Example Request

Create a student using `POST /students`:

```json
{
  "name": "Rahul Sharma",
  "date_of_birth": "2004-05-15",
  "email": "rahul@example.com",
  "phone": "9876543210",
  "course": "B.Tech CSE"
}
```

## Database

The application uses SQLite to store student records.

The database table is created automatically when the application starts.
The database file is generated locally and is not required in the Git repository.

## Error Handling

- `404 Not Found` — Student does not exist.
- `409 Conflict` — Email address already exists.
- `422 Unprocessable Entity` — Request validation failed.
- `500 Internal Server Error` — Database operation failed.

## License

This project is intended for educational purposes.