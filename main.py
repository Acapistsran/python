from fastapi import FastAPI
from api import inventario  # Importa el módulo de rutas de inventario

app = FastAPI()

# Incluye las rutas del módulo de inventario
app.include_router(inventario.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
