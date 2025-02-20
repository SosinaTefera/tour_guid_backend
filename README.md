# Tour Guide Backend

## Overview
This is the backend API for the **Tour Guide** web application. It provides authentication, user management, tour listings, and review functionality.

## Features
- **User Authentication** (Admin & Tourist roles)
- **Tour Management** (CRUD operations)
- **Review System** for Tours
- **Secure Password Hashing** with Bcrypt
- **SQLAlchemy ORM** with Google BigQuery as the database

## Technologies Used
- **Python** (FastAPI/Flask)
- **SQLAlchemy** (ORM for database operations)
- **Google BigQuery** (Database)
- **JWT Authentication**

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Virtualenv

### Setup Steps
1. **Clone the Repository**
   ```sh
   git clone https://github.com/SosinaTefera/tour_guid_backend.git # Or SSH URL
   cd tour_guide_backend
   ```
2. **Create Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables** (Create `.env` file)
   ```env
   DATABASE_URL=bigquery://your-project-id/your-dataset
   SECRET_KEY=your_secret_key
   ```
6. **Start the Server**
   ```sh
   uvicorn app.main:app --reload
   ```

