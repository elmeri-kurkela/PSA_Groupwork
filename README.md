# PSA_Groupwork
# Second-Hand Comic Bookstore Management Backend

A RESTful backend application for managing a second-hand comic bookstore.

The project is developed using **Python, FastAPI and PostgreSQL**, following **Clean Architecture** and **SOLID principles**.

## 1. Project Overview

ComicVault is an internal bookstore management system designed for bookstore employees and administrators.

The backend provides RESTful APIs for managing:

- Comic book catalog
- Customers
- Inventory
- Orders
- Authentication and authorization

The system focuses on maintainability, separation of concerns, data integrity, testability and clear API design.

## 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.13+ | Programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM and database access |
| Alembic | Database migrations |
| Pydantic | Data validation and settings |
| PyJWT | JWT authentication |
| pwdlib | Password hashing |
| Pytest | Automated testing |
| HTTPX | API testing |

## 3. Prerequisites

Before starting, install the following tools:

- Python 3.13 or later
- Git
- Docker Desktop (required for the planned PostgreSQL setup)
- Visual Studio Code (recommended)

Check your installations:

```bash
python --version
git --version
docker --version
docker compose version
```

**Note:** This is a Python backend project. Node.js and npm are not required.

## 4. Getting Started

Follow these steps to set up the project on your computer.

### Step 1: Clone the repository

```bash
git clone https://github.com/elmeri-kurkela/PSA_Groupwork.git
```

Navigate into the project directory:

```bash
cd PSA_Groupwork
```

### Step 2: Create a Python virtual environment

```bash
py -3.13 -m venv .venv
```

The virtual environment keeps this project's Python dependencies separate from other Python projects on your computer.

### Step 3: Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt (CMD):**

```cmd
.venv\Scripts\activate
```

After activation, you should see `(.venv)` at the beginning of your terminal prompt.

### Step 4: Upgrade pip

```bash
python -m pip install --upgrade pip
```

### Step 5: Install project dependencies

```bash
python -m pip install -r requirements.txt
```

All team members should install dependencies using the shared `requirements.txt` file.

### Step 6: Verify the installation

```bash
python -m pip check
```

Expected output:

```text
No broken requirements found.
```

You can also check the installed packages:

```bash
python -m pip list
```

## 5. Git Workflow

The team uses a shared GitHub repository.

The `main` branch is used for the integrated project. For individual development tasks, create a separate branch.

First, make sure your local main branch is up to date:

```bash
git switch main
git pull origin main
```

Create a branch for your task:

```bash
git switch -c feature/your-feature-name
```

Examples:

```bash
git switch -c feature/customer-management
git switch -c feature/inventory-management
git switch -c feature/order-management
```

After completing and testing a small piece of work:

```bash
git add .
git commit -m "feat: describe your change"
git push -u origin feature/your-feature-name
```

Then create a Pull Request on GitHub to merge your changes into `main`.

**Important Git rules:**

- Do not commit your `.venv` directory.
- Do not commit your `.env` file or passwords.
- Do not work directly on `main` for individual features.
- Commit small, completed changes regularly.
- Pull the latest changes before starting new work.

## 6. Project Configuration Files

| File | Purpose |
|---|---|
| `.gitignore` | Excludes virtual environments, caches and local secrets |
| `requirements.txt` | Shared Python dependencies |
| `README.md` | Project overview and setup instructions |
| `.env.example` | Template for environment variables (to be added) |
| `docker-compose.yml` | PostgreSQL container configuration (to be added) |
| `pyproject.toml` | Project and development-tool configuration (to be added) |

## 7. Architecture

The backend will follow Clean Architecture.

The planned main layers are:

- **Domain:** Core business entities, value objects and business rules.
- **Application:** Use cases, application services and repository interfaces.
- **Infrastructure:** Database access, repository implementations and external integrations.
- **API / Presentation:** REST endpoints, request/response schemas and dependency configuration.

The architecture aims to keep business logic independent of frameworks and database implementation details.

## 8. Current Development Status

The project is currently in its initial setup stage.

Completed:

- GitHub repository initialized
- Python virtual environment created
- Initial `.gitignore` configuration
- Initial `requirements.txt` configuration
- Python dependencies installed and checked

Planned next steps:

- PostgreSQL setup using Docker Compose
- Environment variable configuration
- FastAPI application entry point
- Clean Architecture project structure
- Database models and migrations
- REST API implementation
- Authentication and authorization
- Unit and integration tests
- Swagger/OpenAPI documentation

Setup instructions will be updated as the project develops.

## 9. Team Development

All team members should use the same repository and shared dependency configuration.

Before starting development, make sure you have:

1. Cloned the latest repository.
2. Created and activated your own `.venv`.
3. Installed dependencies from `requirements.txt`.
4. Created your own feature branch.

For questions or issues, contact the team and describe the command you ran and the error message you received.