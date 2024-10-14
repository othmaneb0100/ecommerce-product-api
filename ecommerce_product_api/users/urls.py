from django.urls import path
from .views import CreateUserView, CustomObtainAuthToken

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='create_user'),
    path('token/', CustomObtainAuthToken.as_view(), name='token_obtain'),
]