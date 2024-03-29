# Generated by Django 4.0.6 on 2022-07-19 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0002_alter_agenda_dia_horario'),
        ('consulta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='dia',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='hora',
        ),
        migrations.AddField(
            model_name='consulta',
            name='agenda',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='agenda.agenda'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='horario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='agenda.horario'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='data_agendamento',
            field=models.DateField(auto_now_add=True),
        ),
    ]
