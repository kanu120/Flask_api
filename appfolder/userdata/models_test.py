# from appfolder.tests import fixture
from pytest import fixture
from appfolder.userdata.models import User

@fixture
def user() -> User:
    return User(username=100, emailid='akash@gmail.com', password='123')

def test_user_create(user : User):
    assert user