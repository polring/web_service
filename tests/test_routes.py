from app import create_app


def test_home_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_skills_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/skills")
    assert response.status_code == 200


def test_projects_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/projects")
    assert response.status_code == 200


def test_contact_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/contact")
    assert response.status_code == 200
