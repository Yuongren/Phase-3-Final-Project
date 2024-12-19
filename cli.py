# cli.py
from models import Student, Employee, Person
from database import create_tables, get_session

# Create tables if they do not exist
create_tables()

def register():
    """Register a new student or employee."""
    session = get_session()

    # Take user input for personal details
    print("Enter the details of the person to register:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")

    # Check if the person already exists by email
    existing_person = session.query(Person).filter(Person.email == email).first()
    if existing_person:
        print(f"A person with email {email} already exists.")
        return

    # Take user input for grade or department (based on type of person)
    grade = None
    department = None
    user_type = input("Are you registering a student or an employee? (Enter 'student' or 'employee'): ").strip().lower()

    if user_type == "student":
        grade = input("Enter the grade: ")
    elif user_type == "employee":
        department = input("Enter the department: ")
    else:
        print("Invalid option. Please choose either 'student' or 'employee'.")
        return

    # Register person in the database
    person = Person(first_name=first_name, last_name=last_name, email=email)
    session.add(person)
    session.commit()

    if grade:
        student = Student(id=person.id, grade=grade)
        session.add(student)
    elif department:
        employee = Employee(id=person.id, department=department)
        session.add(employee)
    
    session.commit()
    print(f"Successfully registered {first_name} {last_name} as a {user_type}.")

def list_people():
    """List all registered people."""
    session = get_session()

    people = session.query(Person).all()
    if not people:
        print("No people registered yet.")
        return

    print("\nRegistered People:")
    for person in people:
        student = session.query(Student).filter(Student.id == person.id).first()
        employee = session.query(Employee).filter(Employee.id == person.id).first()

        if student:
            print(f"Student: {person.first_name} {person.last_name}, Grade: {student.grade}, Email: {person.email}")
        elif employee:
            print(f"Employee: {person.first_name} {person.last_name}, Department: {employee.department}, Email: {person.email}")

def main():
    """Main function to interact with the user."""
    while True:
        print("\n--- Registration System ---")
        print("1. Register a new person")
        print("2. List all registered people")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            register()
        elif choice == "2":
            list_people()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
