# Generated by Django 5.1.7 on 2025-03-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='receipts/')),
                ('text', models.TextField(blank=True)),
                ('amount', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('groceries', 'Groceries'), ('utilities', 'Utilities'), ('travel', 'Travel'), ('entertainment', 'Entertainment'), ('other', 'Other')], default='other', max_length=20)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
