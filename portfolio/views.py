from typing import Any, Dict, List, Optional, Tuple

from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .data import AUTHOR, BLOG_POSTS, CASE_STUDIES, GITHUB_STATS, PERFORMANCE, PROJECTS, RESUME_URL, SKILLS
from .models import Message
from .services import AskAIService, PredictService


def _group_skills(skills: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    grouped = {}
    for skill in skills:
        grouped.setdefault(skill["category"], []).append(skill)
    return grouped


def _split_text(value: Optional[str]) -> List[str]:
    if not value:
        return []
    raw_parts = value.replace(",", "\n").splitlines()
    return [part.strip() for part in raw_parts if part.strip()]


def _get_projects() -> List[Dict[str, Any]]:
    return PROJECTS


def _get_case_studies() -> List[Dict[str, Any]]:
    return CASE_STUDIES


def _get_skills() -> List[Dict[str, str]]:
    return SKILLS


def _get_author_context() -> Tuple[None, Dict[str, Any], List[Dict[str, str]], Optional[str]]:
    return None, AUTHOR, SKILLS, None

def index(request: HttpRequest) -> HttpResponse:
    _, author_data, _, _ = _get_author_context()
    projects = _get_projects()
    featured_project = next((project for project in projects if project.get("is_featured")), None)
    featured_project = featured_project or (projects[0] if projects else None)
    skills = _get_skills()
    skill_groups = _group_skills(skills)
    context = {
       'author_data': author_data,
       'projects': projects,
       'featured_project': featured_project,
       'skills': skills,
       'skill_groups': skill_groups,
       'performance_metrics': PERFORMANCE,
       'blog_posts': BLOG_POSTS,
       'github_stats': GITHUB_STATS,
       'resume_url': RESUME_URL,
   }

    return render(request, 'index.html', context)


def about(request: HttpRequest) -> HttpResponse:
    author, author_data, skills, image_url = _get_author_context()

    context = {
        "author": author,
        "author_data": author_data,
        "skills": skills,
        "technologies": _group_skills(skills),
        "image_url": image_url,
        "resume_url": RESUME_URL,
    }
    return render(request, "about.html", context)


def projects(request: HttpRequest) -> HttpResponse:
    _, author_data, _, _ = _get_author_context()
    projects_list = _get_projects()
    featured_project = next(
        (project for project in projects_list if project.get("is_featured")),
        projects_list[0] if projects_list else None,
    )
    context = {
        "author_data": author_data,
        "projects": projects_list,
        "featured_project": featured_project,
        "performance_metrics": PERFORMANCE,
        "github_stats": GITHUB_STATS,
        "resume_url": RESUME_URL,
    }
    return render(request, "projects.html", context)


def case_studies(request: HttpRequest) -> HttpResponse:
    _, author_data, _, _ = _get_author_context()
    context = {
        "author_data": author_data,
        "case_studies": _get_case_studies(),
        "resume_url": RESUME_URL,
    }
    return render(request, "case_studies.html", context)


def skills(request: HttpRequest) -> HttpResponse:
    _, author_data, _, _ = _get_author_context()
    skills_list = _get_skills()
    context = {
        "author_data": author_data,
        "skills": skills_list,
        "skill_groups": _group_skills(skills_list),
        "resume_url": RESUME_URL,
    }
    return render(request, "skills.html", context)


def work_detail(request: HttpRequest, slug: str) -> HttpResponse:
    work = next((project for project in _get_projects() if project.get("slug") == slug), None)
    if work is None:
        return render(request, "work_detail.html", status=404)

    stack_items = work.get("stack", [])
    feature_items = work.get("features", [])
    architecture_items = work.get("architecture", [])
    result_items = work.get("results", [])
    summary_text = work.get("summary") or work.get("description", "")
    context = {
        'work': work,
        'stack_items': stack_items,
        'feature_items': feature_items,
        'architecture_items': architecture_items,
        'result_items': result_items,
        'summary_text': summary_text,
    }
    return render(request, 'work_detail.html', context)


def contact(request: HttpRequest) -> HttpResponse:
    _, author_data, _, _ = _get_author_context()
    if request.method == 'POST':
        msg = Message(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
         )
        msg.save()
        messages.success(request, 'Сообщение отправлено!')
        return redirect('contact')

    return render(
        request,
        "contact.html",
        {
            "author_data": author_data,
            "resume_url": RESUME_URL,
        },
    )


def api_projects(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"projects": _get_projects()})


def api_skills(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"skills": _get_skills()})


def api_case_studies(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"case_studies": _get_case_studies()})


def api_ask_ai(request: HttpRequest) -> JsonResponse:
    return JsonResponse(AskAIService.get_status_payload(), status=501)


def api_predict(request: HttpRequest) -> JsonResponse:
    return JsonResponse(PredictService.get_status_payload(), status=501)