from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated")

patient_info = {'name':'Aaryan', 'age' : '22'}

patient1 = Patient(**patient_info)

update_patient_data(patient1)


