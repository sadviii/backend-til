from database import SessionLocal, Employee

session = SessionLocal()

employee = Employee(
    id=1,
    name="Rahul",
    department="Engineering"
)

session.add(employee)
session.commit()

session.close()

print("Employee added")