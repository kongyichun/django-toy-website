# Generated by Django 2.1.9 on 2019-06-28 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playApp', '0003_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32)),
                ('article_name', models.CharField(max_length=200)),
            ],
        ),
    ]
