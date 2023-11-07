import uuid

from django.db import models


class BaseModelInformations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PhoneType(BaseModelInformations):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.id

class Contact(BaseModelInformations):
    class Status(models.TextChoices):
        ACTIVE = 'Ativo'
        INACTIVE = 'Inativo'

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=100)
    status = models.CharField(Status.choices, default=Status.ACTIVE, max_length=20)
    phone_type = models.ForeignKey(PhoneType, on_delete=models.SET_NULL, null=True)
    favorite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"