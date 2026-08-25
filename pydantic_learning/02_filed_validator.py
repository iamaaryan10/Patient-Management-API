from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        return value

def update_patient(patient: Patient):

    print(patient.name)
    print(patient.email)
    print('updated')


patient_info = {'name':'Aaryan', 
                'email' : "abc@hdfc.com",
                'age' : '22', 
                'weight' : 60.2, 
                'married' : True ,
                'allergies' : ['cough', 'fever'], 
                'contact_details' : {'Phone' : '95959595', 'email' : 'aaryan@123'}
                }

patient1 = Patient(**patient_info)

update_patient(patient1)