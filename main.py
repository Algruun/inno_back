from typing import List, Dict

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/pizza/", response_model=Dict[str, List[schemas.Pizza]])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pizzas = crud.get_pizza(db, skip=skip, limit=limit)
    return {'products': pizzas}


if __name__ == '__main__':
    uvicorn.run(app, port=8001, host='0.0.0.0')
