from typing import Any, Dict, List, Optional, Tuple

from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Author, CaseStudy, Category, Item, Message, Service, Skill, Testimony, Work
from .services import AskAIService, PredictService

DEFAULT_AUTHOR = {
    "full_name": "Dauren Askarov",
    "name": "Dauren",
    "lastname": "Askarov",
    "title": "Python Backend Engineer | AI Integration",
    "location": "Almaty, Kazakhstan",
    "bio": (
        "AI-oriented Python Backend Engineer with experience building real-time "
        "backend systems, AI integrations and scalable APIs."
    ),
    "email": "dauren2050@yandex.ru",
    "telegram": "https://t.me/DK_Oscar",
    "github": "https://github.com/Oscardkyou",
    "focus_areas": [
        "AI systems",
        "data pipelines",
        "cloud backend infrastructure",
        "event-driven architecture",
    ],
}

DEFAULT_SKILLS = [
    {"name": "Python", "category": "Backend", "icon": "bx bxl-python"},
    {"name": "FastAPI", "category": "Backend", "icon": "bx bx-code-alt"},
    {"name": "Django", "category": "Backend", "icon": "bx bx-code-block"},
    {"name": "REST API", "category": "Backend", "icon": "bx bx-transfer"},
    {"name": "WebSockets", "category": "Backend", "icon": "bx bx-wifi"},
    {"name": "PostgreSQL", "category": "Databases", "icon": "bx bxs-data"},
    {"name": "Redis", "category": "Databases", "icon": "bx bxs-data"},
    {"name": "ChromaDB", "category": "Databases", "icon": "bx bx-layer"},
    {"name": "RAG", "category": "AI", "icon": "bx bx-brain"},
    {"name": "LLM integration", "category": "AI", "icon": "bx bx-bot"},
    {"name": "HuggingFace", "category": "AI", "icon": "bx bx-bot"},
    {"name": "OpenAI", "category": "AI", "icon": "bx bx-chip"},
    {"name": "Vector Search", "category": "AI", "icon": "bx bx-shape-circle"},
    {"name": "AWS", "category": "Cloud", "icon": "bx bxl-aws"},
    {"name": "S3", "category": "Cloud", "icon": "bx bx-cloud"},
    {"name": "Docker", "category": "Cloud", "icon": "bx bxl-docker"},
    {"name": "Nginx", "category": "Cloud", "icon": "bx bx-server"},
]

DEFAULT_PROJECTS = [
    {
        "title": "Gravora AI Knowledge Platform",
        "summary": "AI system for enterprise knowledge base using RAG.",
        "description": (
            "AI platform for internal knowledge base powered by Retrieval Augmented Generation architecture."
        ),
        "stack": [
            "Python",
            "FastAPI",
            "OpenAI",
            "HuggingFace",
            "Redis",
            "ChromaDB",
            "Docker",
            "Prometheus",
            "Grafana",
        ],
        "features": [
            "RAG pipeline",
            "OpenAI embeddings",
            "ChromaDB vector search",
            "LLM response generation",
            "Redis caching",
            "Telegram bot integration",
        ],
        "architecture": [
            "User",
            "FastAPI API",
            "RAG Service",
            "Vector DB (ChromaDB)",
            "LLM Provider",
        ],
        "results": ["Reduced search time from 15 minutes to 30 seconds."],
        "github_url": "https://github.com/Oscardkyou",
        "link": "",
        "is_featured": True,
    },
    {
        "title": "Low Latency Video Streaming Backend",
        "summary": "Real-time backend system for streaming video from mobile to desktop.",
        "description": "Async backend for low-latency mobile video streaming.",
        "stack": [
            "Python",
            "FastAPI",
            "WebSockets",
            "FFmpeg",
            "Redis",
            "PostgreSQL",
            "S3",
            "Docker",
            "Nginx",
        ],
        "features": [
            "Async architecture",
            "WebSocket streaming",
            "Redis state management",
            "S3 storage",
            "Docker deployment",
        ],
        "architecture": [
            "Mobile Clients",
            "WebSocket Gateway",
            "Streaming Orchestrator",
            "Redis State",
            "S3 Storage",
        ],
        "results": ["Latency under 150ms", "Supports 50+ concurrent streams"],
        "github_url": "https://github.com/Oscardkyou",
        "link": "",
        "is_featured": False,
    },
    {
        "title": "Blockchain Monitoring System",
        "summary": "Backend service for real-time blockchain transaction monitoring.",
        "description": "Event-driven monitoring of blockchain transactions and alerts.",
        "stack": ["Python", "Web3", "Celery", "Redis", "PostgreSQL"],
        "features": [
            "WebSocket blockchain events",
            "RPC integration",
            "transaction monitoring",
            "event processing",
        ],
        "architecture": [
            "Blockchain Node",
            "Web3 Event Listener",
            "Celery Workers",
            "PostgreSQL",
            "Alerting",
        ],
        "results": ["Near real-time monitoring", "Reliable event processing"],
        "github_url": "https://github.com/Oscardkyou",
        "link": "",
        "is_featured": False,
    },
]

