from rest_framework import serializers


class JSONFieldSerializer(serializers.Serializer):
    """Serializer for core"""
    data = serializers.JSONField()
