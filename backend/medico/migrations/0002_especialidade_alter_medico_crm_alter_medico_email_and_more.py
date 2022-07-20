# Generated by Django 4.0.6 on 2022-07-18 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='medico',
            name='crm',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='email',
            field=models.EmailField(blank=True, max_length=60, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='medico',
            name='especialidade',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='medico.especialidade'),
        ),
    ]
