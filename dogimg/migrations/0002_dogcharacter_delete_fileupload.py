# Generated by Django 4.0.4 on 2022-04-27 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogimg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dogcharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idx', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=50)),
                ('char', models.TextField(null=True)),
                ('speci', models.TextField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FileUpload',
        ),
    ]
