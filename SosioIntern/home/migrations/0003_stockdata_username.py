# Generated by Django 3.2.4 on 2021-06-30 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_data_stockdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdata',
            name='username',
            field=models.CharField(default=0, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]