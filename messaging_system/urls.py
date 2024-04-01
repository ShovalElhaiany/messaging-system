from django.urls import path
from .views import MessageListCreateAPIView, UnreadMessageListAPIView, MessageRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('messages/', MessageListCreateAPIView.as_view(), name='message-list-create'),
    path('unread-messages/', UnreadMessageListAPIView.as_view(), name='unread-message-list'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDestroyAPIView.as_view(), name='message-retrieve-update-destroy'),
]
