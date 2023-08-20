# Generated by Django 4.2.4 on 2023-08-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='is_completed'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.CharField(max_length=100, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_at'),
        ),
        migrations.AlterField(
            model_name='usertodo',
            name='order',
            field=models.PositiveSmallIntegerField(verbose_name='order'),
        ),
    ]