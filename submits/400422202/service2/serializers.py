from rest_framework import serializers


class Service2Serializer(serializers.Serializer):
    data = serializers.DictField()
    config = serializers.DictField()
