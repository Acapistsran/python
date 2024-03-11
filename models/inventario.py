from pydantic import BaseModel

class Item(BaseModel):
    nombre: str
    descripcion: str
    cantidad: int
    precio: float
    ID: int
    
class ItemUpdate(BaseModel):
    nombre: str
    descripcion: str
    cantidad: int
    precio: float
    ID: int
