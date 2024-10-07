from rest_framework import serializers


class CreateRoomSerializer(serializers.Serializer):
    source = serializers.CharField(max_length=50, required=True)
    target = serializers.CharField(max_length=50, required=True)
