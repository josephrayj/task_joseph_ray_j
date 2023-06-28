# Django Project Setup Guide

## Clone the Project Repository
- Open your terminal or command prompt.
- Change to the desired directory where you want to clone the project.
- Run the following command to clone the project repository:
```
git clone https://github.com/josephrayj/task_joseph_ray_j.git
```

## Install Dependencies
- Change into the project directory by running:
```
cd task_joseph_ray_j
```
- Install the required dependencies by running the following command:
```
pip install -r requirements.txt
```

## Database Setup
- Open the project's settings.py file located at `task_joseph_ray_j/task_joseph_ray_j/settings.py`.
- Configure the database settings according to your preference. By default, it uses a SQLite database.
- Once configured, save the file.

## Make Migrations and Migrate
- In the terminal or command prompt, run the following command to create the initial migrations:
```
python manage.py makemigrations
```
- Then, run the migrations using the following command:
```
python manage.py migrate
```

## Start the Development Server
- Start the development server by running the following command:
```
python manage.py runserver
```
# API Documentation

This documentation provides information about the APIs available in the Django project.

## Create Employee

- Endpoint: [POST /employee_create](# API Documentation

This documentation provides information about the APIs available in the Django project.

## Create Employee

- Endpoint: [POST /employee_create](http://127.0.0.1:8000/employee_create) - http://127.0.0.1:8000/employee_create
- Description: Creates a new employee record in the system.

## Get Employees

- Endpoint: [GET /employees](http://localhost:8000/employees) http://localhost:8000/employees
- Description: Retrieves a list of all employees.

## Delete Employee

- Endpoint: [DELETE /employee_delete](http://localhost:8000/employee_delete) http://localhost:8000/employee_delete
- Description: Deletes an employee record from the system.

## Update Employee

- Endpoint: [PUT /employee/{employee_id}](http://localhost:8000/employee/EMP002) http://localhost:8000/employee/EMP002
- Description: Updates the details of an existing employee.

Note: Replace `EMP001` and `EMP002` with the actual employee IDs.

That's it! You can use these APIs to perform CRUD operations on the employee records in the Django project.)
- Description: Creates a new employee record in the system.
