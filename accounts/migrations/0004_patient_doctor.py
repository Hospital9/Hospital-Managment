# Generated by Django 4.1.4 on 2022-12-15 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.doctor'),
        ),
    ]
