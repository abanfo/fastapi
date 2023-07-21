
from routers.schemas import PostCreate
from fastapi import HTTPException,status,Response
from db.database import get_db
from sqlalchemy.orm.session import Session
from db.model import Post
import datetime
from auth.aouth2 import get_current_user
# def get_all():
#     cursor.execute("""SELECT * FROM public.post""")
#     posts = cursor.fetchall()
#     return posts
# def get_post(id:int):
#     cursor.execute("""SELECT * FROM public.post where id = %s""",(str(id)))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f' the post with id {id} is not found')
#     return{'post_detail':post}
# def create(post:Post):
#     cursor.execute("""INSERT INTO post (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
#     new_post = cursor.fetchone()
#     conn.commit()
#     return new_post

# def delete(id :int):
#     cursor.execute("""DELETE FROM post WHERE id =%s RETURNING * """,(str(id),))
#     delete_post = cursor.fetchone()
#     conn.commit()
#     if not delete_post:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f' the post with id {id} is not found')
#     return 'ok'

# def update_post(id: int, post: Post):
#     cursor.execute("""UPDATE post set title = %s, content=%s, published =%s WHERE id = %s RETURNING *""",(post.title,post.content,post.published,str(id)))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     if not updated_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id {id} doesnt exist')
#     return updated_post

def get_all(db: Session, limit: int):
    return db.query(Post).limit(limit=limit).all()

def create(db:Session,request: PostCreate, owner_id: int):
    new_post = Post(
        **request.dict()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
def get_post(id:int,db:Session):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f' the post with id {id} is not found')
    return{'post_detail':post}

def delete(id :int,db:Session, user_id: int):
    post_query = db.query(Post).filter(Post.id == id)
    post = post_query.first()  


    if post == None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f' the post with id {id} is not found')
    if post.owner_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f' you cant delete that doesnt belong to u')
    post_query.delete(synchronize_session=false)
    db.commit()
    return 'ok'
def update_post(id: int, request: PostCreate,db:Session, user_id: int):
    updated_post = db.query(Post).filter(Post.id == id)
    post = updated_post.first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id {id} doesnt exist')
    if post.owner_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'you cant delete that doesnt belong to u')
    updated_post.update(request.dict(),synchronize_session=False)
    db.commit()

    return updated_post.first()