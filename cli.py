from models import Student, Employee, Person
from database import get_session
import logging

def register():
    """Register a new student or employee."""
    with get_session() as session:  # Using session as a context manager
        # Take user input for personal details
        print("Enter the details of the person to register:")
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        email = input("Email: ").strip()

        # Ensure fields are not empty
        if not first_name or not last_name or not email:
            print("All fields are required.")
            return

        # Check if the person already exists by email
        existing_person = session.query(Person).filter(Person.email == email).first()
        if existing_person:
            print(f"A person with email {email} already exists.")
            return

        # Take user input for grade or department (based on type of person)
        grade = None
        department = None
        while True:
            user_type = input("Are you registering a student or an employee? (Enter 'student' or 'employee'): ").strip().lower()

            if user_type == "student":
                grade = input("Enter the grade: ").strip()
                break
            elif user_type == "employee":
                department = input("Enter the department: ").strip()
                break
            else:
                print("Invalid option. Please choose either 'student' or 'employee'.")

        # Register person in the database (id is auto-generated)
        person = Person(first_name=first_name, last_name=last_name, email=email)
        try:
            session.add(person)
            session.commit()  # Commit to generate the `id` for the person
        except Exception as e:
            session.rollback()
            print(f"Error registering person: {e}")
            return

        # After committing, the person will have a valid `id`. Now create the student or employee record.
        if grade:
            student = Student(grade=grade)  # Do not set id here, let SQLAlchemy handle it
            session.add(student)
        elif department:
            employee = Employee(department=department)  # Do not set id here, let SQLAlchemy handle it
            session.add(employee)

        # Commit to save the student or employee record
        try:
            session.commit()  # Commit after adding student or employee
            print(f"Successfully registered {first_name} {last_name} as a {user_type}.")
        except Exception as e:
            session.rollback()
            print(f"Error registering {user_type}: {e}")


def list_people():
    """List all registered people."""
    with get_session() as session:  # Using session as a context manager
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
