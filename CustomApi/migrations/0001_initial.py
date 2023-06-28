# Generated by Django 4.2.2 on 2023-06-28 07:43

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hno', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualificationName', models.CharField(max_length=100)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=100)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regid', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phoneNo', models.CharField(blank=True, max_length=20)),
                ('photo', stdimage.models.StdImageField(blank=True, force_min_size=False, upload_to='photos/', variations={'thumbnail': {'crop': True, 'height': 100, 'width': 100}})),
                ('addressDetails', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CustomApi.address')),
                ('projects', models.ManyToManyField(to='CustomApi.project')),
                ('qualifications', models.ManyToManyField(to='CustomApi.qualification')),
                ('workExperience', models.ManyToManyField(to='CustomApi.workexperience')),
            ],
        ),
    ]
