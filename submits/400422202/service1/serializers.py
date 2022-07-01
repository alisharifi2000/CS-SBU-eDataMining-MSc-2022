from rest_framework import serializers

class Service1Serializer(serializers.Serializer):
    data = serializers.DictField()
    config = serializers.DictField()