from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

person = Person(name="Alice", age=30)

new_person: Person= {'name':'bob', 'age': "25"} # now if i pass 25 as a string then there is no problem  

print(new_person)

