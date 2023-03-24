from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    method_label = serializers.CharField(source='get_method_display', read_only=True)

    class Meta:
        model = Job
        fields = "__all__"

        # Add the method_label to the list of fields
        fields = list(fields) + ['method_label']