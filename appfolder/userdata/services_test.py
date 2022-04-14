from pytest import fixture
from appfolder.tests.fixture import app, db
from appfolder.userdata.models import User

@fixture
def insert_test_data(db):
    data: User = User(username='aman120',emailid='aman@gmail.com',password='123')
    db.session.add(data)
    db.session.commit()


def test_get_by_id (insert_test_data, app, db) :
    with app.app_context():
        data= User.query.get(1)
        assert data.username=='aman120'

    

    
