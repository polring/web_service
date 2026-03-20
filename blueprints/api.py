"""JSON API - 외부에서 데이터 조회"""
import json
from pathlib import Path

from flask import Blueprint, jsonify

bp = Blueprint("api", __name__, url_prefix="/api")
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"


def load_json(filename: str):
    path = DATA_DIR / filename
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def _find_by_id(items: list, id: str):
    """id로 항목 조회"""
    for item in items:
        if str(item.get("id")) == str(id):
            return item
    return None


# 기능 1: GET /api/profile
@bp.get("/profile")
def get_profile():
    profile = load_json("profile.json")
    return jsonify(profile)


# 기능 2: GET /api/projects
@bp.get("/projects")
def get_projects():
    projects = load_json("projects.json")
    return jsonify(projects)


# 기능 3: GET /api/projects/<id>
@bp.get("/projects/<id>")
def get_project(id):
    projects = load_json("projects.json")
    project = _find_by_id(projects, id)
    if project is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(project)


# 기능 4: GET /api/notes
@bp.get("/notes")
def get_notes():
    notes = load_json("notes.json")
    return jsonify(notes)


# 기능 5: GET /api/notes/<id>
@bp.get("/notes/<id>")
def get_note(id):
    notes = load_json("notes.json")
    note = _find_by_id(notes, id)
    if note is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(note)
