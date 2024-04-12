# Generated by Django 4.2.11 on 2024-04-12 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('orgs', '0003_alter_organization_managers_and_more'), ('orgs', '0004_alter_organization_type'), ('orgs', '0005_alter_organization_type')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orgs', '0002_add_organization_type_and_more'),
        ('users', '0003_alter_profile_contact_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='managers',
            field=models.ManyToManyField(blank=True, related_name='managers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='territory',
            field=models.ManyToManyField(blank=True, related_name='territory', to='users.region'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='orgs.organizationtype'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='orgs.organizationtype'),
        ),
    ]
