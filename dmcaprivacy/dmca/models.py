from datetime import datetime, timedelta
from django.db import models
from django.conf import settings
from django.forms import model_to_dict
from django.urls import reverse
from django.utils.text import slugify

priority_choices = (
    ('Normal', 'Normal'),
    ('High', 'High'),
)
type_claim_choices = (
    ('DMCA-IMAGES', 'DMCA-IMAGES'),
    ('DMCA-CONTENT', 'DMCA-CONTENT'),
)


class Plans(models.Model):
    id_plan = models.AutoField(primary_key=True)
    plan = models.CharField(max_length=45, unique=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = 'Plans'

    def __str__(self):
        return self.plan


class Clients(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='id_client')
    id_clie = models.AutoField(primary_key=True)
    plan_id = models.ForeignKey(Plans, null=True, blank=True, on_delete=models.CASCADE, db_column='plans_id_plan')
    worker_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='id_worker', blank=True, null=True)
    date_assign = models.DateField(default=datetime.now() + timedelta(days=31))

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = 'clients'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Pages(models.Model):
    id_page = models.AutoField(primary_key=True)
    name_page = models.CharField(max_length=45, unique=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = 'pages'

    def __str__(self):
        return self.name_page


class Nicks(models.Model):
    id_nick = models.AutoField(primary_key=True)
    clients_id_clie = models.ForeignKey(Clients, on_delete=models.CASCADE, db_column='clients_id_clie')
    nick = models.CharField(max_length=45)
    prio = models.CharField(max_length=45, choices=priority_choices, default='normal', verbose_name='Priority')
    pages = models.ManyToManyField("Pages", through="NicksPages")

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = 'nicks'

    def __str__(self):
        return self.nick


class NicksPages(models.Model):
    nick = models.ForeignKey("Nicks", on_delete=models.CASCADE)
    page = models.ForeignKey("Pages", on_delete=models.CASCADE)

    def toJSON(self):
        item = model_to_dict(self)
        return item


class TubePages(models.Model):
    id_tube_pages = models.AutoField(primary_key=True)
    name_tube_page = models.CharField(max_length=45, unique=True)
    contact_tube = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = 'tube_pages'

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.name_tube_page


class TubeReports(models.Model):
    id_tube_repo = models.AutoField(primary_key=True)
    clients_id_clie = models.ForeignKey(Clients, on_delete=models.CASCADE)
    date_tube = models.DateField()
    id_tube_pages = models.ForeignKey(TubePages, on_delete=models.CASCADE)
    tube_urls = models.TextField()
    cant_urls = models.IntegerField()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = 'tube_reports'


class GoogleReports(models.Model):
    id_goog_repo = models.AutoField(primary_key=True)
    clients_id_clie = models.ForeignKey(Clients, on_delete=models.CASCADE, db_column='clients_id_clie')
    date_gore = models.DateField()
    id_clai_gore = models.CharField(max_length=45)
    type_clai_gore = models.CharField(max_length=45, choices=type_claim_choices, default='DMCA-IMAGES', verbose_name='Type of claim')
    urls_gore = models.TextField()
    cant_urls_gore = models.IntegerField()

    class Meta:
        verbose_name_plural = 'google_reports'

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.id_clai_gore
