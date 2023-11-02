from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Issue

# Creating an issue
def create_issue(request):
    if request.method == 'POST':
        # Logic to create an issue
        # Retrieve data from request and save it in the database
        # ...

# Getting a list of issues
def get_issues(request):
    if request.method == 'GET':
        issues = Issue.objects.values('id', 'title', 'body', 'status')
        return JsonResponse(list(issues), safe=False)

# Retrieving a single issue by ID
def get_issue_by_id(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    return JsonResponse({
        'id': issue.id,
        'title': issue.title,
        'body': issue.body,
        'status': issue.status,
        
    })