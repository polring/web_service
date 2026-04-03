"""JSON 데이터 디렉터리 접근 — 블루프린트에서 공통 사용."""
import json
from pathlib import Path

_DATA_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = _DATA_ROOT / "data"

# 데이터 파일명 단일 정의 — 매직 문자열 분산(Primitive Obsession) 완화
PROFILE_JSON = "profile.json"
SKILLS_JSON = "skills.json"
PROJECTS_JSON = "projects.json"
CONTACT_JSON = "contact.json"
ABOUT_JSON = "about.json"
NOTES_JSON = "notes.json"


def load_json(filename: str):
    path = DATA_DIR / filename
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def find_item_by_id(items: list, item_id: str):
    for item in items:
        if str(item.get("id")) == str(item_id):
            return item
    return None
