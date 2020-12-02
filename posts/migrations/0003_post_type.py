# Generated by Django 3.1.4 on 2020-12-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201202_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('SEARCH', 'search'), ('RENT', 'rent'), ('BOTH', 'both')], default='BOTH', max_length=10),
        ),
    ]
