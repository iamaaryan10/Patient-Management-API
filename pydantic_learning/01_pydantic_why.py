from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name : Annotated[str, Field(max_length=50, title='Name of Patient', description='Give name of the patient in less than 50 characters', example='Alice')] # str = Field(max_length=60)
    email : EmailStr
    linkedin : AnyUrl
    age : int = Field(gt=0, lt=120)
    weight : float = Field(gt=0)
    married : bool = False # Default is false
    allergies : Optional[List[str]] = Field(default=None, max_length=5) # Optional and Default is none
    contact_details : Dict[str, str]

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print("updated")

patient_info = {'name':'Aaryan', 
                'email' : "abc@gmail.com",
                'age' : '22', 
                'weight' : 60.2, 
                'married' : True ,
                'allergies' : ['cough', 'fever'], 
                'contact_details' : {'Phone' : '95959595', 'email' : 'aaryan@123'}
                }

patient1 = Patient(**patient_info)

update_patient_data(patient1)


