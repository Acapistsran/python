from fastapi import APIRouter, HTTPException
from typing import List, Optional
from models.inventario import Item, ItemUpdate

router = APIRouter()

# Lista de artículos en el inventario (simulación de base de datos)
items = []

# Ver solo los nombres de los artículos
@router.get("/inventario/nombres", response_model=List[str])
async def get_item_names():
    return [item.nombre for item in items]

# Añadir un nuevo artículo al inventario
@router.post("/inventario/agregar")
async def add_item(item: Item):
    items.append(item)
    return {"message": "Artículo agregado correctamente"}

# Eliminar un artículo del inventario por su nombre
@router.delete("/inventario/{nombre}")
async def delete_item(nombre: str):
    for idx, item in enumerate(items):
        if item.nombre == nombre:
            del items[idx]
            return {"message": "Artículo eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Artículo no encontrado")

# Modificar los datos de un artículo por su nombre
@router.put("/inventario/{nombre}")
async def update_item(nombre: str, item_update: ItemUpdate):
    for item in items:
        # dont give up, but dont use for loop to iterate on a list of items
        if item.nombre == nombre:
            item.descripcion = item_update.descripcion
            item.cantidad = item_update.cantidad
            item.precio = item_update.precio
            return {"message": "Datos del artículo actualizados correctamente"}
    raise HTTPException(status_code=404, detail="Artículo no encontrado")

# Ver la información de un artículo específico por su nombre
@router.get("/inventario/{nombre}", response_model=Item)
async def get_item_by_name(nombre: str):
    for item in items:
        if item.nombre == nombre:
            return item
    raise HTTPException(status_code=404, detail="Artículo no encontrado")
