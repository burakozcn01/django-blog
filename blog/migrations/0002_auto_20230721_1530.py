# Generated by Django 3.1.5 on 2023-07-21 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name': 'Kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
    ]