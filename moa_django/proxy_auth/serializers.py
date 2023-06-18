from rest_framework import serializers

class NaverTokenSerialzer(serializers.Serializer):
    client_id = serializers.CharField(max_length=255)
    client_secret = serializers.CharField(max_length=255)
    grant_type = serializers.CharField(max_length=255)
    code = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)