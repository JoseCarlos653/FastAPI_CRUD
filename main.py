"""
Finalmente, configuramos la aplicacion principal en main.py
para incluir las rutas de los estudiantes. 
"""

# main.py
from fastapi import FastAPI
from routes.student import router as student_router

app = FastAPI()
app.title = 'CRUD Estudiantes'
app.version = '1.0.0'

app.include_router(student_router, prefix='/api')

@app.get('/', tags=['home'])
def read_root():
    return {'message': 'Bienvenidos a la API de gestion de estudiantes'}