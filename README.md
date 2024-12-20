# Phase-3-Final-Project

## Student and Employee Registration System

This is a simple command-line interface (CLI) application built in Python that allows users to register students and employees. The application uses SQLAlchemy ORM for database management and SQLite as the database engine.

### Features:

- Register a new student or employee.
- List all registered students and employees.
- Store personal information like name, email, grade (for students), and department (for employees).

### Prerequisites
Before you begin, ensure you have the following installed:

- Python 3.x
- SQLite (comes pre-installed with Python)
- pipenv (for managing dependencies)

### Installation

#### Step 1: Clone the Repository
Git clone the project to your machine -(https://github.com/Yuongren/Phase-3-Final-Project)
and then navigate to the the repository from your machine by runinning cd Phase-3-Final-Project

#### Step 2: Set up the Virtual Environment
Install dependencies using pipenv. If you don't have pipenv installed, you can install it using:

pip install pipenv
Then, install the necessary dependencies for the project:

pipenv install

#### Step 3: Activate the Virtual Environment
Activate the virtual environment where all dependencies are installed by running the following command: pipenv shell

### Usage

#### 1.Register a New Person
You can register either a student or an employee by providing the necessary details.

Run the following command to start the registration process:
python cli.py

#### Example of Registering a Student:

--- Registration System ---
1. Register a new person
2. List all registered people
3. Exit
Choose an option (1/2/3): 1
Enter the details of the person to register:
First Name: John
Last Name: Doe
Email: johndoe@example.com
Are you registering a student or an employee? (Enter 'student' or 'employee'): student
Enter the grade: A
Successfully registered John Doe as a student.

#### Example of Registering an Employee:

Choose an option (1/2/3): 1
Enter the details of the person to register:
First Name: Jane
Last Name: Smith
Email: janesmith@example.com
Are you registering a student or an employee? (Enter 'student' or 'employee'): employee
Enter the department: HR
Successfully registered Jane Smith as an employee.

#### 2. List All Registered People
You can list all registered people (both students and employees) by choosing the option to list people.

Choose an option (1/2/3): 2
Registered People:
Student: John Doe, Grade: A, Email: johndoe@example.com
Employee: Jane Smith, Department: HR, Email: janesmith@example.com

#### 3. Exit the Program
To exit the program, choose option 3 from the main menu.

## How It Works
The registration system consists of the following components:

### Database Setup (database.py):

 - Uses SQLAlchemy to connect to an SQLite database (registration.db).
 - Creates three tables: people, students, and employees.

### Models (models.py):

 - Defines three classes: Person, Student, and Employee.
 - Person is the base class containing shared attributes (first name, last name, email).
 - Student and Employee inherit from Person and add additional attributes (grade and department).

### CLI Interface (cli.py):

 - Uses input() and print() functions to interact with the user.
 - Allows the user to register a person as a student or employee and list all registered people.
- Uses SQLAlchemy to store and retrieve data from the 
SQLite database.

## Project Structure
graphql
Copy code
student-employee-registration/
│
├── database.py            # Database connection and session management
├── models.py              # Database models for Person, Student, and Employee
├── cli.py                 # Command-line interface (CLI) logic
├── registration.db        # SQLite database file (created on first run)
├── Pipfile                # pipenv dependency manager file
└── Pipfile.lock           # pipenv lock file


## Troubleshooting

### 1. Missing Dependencies
Ensure you have all the necessary dependencies installed by running: pipenv install

### 2. Database Issues
If you encounter database issues, try deleting the registration.db file (it will be recreated automatically) and then re-run the application.

### 3. Invalid Input
If you input an invalid option or data, the program will prompt you to enter the correct information again.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository, make changes, and create a pull request. Please ensure your code is well-documented and follows Python's PEP 8 guidelines.

## Author
Project is created by Youngren Gitonga (https://github.com/Yuongren/Phase-3-Final-Project).
For any questions or issues, please contact the at [youngrengitonga@gmail.com]

## License
This project is licensed under the MIT License - see the LICENSE file for details.
