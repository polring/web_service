"""JSON API - 외부에서 데이터 조회"""
from flask import Blueprint, jsonify

from services.json_store import (
    NOTES_JSON,
    PROFILE_JSON,
    PROJECTS_JSON,
    find_item_by_id,
    load_json,
)

bp = Blueprint("api", __name__, url_prefix="/api")


def _json_list_item_or_404(filename: str, item_id: str):
    items = load_json(filename)
    item = find_item_by_id(items, item_id)
    if item is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(item)


@bp.get("/profile")
def get_profile():
    profile = load_json(PROFILE_JSON)
    return jsonify(profile)


@bp.get("/projects")
def get_projects():
    projects = load_json(PROJECTS_JSON)
    return jsonify(projects)


@bp.get("/projects/<item_id>")
def get_project(item_id):
    return _json_list_item_or_404(PROJECTS_JSON, item_id)


@bp.get("/notes")
def get_notes():
    notes = load_json(NOTES_JSON)
    return jsonify(notes)


@bp.get("/notes/<item_id>")
def get_note(item_id):
    return _json_list_item_or_404(NOTES_JSON, item_id)
