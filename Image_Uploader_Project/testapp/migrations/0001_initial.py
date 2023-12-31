# Generated by Django 4.1.5 on 2023-07-23 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModelClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='myimage')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'image_table',
            },
        ),
    ]
