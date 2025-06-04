from sqlalchemy.orm import Session
from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_questionnaire(db: Session, q: schemas.QuestionnaireCreate):
    db_q = models.Questionnaire(user_id=q.user_id, answer=q.answer)
    db.add(db_q)
    db.commit()
    db.refresh(db_q)
    return db_q


def create_message(db: Session, msg: schemas.ChatMessageCreate):
    db_msg = models.ChatMessage(
        user_id=msg.user_id,
        conversation_id=msg.conversation_id,
        message=msg.message,
    )
    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)
    return db_msg


def get_messages(db: Session, conversation_id: int):
    return (
        db.query(models.ChatMessage)
        .filter(models.ChatMessage.conversation_id == conversation_id)
        .order_by(models.ChatMessage.timestamp)
        .all()
    )
