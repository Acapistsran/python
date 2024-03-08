from fastapi.testclient import TestClient
from inventario import app

client = TestClient(app)

def test_create_item():
	item_data = {
		"nombre": "Item 1",
		"descripcion": "Descripción del item 1",
		"cantidad": 10,
		"precio": 9.99,
		"ID": 1
	}
	response = client.post("/items/", json=item_data)
	assert response.status_code == 201
	assert response.json() == item_data

def test_get_item():
	response = client.get("/items/1")
	assert response.status_code == 200
	assert response.json() == {
		"nombre": "Item 1",
		"descripcion": "Descripción del item 1",
		"cantidad": 10,
		"precio": 9.99,
		"ID": 1
	}

def test_update_item():
	item_data = {
		"nombre": "Item 1 actualizado",
		"descripcion": "Descripción actualizada del item 1",
		"cantidad": 5,
		"precio": 19.99,
		"ID": 1
	}
	response = client.put("/items/1", json=item_data)
	assert response.status_code == 200
	assert response.json() == item_data

def test_delete_item():
	response = client.delete("/items/1")
	assert response.status_code == 204
	assert response.content == b""
