# Generated by Django 2.2.6 on 2020-04-25 10:21
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dialogmans', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
