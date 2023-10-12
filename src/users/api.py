import json
from django.http import JsonResponse
from .models import User, Issue, Role
from django.db import models

def users_all(request):
    users = User.objects.all()
    user_data = [{"id": user.id, "email": user.email, "first_name": user.first_name, "last_name": user.last_name, "role": user.role.value} for user in users]
    return JsonResponse({"result": user_data})

# @csrf_exempt
def users_create(request):
    if request.method != "POST":
        raise NotImplementedError("Only POST requests")

    data = json.loads(request.body)
    role_value = data.get("role")
    role, created = Role.objects.get_or_create(value=role_value)
    data["role"] = role
    user = User.objects.create(**data)

    if not user:
        raise Exception("Cannot create user")

    user_data = {"id": user.id, "email": user.email, "first_name": user.first_name, "last_name": user.last_name, "role": user.role.value}
    return JsonResponse(user_data)

def issues_all(request):
    issues = Issue.objects.all()
    issue_data = [{"id": issue.id, "title": issue.title, "body": issue.body, "timestamp": issue.timestamp, "junior_id": issue.junior_id, "senior_id": issue.senior_id, "status": issue.status} for issue in issues]
    return JsonResponse({"result": issue_data})

# @csrf_exempt
def issues_create(request):
    if request.method != "POST":
        raise NotImplementedError("Only POST requests")

    data = json.loads(request.body)
    issue = Issue.objects.create(**data)

    if not issue:
        raise Exception("Cannot create issue")

    issue_data = {"id": issue.id, "title": issue.title, "body": issue.body, "timestamp": issue.timestamp, "junior_id": issue.junior_id, "senior_id": issue.senior_id, "status": issue.status}
    return JsonResponse(issue_data)