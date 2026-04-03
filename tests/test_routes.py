def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200


def test_skills_route(client):
    response = client.get("/skills")
    assert response.status_code == 200


def test_projects_route(client):
    response = client.get("/projects")
    assert response.status_code == 200


def test_contact_route(client):
    response = client.get("/contact")
    assert response.status_code == 200


def test_about_route(client):
    response = client.get("/about")
    assert response.status_code == 200
