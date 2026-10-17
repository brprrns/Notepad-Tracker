from pathlib import Path

import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200


def test_save_file(client, tmp_path, monkeypatch):
    file_path = tmp_path / "test.txt"

    monkeypatch.setattr(
        "app.commit_file",
        lambda path: None,
    )

    response = client.post(
        "/save",
        json={
            "file_path": str(file_path),
            "content": "Hello World",
        },
    )

    assert response.status_code == 200
    assert file_path.read_text() == "Hello World"


def test_save_without_path(client):
    response = client.post(
        "/save",
        json={
            "content": "Hello",
        },
    )

    assert response.status_code == 400