# Generated by Django 3.1.1 on 2020-10-12 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0008_delete_secondpagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondPageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
    ]
