from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    weight : float
    height : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round((self.weight / (self.height ** 2)), 2)
        return bmi

patient_info = {'name':'Aaryan', 
                'email' : "abc@hdfc.com",
                'age' : 60, 
                'weight' : 60.2, 
                'height' : 1.78,
                'married' : True ,
                'allergies' : ['cough', 'fever'], 
                'contact_details' : {'Phone' : '95959595', 'email' : 'aaryan@123', 'emergency': '123456789'}
                }


patient1 = Patient(**patient_info)

def update_patient(patient: Patient):
    print('BMI', patient.calculate_bmi)

update_patient(patient1)
