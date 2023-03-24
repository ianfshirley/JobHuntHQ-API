from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    method_label = serializers.CharField(source='get_method_display', read_only=True)

    class Meta:
        model = Job
        
        # Get all field names from the model
        fields = [f.name for f in model._meta.get_fields()]

        # Add the method_label to the list of fields
        fields = fields + ['method_label']