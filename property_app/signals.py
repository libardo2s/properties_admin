from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import PropertyType


@receiver(post_migrate)
def populate_property_types(sender, **kwargs):
    property_types = ["Casa", "Apartamento", "Oficina", "Comercial"]
    for property_type in property_types:
        PropertyType.objects.get_or_create(name=property_type)
