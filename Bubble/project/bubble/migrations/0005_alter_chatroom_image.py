# Generated by Django 5.1.5 on 2025-04-07 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bubble', '0004_chatroom_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='room/'),
        ),
    ]
