from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

# Create database engine
engine = create_engine("sqlite:///company_orm.db")

# Base class for ORM models
class Base(DeclarativeBase):
    pass


# Employee table
class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id")
    )
    department: Mapped["Department"] = relationship()

# Department table
class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    department_name: Mapped[str] = mapped_column()


# Create tables if they don't already exist
Base.metadata.create_all(engine)


# Open a database session
with Session(engine) as session:
    employee = session.query(Employee).filter_by(id=1).first()

    employee.name = "Ravi"

    session.commit()

    print(employee.id, employee.name, employee.department_id)

with Session(engine) as session:
    employee = session.query(Employee).filter_by(id=1).first()

    print(employee.name)
    print(employee.department_id)
    print(employee.department)


with Session(engine) as session:
    # Create the HR department
    hr_department = Department(id=20, department_name="HR")
    session.add(hr_department)
    session.commit()

    # Create Priya as an employee belonging to HR
    priya = Employee(id=3, name="Priya", department_id=20)
    session.add(priya)
    session.commit()

    # Read Priya using her employee ID
    employee = session.query(Employee).filter_by(id=3).first()
    print(employee.name)  # Output: Priya
    print(employee.department.department_name)  # Output: HR

    # Update Priya's name to "Priya Sharma"
    employee.name = "Priya Sharma"
    session.commit()

    # Read her again and print
    updated_employee = session.query(Employee).filter_by(id=3).first()
    print(updated_employee.name)  # Output: Priya Sharma
    print(updated_employee.department.department_name)  # Output: HR

    # Delete Priya
    session.delete(updated_employee)
    session.commit()

    # Verify that employee ID 3 no longer exists
    deleted_employee = session.query(Employee).filter_by(id=3).first()
    if deleted_employee is None:
        print("Employee ID 3 no longer exists.")  # Output: Employee ID 3 no longer exists.