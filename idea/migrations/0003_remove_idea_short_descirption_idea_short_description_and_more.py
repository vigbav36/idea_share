# Generated by Django 4.0.6 on 2022-07-19 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0002_idea_applicants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='short_descirption',
        ),
        migrations.AddField(
            model_name='idea',
            name='short_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='long_description',
            field=models.TextField(null=True),
        ),
    ]
