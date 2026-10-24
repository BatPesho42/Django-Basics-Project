# HomeBrew 

HomeBrew is a Django web application for managing and exploring homemade brewing recipes. It allows users to create recipes, track ingredients, and share feedback through comments and ratings.


## Features

- Create, view, edit, and delete recipes
- Organize recipes by category and style
- Manage ingredients through a catalogue
- Track recipe ingredients and quantities
- Search recipes
- Comment and rate recipes


## Technologies

- Python
- Django
- SQLite
- HTML, CSS, Bootstrap

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/BatPesho42/Django-Basics-Project.git
cd Django-Basics-Project
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.


## About

Developed as a submission for the SoftUni Django Basics course exam.