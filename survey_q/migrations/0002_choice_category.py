# Generated by Django 4.0.4 on 2022-04-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_q', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='category',
            field=models.CharField(choices=[('CC', 'checkbox'), ('RR', 'radio'), ('SS', 'select')], default='CC', max_length=10, verbose_name='유형 선택'),
        ),
    ]
