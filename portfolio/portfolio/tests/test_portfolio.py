from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from portfolio.models import Portfolio
from portfolio.views.portfolio import PortfolioListCreateView


class PortfolioListCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("portfolios")

    def create_user(self):
        return get_user_model().objects.create_user(email="normal@user.com", password="foo", full_name="Normal User")

    def test_get_all_portfolios(self):
        user = self.create_user()
        self.client.force_authenticate(user=user)
        Portfolio.objects.create(title="Portfolio 1", user=user)
        Portfolio.objects.create(title="Portfolio 2", user=user)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_empty_portfolio_list(self):
        user = self.create_user()
        self.client.force_authenticate(user=user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_post_portfolio_with_authentication(self):
        self.client.force_authenticate(user=self.create_user())
        data = {"title": "New Portfolio"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Portfolio")

    def test_post_portfolio_without_authentication(self):
        data = {"title": "New Portfolio"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_queryset_returns_all_existing_portfolios(self):
        user = self.create_user()
        Portfolio.objects.create(title="Portfolio 1", user=user)
        Portfolio.objects.create(title="Portfolio 2", user=user)

        view = PortfolioListCreateView()
        view.request = self.client.get(self.url)
        queryset = view.get_queryset()
        self.assertEqual(queryset.count(), 2)


class PortfolioDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def create_user(self):
        return get_user_model().objects.create_user(email="normal@user.com", password="foo", full_name="Normal User")

    def test_get_portfolio_with_valid_id(self):
        user = self.create_user()
        portfolio = Portfolio.objects.create(title="Test Portfolio", user=user)
        self.client.force_authenticate(user=user)
        response = self.client.get(reverse("portfolio", kwargs={"id": portfolio.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Portfolio")

    def test_get_portfolio_with_invalid_id(self):
        self.client.force_authenticate(user=self.create_user())
        response = self.client.get(reverse("portfolio", kwargs={"id": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_portfolio_with_valid_id(self):
        user = self.create_user()
        portfolio = Portfolio.objects.create(title="Test Portfolio", user=user)
        self.client.force_authenticate(user=user)
        data = {"title": "Updated Portfolio"}
        response = self.client.put(reverse("portfolio", kwargs={"id": portfolio.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Portfolio")

    def test_update_portfolio_with_invalid_id(self):
        self.client.force_authenticate(user=self.create_user())
        data = {"title": "Updated Portfolio"}
        response = self.client.put(reverse("portfolio", kwargs={"id": 999}), data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_portfolio_with_valid_id(self):
        user = self.create_user()
        portfolio = Portfolio.objects.create(title="Test Portfolio", user=user)
        self.client.force_authenticate(user=user)
        response = self.client.delete(reverse("portfolio", kwargs={"id": portfolio.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Portfolio.objects.filter(id=portfolio.id).exists())
