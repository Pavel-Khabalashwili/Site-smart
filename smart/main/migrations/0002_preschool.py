# Generated by Django 4.2.7 on 2023-11-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('anons', models.TextField(verbose_name='Анонс')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'До-школьное',
                'verbose_name_plural': 'До-школьные',
            },
        ),
    ]
