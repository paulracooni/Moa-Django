from django.shortcuts import redirect

import uuid
import requests
from urllib import parse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, renderers

from proxy_auth import serializers, authentications

class NaverAccess(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    serializer = serializers.NaverAccessSerializer

    def get(self, request, format=None):

        serializer = self.serializer(data=request.query_params)

        serializer.is_valid(raise_exception=True)

        url="https://nid.naver.com/oauth2.0/authorize"
        query_params = parse.urlencode(serializer.data)
        print(f"{url}?{query_params}")
        return redirect(f"{url}?{query_params}")


class NaverToken(APIView):
    permission_classes = ()
    authentication_classes = []
    serializer = serializers.NaverTokenSerialzer

    def get(self, request, format=None):
        
        # Serialize data
        serializer = self.serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        
        # Request Token
        token = requests.get(
            url     = "https://nid.naver.com/oauth2.0/token",
            params  = serializer.data,
            headers = {
            'Access-Control-Allow-Origin': '*',
            'content-type'               : 'application/json'
          }
        ).json()

        # Request user information
        info = requests.get(
            url     = "https://openapi.naver.com/v1/nid/me",
            headers = {
            'Access-Control-Allow-Origin': '*',
            'content-type'               : 'application/json',
            'Authorization'              : f"Bearer {token['access_token']}"
          }
        ).json()
        
        # Merge all datas
        token.update(info['response'])

        return Response(
            data=token,
            headers={
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, PUT, DELETE, HEAD',
                'Access-Control-Allow-Headers': 'custId, appId, Origin, Content-Type, Cookie, X-CSRF-TOKEN, Accept, Authorization, X-XSRF-TOKEN, Access-Control-Allow-Origin',
                'Access-Control-Max-Age': '3600',
                'content-type': 'application/json'
          },
          exception=True
        )
