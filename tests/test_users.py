
from routers import schemas
from .database import client,session


def test_creat(client):
    res = client.post('/user', json={"email":"email@gmail.com","password":"pass"})
    new_user = schemas.UserDisplay(**res.json())
    assert new_user.email == "email@gmail.com"

