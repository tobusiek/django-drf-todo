from django.http import Http404
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.renderers import (
    BrowsableAPIRenderer,
    JSONRenderer,
    TemplateHTMLRenderer,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from todo.models import Task
from todo.serializers import TaskSerializer

# Create your views here.


class TasksListView(ReadOnlyModelViewSet):
    template_name = "todo/all_tasks.html"
    queryset = Task.objects.all().order_by("due_to")
    serializer_class = TaskSerializer
    renderer_classes = (
        BrowsableAPIRenderer,
        JSONRenderer,
        TemplateHTMLRenderer,
    )

    def get(self, request: Request, *args, **kwargs) -> Response:
        self.object = self.get_object()
        return Response({"tasks": self.object}, template_name=self.template_name)


class TaskDetailView(CreateAPIView, RetrieveUpdateAPIView):
    template_name = "todo/task_details.html"
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "slug"
    renderer_classes = (
        BrowsableAPIRenderer,
        JSONRenderer,
        TemplateHTMLRenderer,
    )

    def get_object(self, slug: str) -> Task:
        try:
            return self.queryset.get(slug=slug)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request: Request, slug: str, *args, **kwargs) -> Response:
        task = self.get_object(slug)
        serializer = self.serializer_class(task)
        return Response(serializer.data)

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, slug: str, *args, **kwargs) -> Response:
        task = self.get_object(slug)
        serializer = self.serializer_class(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
