from copy import deepcopy
from typing import Any, Dict, List, Optional, Tuple

from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .data import AUTHOR, BLOG_POSTS, CASE_STUDIES, GITHUB_STATS, PERFORMANCE, PROJECTS, RESUME_URL, SKILLS
from .models import Message
from .services import AskAIService, PredictService


SUPPORTED_LANGUAGES = ("en", "kz")


def _get_language(request: HttpRequest) -> str:
    lang = request.GET.get("lang") or request.COOKIES.get("site_lang") or "en"
    if lang not in SUPPORTED_LANGUAGES:
        return "en"
    return lang


def _select_localized_value(value: Any, lang: str) -> Any:
    if isinstance(value, dict):
        if all(key in SUPPORTED_LANGUAGES for key in value.keys()):
            return value.get(lang) or value.get("en") or next(iter(value.values()), "")
        return {key: _select_localized_value(item, lang) for key, item in value.items()}
    if isinstance(value, list):
        return [_select_localized_value(item, lang) for item in value]
    return value


def _localized_copy(payload: Any, lang: str) -> Any:
    return _select_localized_value(deepcopy(payload), lang)


def _build_shared_context(request: HttpRequest) -> Dict[str, Any]:
    lang = _get_language(request)
    return {
        "lang": lang,
        "supported_languages": SUPPORTED_LANGUAGES,
        "resume_url": RESUME_URL,
    }


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


def _get_author_context(request: HttpRequest) -> Tuple[None, Dict[str, Any], List[Dict[str, str]], Optional[str]]:
    lang = _get_language(request)
    return None, _localized_copy(AUTHOR, lang), _localized_copy(SKILLS, lang), None

def index(request: HttpRequest) -> HttpResponse:
    _, author_data, _, _ = _get_author_context(request)
    lang = _get_language(request)
    projects = _localized_copy(_get_projects(), lang)
    featured_project = next((project for project in projects if project.get("is_featured")), None)
    featured_project = featured_project or (projects[0] if projects else None)
    skills = _localized_copy(_get_skills(), lang)
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
       **_build_shared_context(request),
   }

    response = render(request, 'index.html', context)
    response.set_cookie("site_lang", _get_language(request), max_age=60 * 60 * 24 * 365)
    return response


def about(request: HttpRequest) -> HttpResponse:
    author, author_data, skills, image_url = _get_author_context(request)

    context = {
        "author": author,
        "author_data": author_data,
        "skills": skills,
        "technologies": _group_skills(skills),
        "image_url": image_url,
        **_build_shared_context(request),
    }
    response = render(request, "about.html", context)
    response.set_cookie("site_lang", _get_language(request), max_age=60 * 60 * 24 * 365)
    return response


def projects(request: HttpRequest) -> HttpResponse:
    _, author_data, _, _ = _get_author_context(request)
    lang = _get_language(request)
    projects_list = _localized_copy(_get_projects(), lang)
    featured_project = next(
        (project for project in projects_list if project.get("is_featured")),
        projects_list[0] if projects_list else None,
    )
    context = {
        "author_data": author_data,
        "projects": projects_list,
        "featured_project": featured_project,
        "performance_metrics": _localized_copy(PERFORMANCE, lang),
        "github_stats": _localized_copy(GITHUB_STATS, lang),
        **_build_shared_context(request),
    }
    response = render(request, "projects.html", context)
    response.set_cookie("site_lang", _get_language(request), max_age=60 * 60 * 24 * 365)
    return response


def case_studies(request: HttpRequest) -> HttpResponse:
    _, author_data, _, _ = _get_author_context(request)
    lang = _get_language(request)
    context = {
        "author_data": author_data,
        "case_studies": _localized_copy(_get_case_studies(), lang),
        **_build_shared_context(request),
    }
    response = render(request, "case_studies.html", context)
    response.set_cookie("site_lang", _get_language(request), max_age=60 * 60 * 24 * 365)
    return response


def skills(request: HttpRequest) -> HttpResponse:
    _, author_data, _, _ = _get_author_context(request)
    lang = _get_language(request)
    skills_list = _localized_copy(_get_skills(), lang)
    context = {
        "author_data": author_data,
        "skills": skills_list,
        "skill_groups": _group_skills(skills_list),
        **_build_shared_context(request),
    }
    response = render(request, "skills.html", context)
    response.set_cookie("site_lang", _get_language(request), max_age=60 * 60 * 24 * 365)
    return response


def work_detail(request: HttpRequest, slug: str) -> HttpResponse:
    lang = _get_language(request)
    work = next((project for project in _localized_copy(_get_projects(), lang) if project.get("slug") == slug), None)
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
        **_build_shared_context(request),
    }
    response = render(request, 'work_detail.html', context)
    response.set_cookie("site_lang", _get_language(request), max_age=60 * 60 * 24 * 365)
    return response


def contact(request: HttpRequest) -> HttpResponse:
    _, author_data, _, _ = _get_author_context(request)
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
            **_build_shared_context(request),
        },
    )


def api_projects(request: HttpRequest) -> JsonResponse:
    lang = _get_language(request)
    return JsonResponse({"lang": lang, "projects": _localized_copy(_get_projects(), lang)})


def api_skills(request: HttpRequest) -> JsonResponse:
    lang = _get_language(request)
    return JsonResponse({"lang": lang, "skills": _localized_copy(_get_skills(), lang)})


def api_case_studies(request: HttpRequest) -> JsonResponse:
    lang = _get_language(request)
    return JsonResponse({"lang": lang, "case_studies": _localized_copy(_get_case_studies(), lang)})


def api_ask_ai(request: HttpRequest) -> JsonResponse:
    return JsonResponse(AskAIService.get_status_payload(), status=501)


def api_predict(request: HttpRequest) -> JsonResponse:
    return JsonResponse(PredictService.get_status_payload(), status=501)