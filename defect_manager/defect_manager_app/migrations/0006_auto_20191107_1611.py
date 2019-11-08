# Generated by Django 2.2.5 on 2019-11-07 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defect_manager_app', '0005_auto_20191107_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defect',
            name='defect_type',
            field=models.CharField(choices=[('Configuration', 'Configuration'), ('Tester Error', 'Tester Error'), ('User Interface', 'User Interface'), ('Other', 'OTHER')], default='Configuration', max_length=64),
        ),
        migrations.AlterField(
            model_name='defect',
            name='severity',
            field=models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='', max_length=8),
        ),
    ]