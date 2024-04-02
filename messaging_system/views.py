from django.db.models import Q
from rest_framework import generics, permissions, authentication, status
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer


# View for listing and creating messages
class MessageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requires authentication
    authentication_classes = [authentication.TokenAuthentication]  # Authenticates using token

    def get_queryset(self):
        # Get the current user
        user = self.request.user
        # Filter messages where the current user is either the sender or the receiver
        return Message.objects.filter(Q(sender=user) | Q(receiver=user))

    def perform_create(self, serializer):
        # Set the sender of the message as the current user before saving
        serializer.save(sender=self.request.user)


# View for listing unread messages
class UnreadMessageListAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        # Filter unread messages for the current user
        return Message.objects.filter(receiver=user, is_read=False)


# View for retrieving, updating, and deleting a single message
class MessageRetrieveUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        # Get the message id from the URL
        message_id = self.kwargs['pk']
        # Update the 'is_read' field of the message to True
        Message.objects.filter(pk=message_id, receiver=user).update(is_read=True)
        # Return filtered queryset of messages for the current user
        return Message.objects.filter(receiver=user)

    def destroy(self, request, *args, **kwargs):
        # Get the message instance
        instance = self.get_object()
        # Check if the current user is the sender or the receiver of the message
        if request.user == instance.sender or request.user == instance.receiver:
            # If so, perform the deletion
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)  # Return success response
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)  # Return forbidden response if not authorized
        