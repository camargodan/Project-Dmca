from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.template.defaultfilters import slugify


class User(AbstractUser):
    is_client = models.BooleanField(default=True)
    is_worker = models.BooleanField(default=False)
    imag_clie = models.ImageField(null=True, blank=True, upload_to="dmca/static/images/faces/")
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def get_absolute_url(self):
        return reverse('edit_user', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)
