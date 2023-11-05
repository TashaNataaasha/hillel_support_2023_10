from django.urls import path
from .views import create_message, get_messages

urlpatterns = [
    path('issues/<int:issue_id>/messages/', create_message),
    path('issues/<int:issue_id>/messages/', get_messages),
]