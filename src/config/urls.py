from django.urls import path
from users import api

urlpatterns = [
    path('users/all', api, name='all_users'),
    path('users/create',api, name='create_user'),
    path('issues/all', api, name='all_issues'),
    path('issues/create', api, name='create_issue'),
]