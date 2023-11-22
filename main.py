from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.Post, db: Session = Depends(get_db)):
    post_obj = crud.get_post(db, pid=post.id)
    if post_obj:
        raise HTTPException(status_code=400, detail="Post with same id already exists")
    else:
        print(post)
        post_out = crud.create_post(db=db, post=post)

        return post_out


@app.get("/posts/", response_model=list[schemas.Post])
def get_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts


@app.get("/posts/{pid}", response_model=schemas.Post)
def get_post(pid: int, db: Session = Depends(get_db)):
    post = crud.get_post(db,pid=pid)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


