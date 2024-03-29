# Generated by Django 5.0.1 on 2024-02-13 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soma', '0002_remove_book_cover_alter_member_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='book',
        ),
        migrations.RemoveField(
            model_name='member',
            name='status',
        ),
        migrations.AddField(
            model_name='book',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='soma.member'),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('AV', 'Available'), ('UN', 'Unavailable')], default='AV', max_length=2),
        ),
        migrations.AlterField(
            model_name='booktransaction',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_transaction', to='soma.book'),
        ),
        migrations.AlterField(
            model_name='booktransaction',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_transaction', to='soma.member'),
        ),
    ]
