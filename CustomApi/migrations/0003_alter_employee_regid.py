# Generated by Django 4.2.2 on 2023-06-28 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomApi', '0002_alter_employee_regid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='regid',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
