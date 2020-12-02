# Generated by Django 3.1.4 on 2020-12-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/avatar/'),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]
