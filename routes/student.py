"""
Las rutas definidas los endpoints de la API y utilizaron los servicios 
para realizar las operaciones CRUD. Definimos esto en routes/student.py
"""

# routes/student.py
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from typing import List
from models.student import Student
from services.student import get_all_students, get_student_by_id, create_student, update_student, delete_student, export_students_to_excel

router = APIRouter()

@router.get('/students', response_model=List[Student], tags=['students'])
def read_students():
    return get_all_students()

@router.get('/students/{student_id}', response_model=Student, tags=['students'])
def read_student(student_id: int):
    student = get_student_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail='Student not found')
    return student

@router.post("/students", response_model=Student, tags=["students"]) 
def create_student_endpoint(student: Student):
    return create_student(student)

@router.put("/students/{student_id}", response_model=Student, tags=["students"]) 
def update_student_endpoint(student_id: int, student: Student): 
    updated_student = update_student(student_id, student)
    if updated_student is None:
        raise HTTPException (status_code=404, detail="Student not found") 
    return updated_student

@router.delete("/students/{student_id}", tags=["students"]) 
def delete_student_endpoint(student_id: int):
    success = delete_student(student_id)
    if not success:
        raise HTTPException (status_code=404, detail="Student not found") 
    return {"message": "Student deleted successfully"}

@router.post('/students/export', tags=['students'])
def export_students():
    file_path = export_students_to_excel()
    return FileResponse(path=file_path, filename='estudiantes.xlsx',
                        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

