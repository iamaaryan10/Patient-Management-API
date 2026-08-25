from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

# Field validator can be used on a single field and if more than one field is to be validated at once or dependent on each other we use model validator

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

    @field_validator('name') # This validator will convert the name to uppercase
    @classmethod
    def name_transform(cls, name):
        return name.upper()

    @field_validator('age', mode='before') # before mode will get the value before type coersion 
    @classmethod
    def age_limit(cls, val):
        if 0 < val <= 100:
            return val
        else:
            raise ValueError("Age not in limit")

def update_patient(patient: Patient):

    print(patient.name)
    print(patient.email)
    print('updated')


patient_info = {'name':'Aaryan', 
                'email' : "abc@hdfc.com",
                'age' : 22, 
                'weight' : 60.2, 
                'married' : True ,
                'allergies' : ['cough', 'fever'], 
                'contact_details' : {'Phone' : '95959595', 'email' : 'aaryan@123'}
                }

patient1 = Patient(**patient_info)

update_patient(patient1)