from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    name =  models.CharField(max_length=60)
    image = models.FilePathField(max_length=500)
    price = models.IntegerField(10)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

