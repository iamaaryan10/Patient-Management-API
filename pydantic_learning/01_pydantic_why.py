from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional

class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool = False # Default is false
    allergies : Optional[List[str]] = None # Optional and Default is none
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


