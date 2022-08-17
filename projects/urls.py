from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project-object/<str:pk>/', views.project, name="project"),
    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>', views.updateProject, name="update-project"),
    path('tag/<slug:tag_slug>', views.projects_by_tag, name="tag"),
]