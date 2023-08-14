# Generated by Django 2.2 on 2023-08-14 11:55

from django.db import migrations, models
import immin.validators


class Migration(migrations.Migration):

    dependencies = [
        ('immin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(error_messages={'unique': '이미 사용중인 닉네임입니다.'}, max_length=15, null=True, unique=True, validators=[immin.validators.validate_no_special_characters]),
        ),
    ]