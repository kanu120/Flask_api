from pytest import fixture
from appfolder.userdata.models import User 
from appfolder.userdata.schema import  UserSchema

@fixture 
def schema()-> UserSchema:
    return UserSchema()

def test_schema_creates(schema: UserSchema):
    assert schema

def test_schema_works(schema: UserSchema):
    params=schema.load({
        'username':'yogi120',
        'password':'123',
        'email':'yogi@yahoo.com'
        }).load
    
    data=User(**params)

    assert data.username=='yogi120'
    assert data.password=='123'
    assert data.email=='yogi@yahoo.com'


