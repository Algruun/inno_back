from sqlalchemy.orm import Session

import models


def get_pizza(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pizza).offset(skip).limit(limit).all()
