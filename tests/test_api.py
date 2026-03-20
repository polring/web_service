"""JSON API - 5개 기능 RED 테스트"""
from app import create_app


# ========== 기능 1: GET /api/profile ==========
def test_api_profile_returns_json():
    """GET /api/profile → 200, 프로필 JSON 반환"""
    app = create_app()
    client = app.test_client()
    response = client.get("/api/profile")
    assert response.status_code == 200
    assert response.content_type == "application/json"
    data = response.get_json()
    assert "name" in data
    assert data["name"] == "전민제"


# ========== 기능 2: GET /api/projects ==========
def test_api_projects_returns_list():
    """GET /api/projects → 200, 프로젝트 목록 JSON 반환"""
    app = create_app()
    client = app.test_client()
    response = client.get("/api/projects")
    assert response.status_code == 200
    assert response.content_type == "application/json"
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "title" in data[0]
    assert "description" in data[0]


# ========== 기능 3: GET /api/projects/<id> ==========
def test_api_project_detail_returns_json():
    """GET /api/projects/1 → 200, 해당 프로젝트 상세 JSON 반환"""
    app = create_app()
    client = app.test_client()
    response = client.get("/api/projects/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == "1"
    assert "title" in data
    assert "description" in data


def test_api_project_detail_not_found():
    """GET /api/projects/999 → 404"""
    app = create_app()
    client = app.test_client()
    response = client.get("/api/projects/999")
    assert response.status_code == 404


# ========== 기능 4: GET /api/notes ==========
def test_api_notes_returns_list():
    """GET /api/notes → 200, 노트 목록 JSON 반환"""
    app = create_app()
    client = app.test_client()
    response = client.get("/api/notes")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "title" in data[0]
    assert "content" in data[0]


# ========== 기능 5: GET /api/notes/<id> ==========
def test_api_note_detail_returns_json():
    """GET /api/notes/1 → 200, 해당 노트 상세 JSON 반환"""
    app = create_app()
    client = app.test_client()
    response = client.get("/api/notes/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == "1"
    assert "title" in data
    assert "content" in data


def test_api_note_detail_not_found():
    """GET /api/notes/999 → 404"""
    app = create_app()
    client = app.test_client()
    response = client.get("/api/notes/999")
    assert response.status_code == 404
