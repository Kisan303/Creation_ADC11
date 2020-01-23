# Generated by Django 3.0.1 on 2020-01-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=250)),
                ('confirm_password', models.CharField(max_length=250)),
            ],
        ),
    ]