DEFAULT_PERFORMANCE = [
    {"metric": "RAG latency", "value": "< 180ms"},
    {"metric": "Streaming latency", "value": "< 150ms"},
    {"metric": "Concurrent streams", "value": "50+ clients"},
    {"metric": "AI cost reduction", "value": "35%"},
]

DEFAULT_BLOG = [
    {"title": "AI Architecture for RAG Systems", "tag": "AI Systems"},
    {"title": "Designing Async FastAPI Services", "tag": "Backend"},
    {"title": "Production LLM Integrations", "tag": "AI Integration"},
]

DEFAULT_GITHUB = {
    "stats": "https://github-readme-stats.vercel.app/api?username=Oscardkyou&show_icons=true&theme=tokyonight",
    "activity": "https://github-readme-activity-graph.vercel.app/graph?username=Oscardkyou&theme=tokyo-night",
}

DEFAULT_CASE_STUDIES = [
    {
        "title": "Gravora RAG Case Study",
        "slug": "gravora-rag-case-study",
        "problem": "Enterprise knowledge was fragmented across documents and chats.",
        "solution": "Built a FastAPI-based RAG pipeline with retrieval, caching, and LLM orchestration.",
        "stack": ["Python", "FastAPI", "OpenAI", "ChromaDB", "Redis"],
        "metrics": ["Latency < 180ms", "Search time reduced by 35%"],
        "architecture": ["User", "FastAPI API", "Retriever", "Vector DB", "LLM Provider"],
        "github_link": "https://github.com/Oscardkyou",
        "demo_link": "",
        "featured": True,
    }
]


def _normalize_skills(skills: List[Skill]) -> List[Dict[str, str]]:
    normalized = []
    for skill in skills:
        normalized.append(
            {
                "name": skill.name,
                "category": skill.category or "Skills",
                "icon": skill.icon or "bx bx-chip",
            }
        )
    return normalized


