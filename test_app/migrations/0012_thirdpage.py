# Generated by Django 3.1.1 on 2020-10-12 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0011_secondpagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thirdpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
    ]
