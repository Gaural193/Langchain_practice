from pydantic import BaseModel, EmailStr, Field 
from typing import Optional 

# -----------------------------------< Basic Pydantic Example >-----------------------------------------
# class Student(BaseModel):
#     name: str


# newstudent = {'name':"gaural"} # here we can only pass a value in str because in above class we have defined name as str. we cant do this in TypedDict. 



# student = Student(**newstudent)

# print(student)
# print(type(student))

## ----------------------------------< how to set default values>----------------------------------------
# class Student(BaseModel):
#     name: str = "Gaural"

# newstudent = {}

# student = Student(**newstudent)
# print(student)
# print(student.name) #it will print the default value "Gaural"

## -----------------------------------------------< Optional Fields >-----------------------------------------

# class Student(BaseModel):
#     name: str = "Gaural"
#     age: Optional[int] = None #if we don't pass age, it will be None


# newstudent = {'age': 25,}  #if we pass age as a str then pydantic is smart enough to convert it to int this is called type coercion and Type coercion.

# student = Student(**newstudent)
# print(student)
# print(type(student.age)) #it will print None

# --------------------------------------------< EmailStr in pydantic >-----------------------------------------

# class Student(BaseModel):
#     name: str = "Gaural"
#     age: Optional[int] = None 
#     email: EmailStr #this will ensure that the email is a valid email address

# newstudent = {'age': 25, 'email': 'gaural.com'}  #this will raise a validation error because 'gaural.com' is not a valid email address
# newstudent = {'age': 25, 'email': 'gaural@example.com'} #this will not raise an error

# student = Student(**newstudent)
# print(student)
# print(type(student.age)) #it will print None
# print(type(student.email)) #it will print <class 'pydantic.types.EmailStr'>

# --------------------------------------< Constraints in Pydantic   >-----------------------------------------

class Student(BaseModel):
    name: str = "Gaural"
    age: Optional[int] = None
    email: EmailStr
    cgps: float = Field(ge=0, le=10, default=5) #Now this will ensure that the CGPA is between 0 and 10

new_student = {'age': 25, 'email': 'gaural@example.com', 'cgps': 5, 'description': 'A decimal value representing the CGPS of student'} # this description is just line Annotated in TypedDict. the description helps explain what the field means.

student = Student(**new_student)

student_dict = dict(student) # we can use the dict() function to convert the Pydantic model instance to a dictionary
print(student_dict['age'])

