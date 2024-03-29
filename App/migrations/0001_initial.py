# Generated by Django 3.2.7 on 2021-09-25 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('acc_name', models.CharField(blank=True, max_length=100, null=True)),
                ('acc_no', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default=0, max_length=50)),
                ('lname', models.CharField(default=0, max_length=50)),
                ('address', models.CharField(default=0, max_length=50)),
                ('room_no', models.CharField(default=0, max_length=50)),
                ('night', models.IntegerField(default='1')),
                ('rrr', models.CharField(default=0, max_length=15)),
                ('lodgeIn', models.CharField(default=0, max_length=50)),
                ('lodgeOut', models.CharField(default=0, max_length=50)),
                ('adult', models.IntegerField(default=1)),
                ('children', models.IntegerField(default=0)),
                ('dob', models.CharField(default=0, max_length=50)),
                ('car', models.IntegerField(default=0)),
                ('meansOfId', models.CharField(blank=True, max_length=200, null=True)),
                ('idNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('tel', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=200, null=True)),
                ('tel', models.CharField(blank=True, max_length=200, null=True)),
                ('car', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HotelConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_care_no', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('parking_charge', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomName', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField()),
                ('img_url', models.CharField(blank=True, max_length=200, null=True)),
                ('catg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.category')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.CharField(blank=True, max_length=200, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='drop_off_driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drop_off_driver', to='App.driver'),
        ),
        migrations.AddField(
            model_name='customer',
            name='pick_up_driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pick_up_driver', to='App.driver'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
