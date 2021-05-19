from django.db import models
from django.contrib.auth.models import User


class Plans(models.Model):
    id_plan = models.AutoField(primary_key=True)
    plan = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = 'Plans'


class Clients(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    id_clie = models.AutoField(primary_key=True)
    imag_clie = models.ImageField(null=True, blank=True, height_field='400', width_field='400', upload_to="images/faces/")
    plan_id = models.ForeignKey(Plans, null=True, blank=True, on_delete=models.CASCADE, db_column='plans_id_plan')
    worker_id_work = models.ForeignKey(
                                        'Workers', on_delete=models.CASCADE, db_column='worker_id_work', blank=True,
                                        null=True)

    class Meta:
        verbose_name_plural = 'clients'


class GoogleReports(models.Model):
    id_goog_repo = models.AutoField(primary_key=True)
    clients_id_clie = models.ForeignKey(Clients, on_delete=models.CASCADE, db_column='clients_id_clie')
    date_gore = models.DateField()
    id_clai_gore = models.CharField(max_length=45)
    type_clai_gore = models.CharField(max_length=45)
    stat_gore = models.CharField(max_length=45)
    urls_gore = models.TextField()
    cant_urls_gore = models.IntegerField()

    class Meta:
        verbose_name_plural = 'google_reports'


class Nicks(models.Model):
    id_nick = models.AutoField(primary_key=True)
    clients_id_clie = models.ForeignKey(Clients, on_delete=models.CASCADE, db_column='clients_id_clie')
    nick = models.CharField(max_length=45)
    prio = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = 'nicks'


class NicksHasPages(models.Model):
    id_nick_page = models.AutoField(primary_key=True)
    nicks_id_nick = models.ForeignKey(Nicks, on_delete=models.CASCADE, db_column='nicks_id_nick')
    pages_id_pages = models.ForeignKey('Pages', on_delete=models.CASCADE, db_column='pages_id_pages')

    class Meta:
        verbose_name_plural = 'nicks_has_pages'


class Pages(models.Model):
    id_page = models.AutoField(primary_key=True)
    name_page = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = 'pages'


class TubeHasPages(models.Model):
    id_tube_pages = models.CharField(primary_key=True, max_length=45)
    tube_reports_id_tube_repo = models.ForeignKey('TubeReports', on_delete=models.CASCADE, db_column='tube_reports_id_tube_repo')
    tube_pages_id_tube_pages = models.ForeignKey('TubePages', on_delete=models.CASCADE, db_column='tube_pages_id_tube_pages')
    tube_urls = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = 'tube_has_pages'


class TubePages(models.Model):
    id_tube_pages = models.AutoField(primary_key=True)
    name_tube_page = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = 'tube_pages'


class TubeReports(models.Model):
    id_tube_repo = models.AutoField(primary_key=True)
    clients_id_clie = models.ForeignKey(Clients, on_delete=models.CASCADE, db_column='clients_id_clie')
    stat_tube = models.CharField(max_length=45)
    date_tube = models.DateField()

    class Meta:
        verbose_name_plural = 'tube_reports'


class Workers(models.Model):
    id_work = models.AutoField(primary_key=True)
    name_work = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = 'workers'
