from unittest.mock import patch
from flask.testing import FlaskClient

from appfolder.tests.fixture import db,app
import  appfolder.userdata.services as services
from appfolder.userdata.schema  import UserSchema
from appfolder.userdata.models import User
from appfolder.userdata import BASE_ROUTE
from appfolder.tests import fixture

@fixture
def make_user(uname: str='kanu111', pwd:str ='100', mailid: str ='q@gamil.com') -> User:
    return User( username=uname , password=pwd, emailid=mailid)

@fixture
class UserResource:
    @patch.object(services, 'get_by_id',
                  lambda: [make_user(uname='kanu111', pwd='100'),
                           make_user(uname='kanu222', pwd='200')])
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f'/api/{BASE_ROUTE}',
                                 follow_redirects=True).get_json()
            expected = UserSchema(many=True).dump(
                [make_user(uname='kanu111', pwd='100'),
                 make_user(uname='kanu222', pwd='200')]
            ).data
            for r in results:
                assert r in expected





