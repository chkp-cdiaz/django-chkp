# Generated by Django 2.1.1 on 2018-10-22 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIR80', '0012_mgmtserverobjects_mgmtserverfilepathudpports'),
    ]

    operations = [
        migrations.AddField(
            model_name='mgmtserverobjects',
            name='MGMTServerFilePathNetworksObjects',
            field=models.CharField(default='/home/carlos/django-chkp/APIR80/tmp/chkpobjectsnetworks.txt', max_length=250),
        ),
    ]
