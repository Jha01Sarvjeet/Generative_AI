from pydantic import BaseModel,EmailStr,Field
from typing import Annotated , Optional


class Student(BaseModel):
    name:str="test"
    age:Optional[int]=None
    email:Optional[EmailStr]=None
    cgpa:int=Field(lt=100,gt=5,description="count should be in ramge fo 5 and 100")
    
    
    
new_student={"name":"sarvjeet","cgpa":95}

student=Student(**new_student)

print(student)
    