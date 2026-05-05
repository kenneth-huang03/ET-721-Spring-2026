import os
import pytest
import sqlite3


from app import App



TEST_DATABASE = "test_flask_auth.db"



@pytest.fixture
def client(monkeypatch):
    """This should really be called client and database setup and not just client but whatever"""

    def get_database_connection():
        connection = sqlite3.connect(TEST_DATABASE)
        connection.row_factory = sqlite3.Row
        return connection
    
    monkeypatch.setattr("app.get_database_connection", get_database_connection)
    App.config["TESTING"] = True
    App.config["SECRET_KEY"] = "test_secret_key"


    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (" \
                "id INTEGER PRIMARY KEY AUTOINCREMENT," \
                "username TEXT NOT NULL," \
                "email TEXT UNIQUE NOT NULL," \
                "password TEXT NOT NULL" \
        ')'
    )

    connection.commit()
    connection.close()


    with App.test_client() as c: yield c
    
    if os.path.exists(TEST_DATABASE):
        os.remove(TEST_DATABASE)



def test_home_redirect(client):
    response = client.get('/')

    assert response.status_code == 302
    assert "/login" in response.location


def test_signup_success(client):
    response = client.post("/signup", data = {
        "username": "test-user",
        "email": "test-user@test-user.test-user",
        "password": "test"
    })

    assert response.status_code == 302
    assert "/login" in response.location

    
def test_login_success(client):
    client.post("/signup", data = {
        "username": "test-user",
        "email": "test-user@test-user.test-user",
        "password": "test"
    })

    response = client.post("/login",
        data = {
            "email": "test-user@test-user.test-user",
            "password": "test"
        },
        follow_redirects = True
    )


    assert response.status_code == 200
    assert b"Welcome" in response.data


def test_login_failiure(client):
    response = client.post("/login", data = {
        "email": "fake-test-user@fake-test-user.fake-test-user",
        "password": "test",
    })


    assert response.status_code == 302
    assert "/login" in response.location
