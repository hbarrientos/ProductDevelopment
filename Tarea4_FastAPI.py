
from fastapi import FastAPI
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import ORJSONResponse
from fastapi.responses import UJSONResponse
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, StreamingResponse, FileResponse
import functools
import operator

app = FastAPI()

### TAREA 4 ###

@app.post("/add")
def add(list_item: list[int]):
    return sum(list_item)


@app.post("/sub")
def sub(list_item: list[int]):
    return functools.reduce(operator.sub, list_item)


@app.post("/mult")
def mult(list_item: list[int]):
    return functools.reduce(operator.mul, list_item)


@app.post("/div")
def div(list_item: list[int]):
    return functools.reduce(operator.truediv, list_item)


class MathOperation(str, Enum):
    add = "Addition"
    sub = "Subtraction"
    mul = "Multiplication"
    div = "Division"


@app.post("/execute/{operation}")
def execute_math_operation(operation: MathOperation, list_item: list[int]):
    if (operation == MathOperation.add):
        return add(list_item)
    elif (operation == MathOperation.sub):
        return sub(list_item)
    elif (operation == MathOperation.mul):
        return mult(list_item)
    elif (operation == MathOperation.div):
        return div(list_item)

### TAREA 4 ###



class RoleName(str, Enum):
    reader = "Reader"
    writer = "Writer"
    admin = "Admin"


fake_items_db = [{"item_name": "uno"}, {"item_name": "dos"}, {"item_name": "tres"}]


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")
def root():
	return {"message": "Hello World, from Galileo master"}


@app.get("/items/all", response_class=ORJSONResponse)
def read_all_items():
    return [{"item_id":"un item"}, {"item_id":"un item"}, {"item_id":"un item"}, {"item_id":"un item"}, {"item_id":"un item"}, {"item_id":"un item"}, {"item_id":"un item"}, {"item_id":"un item"}]


@app.get("/items/all/alternative", response_class=UJSONResponse)
def read_all_items():
    return [{"item_id":"un item"}, {"item_id":"un item"}, {"item_id":"un item"}, {"item_id":"un item"}, {"item_id":"un item"}, {"item_id":"un item"}, {"item_id":"un item"}, {"item_id":"un item"}]


#parametros de path
@app.get("/items/{item_id}")
def read_item(item_id: int, query: Optional[str]=None):
    if (query):
        return {"item_id": item_id, "query": query}
	
    return {"item_id": item_id}


# el orden es importante, en el caso de lo metodos siguientes, son parecidas las URLs y se ejecuta la primera.
@app.get("/users/{user_id}")
def read_current(user_id: str):
	return {"user_id": user_id}

@app.get("/users/current")
def read_current_user():
	return {"user_id": "The current user"}


@app.get("/roles/{rolename}")
def get_role_permissions(rolename: RoleName):
    if (rolename == RoleName.reader):
        return {"role": rolename, "permissions": "You are allowed only to read."}
    if (rolename == "Writer"):
        return {"role": rolename, "permissions": "You are allowed only to write."}
    return {"role": rolename, "permissions": "You have all access."}


@app.get("/items")
def read_all(skip:int=0, limit:int=10):
    return fake_items_db[skip: skip+limit]


@app.get("/users/{user_id}/items/{item_id}")
def read_user_items(user_id:int, item_id:int, query:Optional[str]=None, short:bool=False):
    items = {"item_id": item_id, "owner": user_id}
    if (query):
        items.update({"query": query})
    if (not short):
        items.update({"description": "This is a logn description for the selected item"})
    return items


@app.post("/items")
def create_item(item: Item):
    if (not item.tax):
        item.tax = item.price * 0.12
    return {"item_id": random.randint(1,100), **item.dict()}


@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
    return {"msg": f"El item {item_id} fue actualizado.", "item":item.dict()}


# sin el response_class, se devolveria un texto y no el html renderizado
@app.get("/html", response_class=HTMLResponse)
def get_html():
    return """
    <html><head><title></title></head>
    <body><h1>Look in to HTML</h1></body>
    </html>
    """


@app.get("/legacy")
def get_legacy():
    return """<?xml version="1.0"?>
    <shampoo><Header>Apply shampoo here</Header></shampoo>
    """


@app.get("/plain", response_class=PlainTextResponse)
def get_text():
    return "Hello World!"


@app.get("/redirect")
def get_redirect():
    return RedirectResponse("https://google.com")


@app.get("/video")
def show_video():
    video_file = open("ejemplo.mp4", mode="rb")
    return StreamingResponse(video_file, media_type="video/mp4")
    

@app.get("/video/download")
def download_video():
    return FileResponse("ejemplo.mp4")


def download_video():
    df = pd.DataFrame({"col1":[1,2], "col2":[3,4]})
    stream = io.StrinIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment"
    return 
    
    
# Tarea agregar 4 operaciones> suma, resta, multi, division. Que reciba un arreglo y que los opere, segun la operacion.
# 5 endpoints, uno para cada operacion y uno donde vaya como parametro.



