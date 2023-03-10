# Generated by Django 4.1.4 on 2022-12-19 03:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('logo', models.URLField()),
            ],
            options={
                'db_table': 'services',
            },
        ),
        migrations.CreateModel(
            name='Payment_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('paymentDate', models.DateField(default='')),
                ('expirationDate', models.DateField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_services', to='pagos_v2.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'payment_user',
            },
        ),
        migrations.CreateModel(
            name='Expired_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_fee_amount', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('pay_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expired_payments', to='pagos_v2.payment_user', unique=True)),
            ],
            options={
                'db_table': 'expired_payments',
            },
        ),
    ]
