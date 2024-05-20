from django.urls import path
from .views import RegisterAPIView, AuthAPIView

app_name = 'Users'

urlpatterns = [
    path('signup/', RegisterAPIView.as_view()),
    path('login/', AuthAPIView.as_view()),
]