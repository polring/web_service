from flask import Blueprint, render_template

from services.json_store import (
    ABOUT_JSON,
    CONTACT_JSON,
    PROFILE_JSON,
    PROJECTS_JSON,
    SKILLS_JSON,
    load_json,
)

bp = Blueprint("main", __name__)


@bp.get("/")
def home():
    profile = load_json(PROFILE_JSON)
    return render_template(
        "home.html",
        title=f"안녕하세요, 저는 {profile['name']}입니다.",
        lead=profile["headline"],
        intro=profile["intro"],
        principles=profile["principles"],
    )


@bp.get("/skills")
def skills():
    skills_data = load_json(SKILLS_JSON)
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
    projects_data = load_json(PROJECTS_JSON)
    return render_template(
        "projects.html",
        title="미니 프로젝트 아카이브",
        lead="간단한 아이디어를 빠르게 구현하고, 기록으로 남기는 것을 목표로 합니다.",
        projects=projects_data,
    )


@bp.get("/contact")
def contact():
    contact_data = load_json(CONTACT_JSON)
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
    about_data = load_json(ABOUT_JSON)
    return render_template(
        "about.html",
        title="소개",
        lead="저를 조금 더 알아가실 수 있는 페이지입니다.",
        bio=about_data["bio"],
        highlights=about_data["highlights"],
    )
