# Generated by Django 4.2.4 on 2023-08-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandcenter', '0002_post_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='epic_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]