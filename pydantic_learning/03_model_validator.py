from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional, Annotated

# If age of a person is more than 60 he has to have a emergency contact details or else he won't be able to create his ID

class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]

    @model_validator(mode='after')
    def emergency_contact_validation(self):
        if self.age >= 60 and 'emergency' not in self.contact_details:
            raise ValueError("Patients older than 60 should add a emergency contact")
        else:
            return self


patient_info = {'name':'Aaryan', 
                'email' : "abc@hdfc.com",
                'age' : 60, 
                'weight' : 60.2, 
                'married' : True ,
                'allergies' : ['cough', 'fever'], 
                'contact_details' : {'Phone' : '95959595', 'email' : 'aaryan@123', 'emergency': '123456789'}
                }

patient1 = Patient(**patient_info)

def create_user(patient: Patient):

    print(patient.name)
    print(patient.contact_details)
    print('Successfully created a patient')

create_user(patient1)