from django.urls import path

from .views import (
    about,
    api_ai_chat,
    api_ai_experiments,
    api_ai_predict,
    api_case_studies,
    api_projects,
    api_skills,
    case_studies,
    contact,
    index,
    projects,
    skills,
    work_detail,
)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('case-studies/', case_studies, name='case_studies'),
    path('skills/', skills, name='skills'),
    path('work/<slug:slug>/', work_detail, name='work_detail'),
    path('contact/', contact, name='contact'),
    path('api/projects/', api_projects, name='api_projects'),
    path('api/skills/', api_skills, name='api_skills'),
    path('api/case-studies/', api_case_studies, name='api_case_studies'),
    path('api/ai/chat/', api_ai_chat, name='api_ai_chat'),
    path('api/ai/experiments/', api_ai_experiments, name='api_ai_experiments'),
    path('api/ai/predict/', api_ai_predict, name='api_ai_predict'),
]