def _normalize_case_study(case_study: CaseStudy) -> Dict[str, Any]:
    return {
        "title": case_study.title,
        "slug": case_study.slug,
        "problem": case_study.problem,
        "solution": case_study.solution,
        "stack": _split_text(case_study.stack),
        "metrics": _split_text(case_study.metrics),
        "architecture": _split_text(case_study.architecture),
        "github_link": case_study.github_link,
        "demo_link": case_study.demo_link,
        "featured": case_study.featured,
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


def _normalize_work(work: Work) -> Dict[str, Any]:
    return {
        "title": work.title,
        "summary": work.summary or work.description[:160],
        "description": work.description,
        "stack": _split_text(work.stack),
        "features": _split_text(work.features),
        "architecture": _split_text(work.architecture),
        "results": _split_text(work.results),
        "github_url": work.github_url,
        "link": work.link,
        "image_url": work.image.url if work.image else "",
        "slug": work.slug,
        "is_featured": work.is_featured,
    }


def _get_projects() -> List[Dict[str, Any]]:
    works = list(Work.objects.all())
    if works:
        return [_normalize_work(work) for work in works]
    return DEFAULT_PROJECTS


def _get_case_studies() -> List[Dict[str, Any]]:
    case_studies = list(CaseStudy.objects.all())
    if case_studies:
        return [_normalize_case_study(case_study) for case_study in case_studies]
    return DEFAULT_CASE_STUDIES


def _get_skills() -> List[Dict[str, str]]:
    skills_qs = Skill.objects.all()
    if skills_qs.exists():
        return _normalize_skills(skills_qs)
    return DEFAULT_SKILLS


def _get_author_context() -> Tuple[Optional[Author], Dict[str, Any], List[Dict[str, str]], Optional[str]]:
    author = Author.objects.prefetch_related("skills").first()

    if author:
        skills = _normalize_skills(author.skills.all())
        author_data = {
            "full_name": f"{author.name} {author.lastname}",
            "name": author.name,
            "lastname": author.lastname,
            "title": author.title or DEFAULT_AUTHOR["title"],
            "location": author.location or DEFAULT_AUTHOR["location"],
            "bio": author.about or DEFAULT_AUTHOR["bio"],
            "email": author.email or DEFAULT_AUTHOR["email"],
            "telegram": author.telegram or DEFAULT_AUTHOR["telegram"],
            "github": author.github or DEFAULT_AUTHOR["github"],
            "focus_areas": author.focus_areas.split("\n") if author.focus_areas else DEFAULT_AUTHOR["focus_areas"],
        }
        image_url = author.image.url if author.image else None
    else:
        skills = DEFAULT_SKILLS
        author_data = DEFAULT_AUTHOR
        image_url = None

    return author, author_data, skills, image_url

def index(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    projects = _get_projects()
    featured_project = next((project for project in projects if project.get("is_featured")), None)
    featured_project = featured_project or (projects[0] if projects else None)
    skills = _get_skills()
    skill_groups = _group_skills(skills)
    services = Service.objects.all()
    testimonies = Testimony.objects.all()


    #for work in works:
    #    print(work.category)


    context = {
       'categories': categories,
       'works': Work.objects.all(),
       'services': services,
       'testimonies': testimonies,
       'projects': projects,
       'featured_project': featured_project,
       'skills': skills,
       'skill_groups': skill_groups,
       'performance_metrics': DEFAULT_PERFORMANCE,
       'blog_posts': DEFAULT_BLOG,
       'github_stats': DEFAULT_GITHUB,
       'resume_url': '/static/assets/dauren-askarov-resume.pdf',
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
        "resume_url": "/static/assets/dauren-askarov-resume.pdf",
    }
    return render(request, "about.html", context)


def projects(request: HttpRequest) -> HttpResponse:
    projects_list = _get_projects()
    featured_project = next(
        (project for project in projects_list if project.get("is_featured")),
        projects_list[0] if projects_list else None,
    )
    context = {
        "projects": projects_list,
        "featured_project": featured_project,
        "performance_metrics": DEFAULT_PERFORMANCE,
        "github_stats": DEFAULT_GITHUB,
        "resume_url": "/static/assets/dauren-askarov-resume.pdf",
    }
    return render(request, "projects.html", context)


def skills(request: HttpRequest) -> HttpResponse:
    skills_list = _get_skills()
    context = {
        "skills": skills_list,
        "skill_groups": _group_skills(skills_list),
        "resume_url": "/static/assets/dauren-askarov-resume.pdf",
    }
    return render(request, "skills.html", context)


def work_detail(request: HttpRequest, slug: str) -> HttpResponse:
    work = get_object_or_404(Work, slug=slug)
    testimonies = Testimony.objects.all()
    stack_items = _split_text(work.stack)
    feature_items = _split_text(work.features)
    architecture_items = _split_text(work.architecture)
    result_items = _split_text(work.results)
    summary_text = work.summary or work.description
    context = {
        'work': work,
        'testimonies': testimonies,
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
            "resume_url": "/static/assets/dauren-askarov-resume.pdf",
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