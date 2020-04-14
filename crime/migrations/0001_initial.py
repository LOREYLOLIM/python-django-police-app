# Generated by Django 2.1.7 on 2020-04-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('SureName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('PhoneNumber', models.IntegerField()),
                ('Location', models.CharField(max_length=50)),
                ('Date', models.DateTimeField(auto_now=True)),
                ('CrimeType', models.CharField(max_length=50)),
                ('CrimeDesciption', models.TextField(max_length=1000)),
            ],
        ),
    ]