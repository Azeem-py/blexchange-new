import imp
from .views import UserViewSet
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

user_list = UserViewSet.as_view({
    'get': "list",
})
user_detail = UserViewSet.as_view({
    'get': "retrieve",
})

urlpatterns = format_suffix_patterns([
    path('list', user_list, name='user-list'),
    path('user/<int:pk>/', user_detail, name="user-details"),
])