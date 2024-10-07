from django.db import models

from care.utils.models.base import BaseModel


class Call(BaseModel):
    room_code = models.CharField(null=True, blank=True)
    access_token = models.CharField(null=True, blank=True)
