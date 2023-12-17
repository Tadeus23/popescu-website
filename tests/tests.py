import json
import pytest
from backend import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to My CV" in response.data


def test_get_personal_info_route(client):
    response = client.get('/personal')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert 'name' in data
    assert 'job' in data


def test_get_experience_route(client):
    response = client.get('/experience')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert isinstance(data, list)
    if data:
        assert 'title' in data[0]
        assert 'company' in data[0]


def test_get_education_route(client):
    response = client.get('/education')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert isinstance(data, list)
    if data:
        assert 'degree' in data[0]
        assert 'major' in data[0]


def test_get_skills_route(client):
    response = client.get('/skills')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert isinstance(data, list)
    if data:
        assert 'skill' in data[0]
        assert 'years_exp' in data[0]


def test_get_certifications_route(client):
    response = client.get('/certifications')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert isinstance(data, list)
    if data:
        assert 'name' in data[0]
        assert 'institute' in data[0]


if __name__ == '__main__':
    pytest.main()
