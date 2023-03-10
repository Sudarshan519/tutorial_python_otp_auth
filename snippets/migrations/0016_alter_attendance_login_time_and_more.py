# Generated by Django 4.1.5 on 2023-01-26 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0015_rename_start_time_company_login_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='login_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='logout_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='break_end',
            field=models.TimeField(blank=True, default='13:45:00'),
        ),
        migrations.AlterField(
            model_name='company',
            name='break_start',
            field=models.TimeField(blank=True, default='13:00:00'),
        ),
        migrations.AlterField(
            model_name='company',
            name='login_time',
            field=models.TimeField(blank=True, default='9:00:00'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logout_time',
            field=models.TimeField(blank=True, default='18:00:00'),
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reason', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
