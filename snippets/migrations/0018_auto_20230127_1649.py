# Generated by Django 3.2.16 on 2023-01-27 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0017_alter_attendance_end_break_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='company',
        ),
        migrations.AddField(
            model_name='company',
            name='employer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='snippets.employer'),
        ),
        migrations.AddField(
            model_name='employee',
            name='employer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='snippets.employer'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='snippets.phonemodel'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='phone',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='snippets.phonemodel'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employer', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='Mobile',
            field=models.IntegerField(unique=True),
        ),
    ]