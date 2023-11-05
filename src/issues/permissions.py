from rest_framework.permissions import BasePermission

class IsParticipant(BasePermission):
    def has_permission(self, request, view):
        issue_id = view.kwargs.get('issue_id')
        issue = get_object_or_404(Issue, id=issue_id)
        return issue.is_participant(request.user)
