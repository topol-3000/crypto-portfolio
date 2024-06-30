from django.urls import path

from portfolio.views.user import UserRegistrationView

urlpatterns = [
    path("registration", UserRegistrationView.as_view(), name="registration"),
]
