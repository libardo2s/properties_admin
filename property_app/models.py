from django.db import models


# Create your models here.
class PropertyType(models.Model):
    name = models.CharField("Tipo", max_length=100)

    class Meta:
        db_table = "properties_type"

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField("Nombre de la Propiedad", max_length=100)
    address = models.CharField("Dirección de la propiedad", max_length=100)
    country = models.CharField("País", max_length=100)
    city = models.CharField("Ciudad", max_length=100)
    zip_code = models.IntegerField("Código Postal")
    type = models.ForeignKey(
        PropertyType, related_name="property_type", on_delete=models.CASCADE
    )
    area = models.DecimalField("Superficie", max_digits=6, decimal_places=2)
    deleted = models.BooleanField("Eliminado", default=False)

    class Meta:
        db_table = "properties"

    def __str__(self):
        return self.name
