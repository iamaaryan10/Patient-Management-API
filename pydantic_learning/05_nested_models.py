from pydantic import BaseModel


class Address(BaseModel):

    city : str
    state : str
    pincode : str

class Patient(BaseModel):

    name : str
    age : int
    address : Address

address_info = {"city" : "Sehore", "state" : "MP", "pincode" : "466114"}

address1 = Address(**address_info)

patient_info = {"name" : "Aaryan", "age" : 22, "address" : address1}

patient1 = Patient(**patient_info)

print(patient1)