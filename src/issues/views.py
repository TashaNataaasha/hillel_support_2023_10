from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Message
from .permissions import IsParticipant

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsParticipant])
def create_message(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    content = request.data.get('content')
    message = Message.objects.create(issue=issue, content=content)
    return Response({'message_id': message.id})

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsParticipant | IsAdminUser])
def get_messages(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    messages = Message.objects.filter(issue=issue)
    data = [{'id': message.id, 'content': message.content, 'created_at': message.created_at} for message in messages]
    return Response(data)