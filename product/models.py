from django.db import models
from django.contrib.auth.models import User
from slugify import slugify


class BaseModel(models.Model):
    slug = models.SlugField(db_index=True, unique=True,
                            null=True, blank=True, max_length=512)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Currency(BaseModel):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "currency"


class Category(BaseModel):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"


class Brand(BaseModel):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "brand"


class Tag(BaseModel):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tag"


class Product(BaseModel):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
