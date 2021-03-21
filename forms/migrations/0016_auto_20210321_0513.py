# Generated by Django 3.1.5 on 2021-03-21 05:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0015_auto_20210319_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factsheetdynamicindicatorsmodel',
            name='prov',
            field=models.CharField(blank=True, choices=[('', 'Yes/No'), ('yes', 'Yes'), ('no', 'No')], default='Choose Your Option', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='financialexpensesmodel',
            name='cultToolsDate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='financialexpensesmodel',
            name='fenceDate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='financialexpensesmodel',
            name='fertilizersDate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='financialexpensesmodel',
            name='irrigationDate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='financialexpensesmodel',
            name='laborDate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='financialexpensesmodel',
            name='miscellaneousDate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='financialexpensesmodel',
            name='seedsDate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='financialexpensesmodel',
            name='soilPrepDate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='financialexpensesmodel',
            name='transportaionDate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='outputindicatorsmodel',
            name='harvestDate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='outputindicatorsmodel',
            name='lostQuant',
            field=models.CharField(blank=True, choices=[('', 'Yes/No'), ('yes', 'Yes'), ('no', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='outputindicatorsmodel',
            name='sowingDate',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]