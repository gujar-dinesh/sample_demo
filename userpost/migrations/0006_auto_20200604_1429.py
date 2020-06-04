# Generated by Django 3.0.2 on 2020-06-04 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpost', '0005_auto_20200603_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdata',
            name='text',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='postuser',
            name='username',
            field=models.TextField(max_length=15, unique=True),
        ),
    ]