# Generated by Django 4.1.5 on 2023-01-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0023_remove_approver_company_remove_approver_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='approvers',
            field=models.ManyToManyField(blank=True, null=True, to='snippets.approver'),
        ),
    ]
