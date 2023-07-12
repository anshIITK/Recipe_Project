# Generated by Django 4.2.3 on 2023-07-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=50)),
                ('recipe_desc', models.TextField()),
                ('recipe_img', models.ImageField(upload_to='path of Image')),
            ],
        ),
    ]
