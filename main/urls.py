from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.PortfolioLoginView.as_view(), name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.PortfolioLogoutView.as_view(), name="logout"),
]
