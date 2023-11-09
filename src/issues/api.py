from rest_framework import generics
from .models import Message
from .permissions import RoleIsSenior, RoleIsJunior, RoleIsAdmin, IssueParticipant
from .serializers import MessageSerializer

class CreateMessageAPIView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [RoleIsSenior | RoleIsJunior | RoleIsAdmin & IssueParticipant]

    def perform_create(self, serializer):
        issue_id = self.kwargs.get('issue_id')
        serializer.save(author=self.request.user, issue_id=issue_id)

class ListIssueMessagesAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [RoleIsSenior | RoleIsJunior | RoleIsAdmin & IssueParticipant]

    def get_queryset(self):
        issue_id = self.kwargs.get('issue_id')
        return Message.objects.filter(issue_id=issue_id)
