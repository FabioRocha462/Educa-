# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
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
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    action_time = models.DateTimeField()

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
    name = models.CharField(max_length=50)
    domain = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'django_site'


class DocumentsMemorando(models.Model):
    uuid = models.CharField(primary_key=True, max_length=32)
    others = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField()
    receiver = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    confirm = models.BooleanField(blank=True, null=True)
    destiny = models.CharField(max_length=50)
    title = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_memorando'


class DocumentsOfficial(models.Model):
    uuid = models.CharField(primary_key=True, max_length=32)
    number = models.IntegerField()
    others = models.CharField(max_length=255, blank=True, null=True)
    receiver = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    confirm = models.BooleanField(blank=True, null=True)
    destiny = models.CharField(max_length=50)
    title = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_official'


class DocumentsRequeriment(models.Model):
    uuid = models.CharField(primary_key=True, max_length=32)
    number = models.IntegerField()
    others = models.CharField(max_length=255, blank=True, null=True)
    receiver = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    confirm = models.BooleanField(blank=True, null=True)
    destiny = models.CharField(max_length=50)
    title = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_requeriment'


class EventsEvent(models.Model):
    uuid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=2)
    date = models.DateField()
    status_activated = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events_event'


class EventsFoodEvent(models.Model):
    quantity = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    event = models.ForeignKey(EventsEvent, models.DO_NOTHING)
    food = models.ForeignKey('ProductsFood', models.DO_NOTHING)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events_food_event'


class ProductsCleaning(models.Model):
    uuid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_cleaning'


class ProductsCleaningRequestcleaning(models.Model):
    quantity = models.FloatField(blank=True, null=True)
    cleaning = models.ForeignKey(ProductsCleaning, models.DO_NOTHING, blank=True, null=True)
    requestcleaning = models.ForeignKey('ProductsRequestCleaning', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_cleaning_requestcleaning'


class ProductsFood(models.Model):
    uuid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    validity = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    bidding_value = models.FloatField(blank=True, null=True)
    typecategoria = models.CharField(db_column='typeCategoria', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'products_food'


class ProductsFoodRequestfood(models.Model):
    quantity = models.FloatField(blank=True, null=True)
    food = models.ForeignKey(ProductsFood, models.DO_NOTHING, blank=True, null=True)
    requestfood = models.ForeignKey('ProductsRequestFood', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_food_requestfood'


class ProductsRequestCleaning(models.Model):
    uuid = models.CharField(primary_key=True, max_length=32)
    status_activate = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_request_cleaning'


class ProductsRequestFood(models.Model):
    uuid = models.CharField(primary_key=True, max_length=32)
    status_activate = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_request_food'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    extra_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    key = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class UsersUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=32)
    email = models.CharField(unique=True, max_length=254)
    image = models.CharField(max_length=100, blank=True, null=True)
    typeuser = models.CharField(db_column='typeUser', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)
