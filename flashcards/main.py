from fastapi import FastAPI
from route_teacher import router as teacher_router
from route_student import router as student_router


app = FastAPI()
app.include_router(teacher_router)
app.include_router(student_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Flashcard API!"}
