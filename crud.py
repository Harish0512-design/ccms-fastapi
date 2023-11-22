from sqlalchemy.orm import Session

from models import Post
import schemas


def create_post(db: Session, post: schemas.Post):
    print(post)
    post_obj = Post(id=post.id, title=post.title, content=post.content, category=post.category)
    db.add(post_obj)
    db.commit()
    db.refresh(post_obj)
    return post_obj


def get_post(db: Session, pid: int):
    return db.query(Post).filter(Post.id == pid).first()


def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()


