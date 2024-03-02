from rest_framework import serializers

from todo import models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = "__all__"
        read_only_fields = ("slug",)
        depth = 1
