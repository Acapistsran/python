from fastapi.testclient import TestClient
from inventario import app, Item, ItemUpdate

client = TestClient(app)

def test_get_item_names():
	response = client.get("/inventario/nombres")
	assert response.status_code == 200

def test_add_item():
	item = Item(nombre="item1", descripcion="desc1", cantidad=10, precio=100.0)
	response = client.post("/inventario/agregar", json=item.dict())
	assert response.status_code == 200
	assert response.json() == {"message": "Artículo agregado correctamente"}

def test_get_item_by_name():
	response = client.get("/inventario/item1")
	assert response.status_code == 200
	assert response.json() == {"nombre": "item1", "descripcion": "desc1", "cantidad": 10, "precio": 100.0}

def test_update_item():
	item_update = ItemUpdate(descripcion="desc2", cantidad=20, precio=200.0)
	response = client.put("/inventario/item1", json=item_update.dict())
	assert response.status_code == 200
	assert response.json() == {"message": "Datos del artículo actualizados correctamente"}

def test_delete_item():
	response = client.delete("/inventario/item1")
	assert response.status_code == 200
	assert response.json() == {"message": "Artículo eliminado correctamente"}