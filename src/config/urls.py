from django.contrib import admin
from django.urls import path
from .exchange_rates import exchange_rates
from users import api


urlpatterns = [
    path("exchange-rates/", exchange_rates),
    path("users/all", api.users_all, name="all_users"),
    path("users/create", api.users_create, name="create_user"),
    path("issues/all", api.issues_all, name="all_issues"),
    path("issues/create", api.issues_create, name="create_issue"),
]