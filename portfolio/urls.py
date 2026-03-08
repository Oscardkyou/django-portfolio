from django.urls import path

from .views import (
    about,
    api_ask_ai,
    api_case_studies,
    api_predict,
    api_projects,
    api_skills,
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
    path('skills/', skills, name='skills'),
    path('work/<slug:slug>/', work_detail, name='work_detail'),
    path('contact/', contact, name='contact'),
    path('api/projects/', api_projects, name='api_projects'),
    path('api/skills/', api_skills, name='api_skills'),
    path('api/case-studies/', api_case_studies, name='api_case_studies'),
    path('api/ask-ai/', api_ask_ai, name='api_ask_ai'),
    path('api/predict/', api_predict, name='api_predict'),
]