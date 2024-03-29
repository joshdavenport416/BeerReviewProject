# Generated by Django 2.2 on 2019-06-12 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BeerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=255)),
                ('typedescription', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'beertypes',
                'db_table': 'beertype',
            },
        ),
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beername', models.CharField(max_length=255)),
                ('beerprice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('beerentrydate', models.DateField()),
                ('beerurl', models.URLField(blank=True, null=True)),
                ('beerdescription', models.TextField()),
                ('beertype', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='beerapp.BeerType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'beers',
                'db_table': 'beer',
            },
        ),
    ]
