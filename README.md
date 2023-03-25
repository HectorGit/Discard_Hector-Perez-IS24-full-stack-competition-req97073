# Web application development tracker

# Start the backend 

`cd backend_in_django`
`python -m venv 39venv`
`pip install -r requirements.py`
`python manage.py runserver`

The server should run in port 8000 (http://localhost:8000)

Before starting, to populate the database, hit this endpoint once: 
`localhost:8000/insert_web_app_information/`

# Start the frontend

`cd frontend_in_react`
`npm start`

The server should run in port 3000 (http://localhost:3000)