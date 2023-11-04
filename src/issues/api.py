from rest_framework import permissions

class IsParticipantOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.is_staff:
            return True
        
        # Check if the user is a participant in the issue
        return request.user in obj.issue.participants.all()

from rest_framework import generics

class IssueMessagesView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsParticipantOrAdmin]

    def get_queryset(self):
        issue_id = self.kwargs['issue_id']
        return Message.objects.filter(issue_id=issue_id)

    def perform_create(self, serializer):
        issue_id = self.kwargs['issue_id']
        serializer.save(issue_id=issue_id)