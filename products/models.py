from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Mahsulot nomi")
    description = models.TextField(verbose_name="Tavsif")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Soni")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
    upload_to='products/',
    blank=True,
    null=True,
    verbose_name="Mahsulot rasmi"
)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"