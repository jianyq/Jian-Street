from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .db import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@app.post("/questionnaires/", response_model=schemas.Questionnaire)
def create_questionnaire(q: schemas.QuestionnaireCreate, db: Session = Depends(get_db)):
    return crud.create_questionnaire(db, q)



@app.post("/messages/", response_model=schemas.ChatMessage)
def create_message(msg: schemas.ChatMessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db, msg)


@app.get("/conversations/{conversation_id}", response_model=list[schemas.ChatMessage])
def read_messages(conversation_id: int, db: Session = Depends(get_db)):
    return crud.get_messages(db, conversation_id)

@app.get("/score/{conversation_id}")
def get_score(conversation_id: int, db: Session = Depends(get_db)):
    return {"score": crud.calculate_score(db, conversation_id)}
