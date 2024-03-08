from fastapi.testclient import TestClient
from proyecto.main import app

client = TestClient(app)

def test_get_item_names():
    response = client.get("/api/inventario/nombres")
    assert response.status_code == 200
    assert response.json() == []

def test_add_item():
    item_data = {"nombre": "Artículo de prueba", "descripcion": "Descripción de prueba", "cantidad": 10, "precio": 5.0}
    response = client.post("/api/inventario/agregar", json=item_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Artículo agregado correctamente"}

def test_delete_item():
    item_data = {"nombre": "Artículo de prueba", "descripcion": "Descripción de prueba", "cantidad": 10, "precio": 5.0}
    client.post("/api/inventario/agregar", json=item_data)  # Agregar un artículo para probar su eliminación
    response = client.delete("/api/inventario/Artículo%20de%20prueba")
    assert response.status_code == 200
    assert response.json() == {"message": "Artículo eliminado correctamente"}

# Agrega más pruebas para otras rutas y funcionalidades según sea necesario...
