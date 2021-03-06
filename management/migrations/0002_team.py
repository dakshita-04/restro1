# Generated by Django 3.0.7 on 2020-08-05 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('designatio', models.CharField(blank=True, max_length=100, null=True)),
                ('img', models.FileField(blank=True, null=True, upload_to='')),
                ('fb', models.URLField(blank=True, null=True)),
                ('tu', models.URLField(blank=True, null=True)),
                ('insta', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
