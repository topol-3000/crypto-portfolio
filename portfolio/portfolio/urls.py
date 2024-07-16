from django.urls import path

from portfolio.views.portfolio import PortfolioDetailView, PortfolioListCreateView
from portfolio.views.user import UserRegistrationView

urlpatterns = [
    path("registration", UserRegistrationView.as_view(), name="registration"),
    path("portfolios/<int:id>/", PortfolioDetailView.as_view(), name="portfolio"),
    path("portfolios", PortfolioListCreateView.as_view(), name="portfolios"),
]
