# MVP Chat Web App

This project contains a minimal scaffold for a chat-based web application using a FastAPI backend and a React frontend.

## Backend

The backend is located in the `backend/` directory and uses FastAPI with SQLite via SQLAlchemy.

Create a virtual environment, install dependencies, and run the server:

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Frontend

The frontend is located in the `frontend/` directory and was bootstrapped manually. To start the development server:

```bash
cd frontend
npm install
npm start
```

This will launch the React app which can interact with the FastAPI backend.
