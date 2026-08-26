from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

app = FastAPI()

class Patient(BaseModel):

    id : Annotated[str, Field(..., description='ID of the patient', examples=['P123'])]
    name : Annotated[str, Field(..., description='Name of the patient', examples=['Alice Gotham'])]
    city: Annotated[str, Field(..., description='Enter your residential city', examples=['Gaziyabad'])]
    age : Annotated[int, Field(...,gt=0, lt=121, description='Enter your current age', examples=[34])]
    gender : Annotated[Literal['male', 'female', 'other'], Field(..., description='Gender of Patient')]
    height : Annotated[float, Field(..., gt = 0, description='Height of the patient in meters')]
    weight : Annotated[float, Field(..., gt = 0, description='Weight of the patient in kilograms')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round((self.weight) / (self.height ** 2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5 :
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open("patients.json", 'w') as f:
        json.dump(data, f)

@app.get("/")
def hello():
    return {'message' : 'Patient Management System API'}

@app.get("/about")
def about():
    return {'message' : 'A fully functional API to manage your patient records'}

@app.get("/view")
def view():
    data = load_data()

    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description='ID of patient in the DB', example='P123')):
    # load the patient
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description='Dort in the basis of height or weight or bmi'), order: str = Query('asc', description='Sort in asc or desc order')):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')

    if order not in ['asc', 'desc']:
            raise HTTPException(status_code=400, detail=f'Invalid field select from {['asc', 'dsc']}')

    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse = sort_order)

    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):

    # load exisiting data
    data = load_data()

    # check if pid already exisit
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exisit')

    # new patient add to database
    data[patient.id] = patient.model_dump(exclude=['id'])

    #save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message' : 'Patient created successfully'})