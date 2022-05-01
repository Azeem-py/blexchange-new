from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name="sign up"),
    path('login/', views.login, name="login"),
    path('addlink/', views.add_link, name="link"),
]
