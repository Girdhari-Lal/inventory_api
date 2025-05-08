from django.urls import path
from users.views import UserRegisterView, UserLoginView, UserProfileView
urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('user/', UserProfileView.as_view()),
]