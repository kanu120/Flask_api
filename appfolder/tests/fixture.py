import pytest

from appfolder import connection

@pytest.fixture
def app():
    return connection('test')

@pytest.fixture
def db(app):
    from appfolder import db
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()
        db.session.commit()