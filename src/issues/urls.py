from django.urls import path
from .api import CreateMessageAPIView, ListIssueMessagesAPIView

urlpatterns = [
    path('<int:issue_id>/messages/', CreateMessageAPIView.as_view(), name='create_message'),
    path('<int:issue_id>/messages/', ListIssueMessagesAPIView.as_view(), name='issue_messages'),
]
