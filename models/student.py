"""
Creamos en el archivo models/student.py. Estos modelos definen como se 
veran nuestros datos de estudiante.
"""
# models/student.py
from pydantic import BaseModel

class Student(BaseModel):
    id: int
    nombre: str
    edad: int
    carrera: str
    promedio: float

