from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError


def validate_image(imag_clie):
    file_size = imag_clie.file.size
    limit_mb = 4
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)


class User(AbstractUser):
    is_client = models.BooleanField(default=True)
    is_worker = models.BooleanField(default=False)
    imag_clie = models.ImageField(null=True, blank=True, upload_to="dmca/static/images/faces/", validators=[validate_image])
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def get_absolute_url(self):
        return reverse('edit_user', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)
