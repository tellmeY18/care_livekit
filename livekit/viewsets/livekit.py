from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from livekit.api import AccessToken, VideoGrants
from livekit.models.call import Call
from livekit.serializers.livekit import CreateRoomSerializer
from livekit.settings import plugin_settings as settings
from livekit.util import generate_room_code


class LivekitViewset(
    GenericViewSet,
):
    permission_classes = [IsAuthenticated]

    serializer_action_classes = {
        "create_room": CreateRoomSerializer,
    }

    def get_serializer_class(self):
        if self.action in self.serializer_action_classes:
            return self.serializer_action_classes[self.action]

        return super().get_serializer_class()

    def validate_request(self, request):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        return serializer.validated_data

    @action(detail=False, methods=["POST"], url_path="create_room")
    def create_room(self, request):
        data = self.validate_request(request)

        source_username = data.get("source")
        target_username = data.get("target")

        room_code = generate_room_code(source_username, target_username)

        grant = VideoGrants(room_join=True, room=room_code)
        access_token = (
            AccessToken(
                api_key=settings.LIVEKIT_API_KEY,
                api_secret=settings.LIVEKIT_API_SECRET,
            )
            .with_identity(source_username)
            .with_name(source_username)
            .with_grants(grant)
            .to_jwt()
        )

        response = {
            "room_code": room_code,
            "access": str(access_token),
            "url": settings.LIVEKIT_API_URL,
        }

        Call.objects.create(room_code=room_code, access_token=str(access_token))

        return Response(response, status=status.HTTP_201_CREATED)
