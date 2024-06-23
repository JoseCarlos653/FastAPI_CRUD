"""
Los servicios contendran la logica de negocio, como agregar, actualizar y eliminar estudiantes.
Definimos esto en services/student.py
"""

#services/student.py
from typing import List, Optional
from models.student import Student
from openpyxl import Workbook

# Lista simulada de estudiantes
students_db: List[Student] = []

def get_all_students() -> List[Student]:
    return students_db

def get_student_by_id(student_id: int) -> Optional[Student]:
    for student in students_db:
        if student.id == student_id:
            return student
    return None

# Crear estudiante
def create_student(student: Student) -> Student:
    students_db.append(student)
    return student

# Actualizar estudiante
def update_student(student_id: int, student: Student) -> Optional[Student]:
    for idx, existing_student in enumerate(students_db):
        if existing_student.id == student_id:
            students_db[idx] = student
            return student
    return None

# Eliminar estudiante
def delete_student(student_id: int) -> bool:
    for idx, existing_student in enumerate(students_db):
        if existing_student.id == student_id:
            del students_db[idx]
            return True
    return False    

def export_students_to_excel() -> str:
    wb = Workbook()
    ws = wb.active
    ws.title = 'Estudiantes'

    # Agregar encabezados
    headers = ["ID", "Nombre", "Edad", "Carrera", "Promedio"]
    ws.append(headers)

    # Agregar datos de estudiantes
    for student in students_db:
        ws.append([student.id, student.nombre, student.edad, student.carrera, student.promedio])
    
    # Guardar el archivo
    file_path = "estudiantes.xlsx"
    wb.save(file_path)

    return file_path