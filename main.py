from fastapi import FastAPI
from ModelName import ModelName

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World!"}


# path parameter starts
@app.get('/items/{item_id}')
async def read_item(item_id:int):
    return {"item_id": item_id}

@app.get('/models/{model_name}')
async def get_model(model_name:ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning"}
    
    if model_name.value == ModelName.restel:
        return {"model_name": model_name, "message": "path is restel"}
    return {"model_name": model_name}

@app.get('/files/{file_path:path}')
async def read_file(file_path:str):
    return {"file_path": file_path}

# path parameter ends

# Query Paramters Starts

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]

@app.get('/items/')
async def read_item(skip:int = 0, limit:int = 10):
    return fake_items_db[skip:skip+limit]

# optional parameter
from typing import Union
@app.get('/item/{item_id}')
def read_item(item_id:str, q:Union[float, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# query parameter type conversion
@app.get('/itemdet/{item_id}')
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id":item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"amazing item"})
    return item

# Multiple path and query parameters
@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id:int, item_id:str, q:Union[str,None] = None, short:bool = False):
    item = {"item_id": item_id, "user_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"desc":"Item has long description"})
    return item

