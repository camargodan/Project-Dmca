# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_worker = models.IntegerField(blank=True, null=True)
    is_client = models.IntegerField(blank=True, null=True)
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class DmcaClients(models.Model):
    id_clie = models.AutoField(primary_key=True)
    imag_clie = models.CharField(max_length=100, blank=True, null=True)
    plans_id_plan = models.ForeignKey('DmcaPlans', models.DO_NOTHING, db_column='plans_id_plan', blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, blank=True, null=True)
    worker_id_work = models.ForeignKey('DmcaWorkers', models.DO_NOTHING, db_column='worker_id_work', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmca_clients'


class DmcaGooglereports(models.Model):
    id_goog_repo = models.AutoField(primary_key=True)
    date_gore = models.DateField()
    id_clai_gore = models.CharField(max_length=45)
    type_clai_gore = models.CharField(max_length=45)
    stat_gore = models.CharField(max_length=45)
    urls_gore = models.TextField()
    cant_urls_gore = models.IntegerField()
    clients_id_clie = models.ForeignKey(DmcaClients, models.DO_NOTHING, db_column='clients_id_clie')

    class Meta:
        managed = False
        db_table = 'dmca_googlereports'


class DmcaNicks(models.Model):
    id_nick = models.AutoField(primary_key=True)
    nick = models.CharField(max_length=45)
    prio = models.CharField(max_length=45)
    clients_id_clie = models.ForeignKey(DmcaClients, models.DO_NOTHING, db_column='clients_id_clie')

    class Meta:
        managed = False
        db_table = 'dmca_nicks'


class DmcaNickshaspages(models.Model):
    id_nick_page = models.AutoField(primary_key=True)
    nicks_id_nick = models.ForeignKey(DmcaNicks, models.DO_NOTHING, db_column='nicks_id_nick')
    pages_id_pages = models.ForeignKey('DmcaPages', models.DO_NOTHING, db_column='pages_id_pages')

    class Meta:
        managed = False
        db_table = 'dmca_nickshaspages'


class DmcaPages(models.Model):
    id_page = models.AutoField(primary_key=True)
    name_page = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'dmca_pages'


class DmcaPlans(models.Model):
    id_plan = models.AutoField(primary_key=True)
    plan = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'dmca_plans'


class DmcaTubehaspages(models.Model):
    id_tube_pages = models.CharField(primary_key=True, max_length=45)
    tube_urls = models.CharField(max_length=45)
    tube_pages_id_tube_pages = models.ForeignKey('DmcaTubepages', models.DO_NOTHING, db_column='tube_pages_id_tube_pages')
    tube_reports_id_tube_repo = models.ForeignKey('DmcaTubereports', models.DO_NOTHING, db_column='tube_reports_id_tube_repo')

    class Meta:
        managed = False
        db_table = 'dmca_tubehaspages'


class DmcaTubepages(models.Model):
    id_tube_pages = models.AutoField(primary_key=True)
    name_tube_page = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'dmca_tubepages'


class DmcaTubereports(models.Model):
    id_tube_repo = models.AutoField(primary_key=True)
    stat_tube = models.CharField(max_length=45)
    date_tube = models.DateField()
    clients_id_clie = models.ForeignKey(DmcaClients, models.DO_NOTHING, db_column='clients_id_clie')

    class Meta:
        managed = False
        db_table = 'dmca_tubereports'


class DmcaWorkers(models.Model):
    id_work = models.AutoField(primary_key=True)
    name_work = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'dmca_workers'


class SocialaccountSocialaccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    socialapp_id = models.BigIntegerField()
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp_id', 'site'),)


class SocialaccountSocialtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)
