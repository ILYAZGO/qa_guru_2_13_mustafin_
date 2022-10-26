import requests
from requests import Response
import schemas.schemas as schema
from pytest_voluptuous import S


def test_get_single_user():
    user_id = 2

    result: Response = requests.get(
        url="https://reqres.in/api/users" + "/" + str(user_id)
    )

    assert result.status_code == 200
    assert result.json()['data']['email'] == 'janet.weaver@reqres.in'
    assert len(result.json()['data']) != 0
    assert result.json() == S(schema.get_user_schema)


def test_get_single_user_not_found():
    user_id = 778

    result: Response = requests.get(
        "https://reqres.in/api/users" + "/" + str(user_id)
    )

    assert result.status_code == 404


def test_create_user():
    name = "ilias"
    job = "qa"

    result = requests.post(
        url="https://reqres.in/api/users",
        json={"name": name, "job": job}
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(schema.create_user_schema)


def test_patch_update_user():
    user_id = 5
    name = "ilias"
    job = "horse"

    result = requests.patch(
        url="https://reqres.in/api/users" + "/" + str(user_id),
        json={"name": name, "job": job}
    )

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(schema.update_user_schema)


def test_post_register_user():
    email = "eve.holt@reqres.in"
    password = "Zaq1@wsX"

    result = requests.post(
        url="https://reqres.in/api/register",
        json={"email": email, "password": password}
    )

    assert result.status_code == 200
    assert result.json() == S(schema.register_user_schema)


def test_post_login_user():
    email = "eve.holt@reqres.in"
    password = "Zaq1@wsX"

    result = requests.post(
        url="https://reqres.in/api/login",
        json={"email": email, "password": password}
    )

    assert result.status_code == 200
    assert result.json() == S(schema.login_user_schema)
