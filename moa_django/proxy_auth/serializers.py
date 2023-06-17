from rest_framework import serializers

class NaverAccessSerializer(serializers.Serializer):
    client_id = serializers.CharField(max_length=255)
    redirect_uri = serializers.CharField(max_length=255)
    response_type = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)


class NaverTokenSerialzer(serializers.Serializer):
    client_id = serializers.CharField(max_length=255)
    client_secret = serializers.CharField(max_length=255)
    grant_type = serializers.CharField(max_length=255)
    code = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)