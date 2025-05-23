from django.db import models
from utils.base_model import BaseModel


class Product(BaseModel):
    
    name = models.CharField(max_length=255, null=False, blank=False)
    product_image = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("-id", )
