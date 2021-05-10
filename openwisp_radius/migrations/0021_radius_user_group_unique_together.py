# Generated by Django 3.1.5 on 2021-01-29 17:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openwisp_radius', '0020_added_optional_registration_fields'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='radiususergroup', unique_together={('user', 'group')},
        ),
    ]