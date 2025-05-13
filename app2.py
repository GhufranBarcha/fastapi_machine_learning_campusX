from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
   return {"message":"Hello world"} 



@app.get("/about")
def about():
   return {"about": "Learning fastapi using campusX by Ghufran Barcha"}
