# Generated by Django 5.1.5 on 2025-01-26 11:19

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePreparationGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(upload_to='Yuriqnoma/articles/', verbose_name="Yo'riqnoma fayli")),
            ],
            options={
                'verbose_name': "Maqola yo'riqnomasi",
                'verbose_name_plural': "Maqolalar yo'riqnomasi",
            },
        ),
        migrations.CreateModel(
            name='CopyRight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Mualliflik huquqi nomi')),
                ('content', django_ckeditor_5.fields.CKEditor5Field()),
            ],
            options={
                'verbose_name': 'Mualliflik huquqi',
                'verbose_name_plural': 'Mualliflik huquqlari',
            },
        ),
        migrations.CreateModel(
            name='SampleDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='namunaviy hujjat nomi')),
                ('content', django_ckeditor_5.fields.CKEditor5Field()),
            ],
            options={
                'verbose_name': 'Namunaviy hujjat',
                'verbose_name_plural': 'Namunaviy hujjatlari',
            },
        ),
    ]
