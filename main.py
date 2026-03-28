from fastapi import FastAPI, status
from models.db import db
from models.models import Sheep

app = FastAPI()


@app.get("/sheep/{sheep_id}")
def get_sheep(sheep_id: int):
    sheep = db.get_sheep(sheep_id)
    if sheep:
        return sheep
    return {"error": "Sheep not found"}


@app.post("/sheep/", status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    return db.add_sheep(sheep)


@app.put("/sheep/{sheep_id}")
def update_sheep(sheep_id: int, sheep: Sheep):
    updated = db.update_sheep(sheep_id, sheep)
    if updated:
        return updated
    return {"error": "Sheep not found"}