import hashlib

from livekit.settings import plugin_settings as settings


def generate_room_code(source_user, target_user):
    combined = "-".join(sorted([source_user, target_user]))
    hash_object = hashlib.sha256(combined.encode("utf-8"))
    hash_hex = hash_object.hexdigest()
    return settings.LIVEKIT_ROOM_NAME_PREFIX + hash_hex
