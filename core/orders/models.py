from django.urls import reverse
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
        return f"<Product: name: {self.name}, stock: {self.quantity_stock}, situation: {self.get_product_situation_display()}>"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.quantity_stock > 0:
            self.product_situation = 'av'
        else:
            self.product_situation = 'un'

        return super(Product, self).save(force_insert=False, force_update=False, using=None,
                                         update_fields=None)

    def get_absolute_url(self):
        return reverse("app:product_detail", kwargs={"pk": self.pk})


class Order(models.Model):
    STATUS = (
        ('p', 'Pending to send'),
        ('s', 'Sending'),
        ('d', 'Delivered'),
    )

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name=_("Product"))
    quantity = models.IntegerField(_("Quantity"))
    unitary_value = models.DecimalField(_("Unitary value"), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Order date"))
    applicant = models.CharField(_('Applicant'), max_length=150)
    zip_code = models.IntegerField(_("Zip code"))
    uf = models.CharField(_("Federation unity"), max_length=2)
    city = models.CharField(_("City"), max_length=100)
    district = models.CharField(_("District"), max_length=100)
    street = models.CharField(_("Street"), max_length=200)
    number = models.IntegerField(_("Street"))
    forwarding_agent = models.CharField(_("Street"), max_length=200)
    order_situation = models.CharField(choices=STATUS, max_length=1, verbose_name=_("Order situation"), default='p')

    def __str__(self):
        return f"<Order, product: {self.product}, quantity: {self.quantity}, " \
               f"unitary value: {self.unitary_value}, status: {self.order_situation}>"

    def get_absolute_url(self):
        return reverse("app:order_detail", kwargs={"pk": self.pk})
