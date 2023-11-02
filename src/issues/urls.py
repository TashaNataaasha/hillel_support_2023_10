from django.urls import path
from . import views

urlpatterns = [
    path("create-issue/", views.create_issue, name="create_issue"),
    path("issues/", views.get_issues, name="get_issues"),
    path(
        "issues/<int:issue_id>/", views.get_issue_by_id, name="get_issue_by_id"
    ),
]
