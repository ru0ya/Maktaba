# Generated by Django 4.2.10 on 2024-03-21 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soma', '0005_alter_booktransaction_borrowed_days_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='booktransaction',
            name='date_borrowed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booktransaction',
            name='date_returned',
            field=models.DateTimeField(null=True),
        ),
    ]