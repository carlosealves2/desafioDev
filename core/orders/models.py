from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Product(models.Model):
    SITUATION = (
        ('av', 'Available'),
        ('un', 'Unavailable')
    )
    name = models.CharField(_("Name"), max_length=200)
    unitary_value = models.DecimalField(_("Unitary value"), decimal_places=2, max_digits=10)
    quantity_stock = models.IntegerField(_("Quantity in stock"))
    product_situation = models.CharField(_("Product situation"), choices=SITUATION, max_length=2)

    def __str__(self):
        return f"<Product: name: {self.name}, stock: {self.quantity_stock}, situation: {self.product_situation}>"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.quantity_stock > 0:
            self.product_situation = 'av'
        else:
            self.product_situation = 'un'

        return super(Product, self).save(force_insert=False, force_update=False, using=None,
                                         update_fields=None)
