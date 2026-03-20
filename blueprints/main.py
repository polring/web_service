from flask import Blueprint, render_template
import json
from pathlib import Path

bp = Blueprint("main", __name__)
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"


def load_json(filename: str):
    path = DATA_DIR / filename
    with path.open(encoding="utf-8") as file:
        return json.load(file)


@bp.get("/")
def home():
    profile = load_json("profile.json")
    return render_template(
        "home.html",
        title=f"안녕하세요, 저는 {profile['name']}입니다.",
        lead=profile["headline"],
        intro=profile["intro"],
        principles=profile["principles"],
    )


@bp.get("/skills")
def skills():
    skills_data = load_json("skills.json")
    return render_template(
        "skills.html",
        title="기술 스택과 관심 분야",
        lead="현재 집중하는 기술과 앞으로 확장하고 싶은 영역을 정리했습니다.",
        focus=skills_data["focus"],
        items=skills_data["items"],
        interests=skills_data["interests"],
    )


@bp.get("/projects")
def projects():
    projects_data = load_json("projects.json")
    return render_template(
        "projects.html",
        title="미니 프로젝트 아카이브",
        lead="간단한 아이디어를 빠르게 구현하고, 기록으로 남기는 것을 목표로 합니다.",
        projects=projects_data,
    )


@bp.get("/contact")
def contact():
    contact_data = load_json("contact.json")
    return render_template(
        "contact.html",
        title="연락 및 목표",
        lead="공유하고 싶은 아이디어가 있다면 언제든 이야기 나누고 싶습니다.",
        email=contact_data["email"],
        github=contact_data["github"],
        goal=contact_data["goal"],
    )


@bp.get("/about")
def about():
    pass
