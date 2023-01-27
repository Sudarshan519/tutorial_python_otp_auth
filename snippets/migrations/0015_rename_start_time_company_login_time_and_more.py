# Generated by Django 4.1.5 on 2023-01-26 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0014_remove_company_owner_company_break_start_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='start_time',
            new_name='login_time',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='stop_time',
            new_name='logout_time',
        ),
        migrations.AddField(
            model_name='company',
            name='break_end',
            field=models.TimeField(default='13:45:00'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_time', models.TimeField(blank=True)),
                ('logout_time', models.TimeField(blank=True)),
                ('date', models.DateField(auto_now=True)),
                ('start_break', models.TimeField(blank=True)),
                ('end_break', models.TimeField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]