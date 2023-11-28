from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    surname = serializers.CharField(max_length=255)