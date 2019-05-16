# Generated by Django 2.2.1 on 2019-05-16 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('synapse', models.CharField(max_length=25, null=True)),
                ('bio', models.TextField(null=True)),
                ('profile_pic', models.ImageField(max_length=150, upload_to='./profile_pics/')),
                ('facebook', models.URLField(max_length=150)),
                ('twitter', models.URLField(max_length=150)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('blocked', models.BooleanField(default=False)),
                ('favorite', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('friended', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friended', to=settings.AUTH_USER_MODEL)),
                ('friender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('N', 'None'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('D', 'Decline to answer')], default='N', max_length=2)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Phone Number', max_length=31)),
                ('street', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('state', localflavor.us.models.USStateField(max_length=2)),
                ('country', models.CharField(default='USA', max_length=25)),
                ('zip_code', localflavor.us.models.USZipCodeField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]