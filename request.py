from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


# create our datamodel
class Item(BaseModel):
    name: str
    description: Union[str, None]
    price: float
    tax: Union[float, None] = None

class Employee(BaseModel):
    fname: str
    lname: Union[str, None] = None
    age: int
    experience: int
    salary: float

app = FastAPI()

@app.post('/items/')
async def create_item(item: Item):
    return item

@app.post('/employee/')
async def create_employee(employee:Employee):
    fullName = employee.fname + (" " + employee.lname if employee.lname else "")
    return {"fullname": fullName, **employee.dict()}

@app.put('/employee/{emp_id}')
async def update_emp(employee: Employee, emp_id: int):
    return {"emp_id": emp_id, **employee.dict()}