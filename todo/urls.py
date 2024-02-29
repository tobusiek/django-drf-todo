from django.urls import include, path
from rest_framework.routers import DefaultRouter

from todo import views

router = DefaultRouter()
router.register(r"tasks", views.TasksListView, basename="tasks")

urlpatterns = [
    path("", include(router.urls)),
    path("tasks/<slug:slug>", views.TaskDetailView.as_view()),
]
