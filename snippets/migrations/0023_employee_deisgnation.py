# Generated by Django 3.2.16 on 2023-01-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0022_auto_20230127_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='deisgnation',
            field=models.CharField(blank=True, default='staff', max_length=32, null=True),
        ),
    ]
