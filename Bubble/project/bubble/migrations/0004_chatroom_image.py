# Generated by Django 5.1.5 on 2025-04-07 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bubble', '0003_alter_chatroom_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='course/'),
        ),
    ]
