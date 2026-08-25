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

# type -> dict
temp1 = patient1.model_dump(include=['name'])
temp2 = patient1.model_dump(exclude=['name'])
temp3 = patient1.model_dump()

# type -> str
temp4 = patient1.model_dump_json(include=['name'])
temp5 = patient1.model_dump_json(exclude=['name'])
temp6 = patient1.model_dump_json()
temp7 = patient1.model_dump_json(exclude={'address':['state']})

# exclude_unset is used when we don't want to export default values given by pydantic

print(temp1)
print(temp2)
print(temp3)
print(temp4)
print(temp5)
print(temp6)
print(temp7)