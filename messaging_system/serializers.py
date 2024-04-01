from rest_framework import serializers
from .models import Message


# Serializer for the Message model
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message  # Specifies the model to be serialized
        fields = "__all__"  # Includes all fields of the model in the serialization
