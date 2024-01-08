# Generated by Django 4.2.5 on 2024-01-08 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('max_anzahl', models.SmallIntegerField()),
                ('offene_AG', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AGKategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Datumsraum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdatum', models.DateTimeField()),
                ('enddatum', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gruppe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nutzer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=100)),
                ('nachname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Raum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raum_nr', models.CharField(max_length=12)),
                ('geschoss', models.CharField(max_length=4)),
                ('kapazitaet', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zeitraum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startzeit', models.TimeField()),
                ('endzeit', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schueler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klasse', models.CharField(max_length=3)),
                ('tag_id', models.CharField(max_length=100)),
                ('bus_kind', models.BooleanField()),
                ('name_eb', models.CharField(max_length=100)),
                ('kontakt_eb', models.CharField(max_length=300)),
                ('ag_buchungen', models.ManyToManyField(to='main_app.ag')),
                ('gruppen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.gruppe')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nutzer')),
            ],
        ),
        migrations.CreateModel(
            name='Raum_Belegung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tablet_id', models.BigIntegerField(null=True)),
                ('ag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.ag')),
                ('raum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.raum')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolle', models.CharField(max_length=40)),
                ('is_password_otp', models.BooleanField(default=True)),
                ('nutzer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.nutzer')),
                ('rechte_gruppe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('can_import', 'Can import excel data')],
            },
        ),
        migrations.AddField(
            model_name='gruppe',
            name='gruppenleiter_leiter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.personal'),
        ),
        migrations.AddField(
            model_name='gruppe',
            name='raum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.raum'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_wert', models.CharField(choices=[('GOOD', 'Good'), ('MEDIUM', 'Medium'), ('BAD', 'Bad')], default='MEDIUM', max_length=6)),
                ('schueler_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.schueler')),
            ],
        ),
        migrations.CreateModel(
            name='Aufenthalt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raum_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.raum')),
                ('schueler_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.schueler')),
                ('zeitraum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.zeitraum')),
            ],
        ),
        migrations.CreateModel(
            name='AGZeit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wochentag', models.TextField(choices=[('Montag', 'Montag'), ('Dienstag', 'Dienstag'), ('Mittwoch', 'Mittwoch'), ('Donnerstag', 'Donnerstag'), ('Freitag', 'Freitag')], default='Montag', max_length=10)),
                ('zeitraum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.zeitraum')),
            ],
        ),
        migrations.AddField(
            model_name='ag',
            name='ag_kategorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.agkategorie'),
        ),
        migrations.AddField(
            model_name='ag',
            name='ag_zeit',
            field=models.ManyToManyField(to='main_app.agzeit'),
        ),
        migrations.AddField(
            model_name='ag',
            name='angebots_datum_raum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.datumsraum'),
        ),
        migrations.AddField(
            model_name='ag',
            name='leiter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.personal'),
        ),
    ]
