# Generated by Django 4.0.5 on 2022-07-03 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_answer_answer_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
