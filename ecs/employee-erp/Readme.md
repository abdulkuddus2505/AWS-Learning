# 🧾 Flask Employee ERP App

A simple Employee ERP system built using Flask and SQLAlchemy, with CRUD operations and Bootstrap UI.

---

## 🚀 Features

- Add,and View employees
- SQLite or PostgreSQL database support
- Bootstrap for styling
- Supports running via:
  - Local development server
  - Docker container

---

## 🛠️ Project Structure

```
employee-erp/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── config.py
│   └── templates/
│       ├── index.html
│       └── add_employee.html
├── run.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

## 🧩 Problems Faced & Solutions

### 1. ❌ `'erp' is undefined` in templates

**Issue:**
```
jinja2.exceptions.UndefinedError: 'erp' is undefined
```

**Cause:**  
Trying to access a blueprint in Jinja like this:
```html
{{ erp.add_employee }}
```

**Solution:**  
Use Flask's `url_for()` with blueprint prefix:
```html
{{ url_for('erp.add_employee') }}
```

---

### 2. ❌ Incorrect `url_for()` usage

**Incorrect:**
```html
url_for('add_employee')  # Without blueprint name
```

**Correct:**
```html
url_for('erp.add_employee')
```

---

### 3. ❌ App doesn't start or import errors

**Cause:**  
`create_app()` not called in the entry script (`run.py`), or misplacement of files.

**Solution:**  
Make sure you have a `run.py` at the root:
```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🧪 Running Locally (Without Docker)

### 🔧 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 🔧 2. Set Environment Variables (Optional)

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
```

### ▶️ 3. Run the App

```bash
python run.py
```

Access the app at: [http://localhost:5000](http://localhost:5000)

---

## 🐳 Running with Docker

### 📄 1. Create a `Dockerfile`

```Dockerfile
# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy code
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "run.py"]
```

### 📄 2. Create `.dockerignore`

```
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
*.sqlite3
.env
```

### 🐳 3. Build Docker Image

```bash
docker build -t employee-erp .
```

### 🐳 4. Run Docker Container (Basic)

```bash
docker run -p 5000:5000 employee-erp
```

### 🐳 5. Run Docker with PostgreSQL ENV (Advanced)

If you're connecting to a PostgreSQL database instead of SQLite, use the following command:

```bash
docker run --rm -p 5000:5000 \
  --network=host \
  --env DB_USER=postgres \
  --env DB_PASS=password \
  --env DB_HOST=localhost \
  --env DB_PORT=5432 \
  --env DB_NAME=erpdb \
  employee-erp
```

Make sure PostgreSQL is running and accessible at `localhost:5432`.

---

## 📥 Requirements

```
Flask
Flask-SQLAlchemy
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 📌 Notes

- By default, the app uses SQLite (`erp.db`) for simplicity.
- For PostgreSQL, ensure your config uses environment variables.

---

## ✅ TODOs (optional enhancements)

- Add unit tests
- Switch from SQLite to PostgreSQL in production
- Deploy to AWS/Heroku
- Add pagination, search, or filters

---

## 📧 Contact

For support or improvements, feel free to raise an issue or contribute!
