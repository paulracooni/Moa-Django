from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from proxy_auth import views

urlpatterns = format_suffix_patterns([
    path('naver_access', views.NaverAccess.as_view()),
    path('naver_token', views.NaverToken.as_view()),
])