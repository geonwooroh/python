# Generated by Django 4.2.7 on 2023-11-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_update_at_alter_post_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]