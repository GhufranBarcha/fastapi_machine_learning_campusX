from fastapi import FastAPI, Path, Query, HTTPException
import json

app = FastAPI()

def load_data():
   with open("patients.json", "r") as f:
      data = json.load(f)
   return data   
   

@app.get("/")
def hello():
   return {"message":"Patient Managements System FastAPI"} 

@app.get("/about")
def about():
   return {"about": "A fastapi backend for patient management systems"}


@app.get("/view")
def view_data():
   
   data = load_data()
   return data


@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(..., description='ID of the patients in DB', example = 'Example: P001')):
   ## Load all the data
   data = load_data()
   
   if patient_id in data:
      return data[patient_id]
   raise HTTPException(status_code=404, detail = 'Patient not found')


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort based on bmi, weight and height'), order: str = Query('asc', description='Sort in asc or desc order')):
   valid_fields = ['height', 'weight', 'bmi']
   
   if sort_by not in valid_fields:
      raise HTTPException(status_code=400, detail=f'Invalid filed. Select between these {valid_fields}')
   
   if order not in ['asc', 'desc']:
      raise HTTPException(status_code=400, detail=f'Invalid filed. Select between these asc, desc')
   
   data  = load_data()
   

   sort_order = True if order=='desc' else False

   sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

   return sorted_data
   