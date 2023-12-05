from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group


# Create your models here.

# Zeitraum enthält zwei Uhrzeiten
class Zeitraum(models.Model):
    startzeit = models.TimeField()
    endzeit = models.TimeField(null=True)
# Datumsraum enhält zwei Tage mit konkreter Uhrzeit
class Datumsraum(models.Model):
    startdatum = models.DateTimeField()
    enddatum = models.DateTimeField()
class Nutzer(models.Model):
    vorname = models.CharField(max_length=100)
    nachname = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
class Personal(models.Model):
    rolle = models.CharField(max_length=40)
    rechte_gruppe = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)       # null=True rausmachen
    nutzer = models.ForeignKey(Nutzer, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null= True)    # null=True rausmachen
    is_password_otp = models.BooleanField(default=True)

    class Meta:
        permissions = [("can_import", "Can import excel data")]

class Raum(models.Model):
    raum_nr = models.SmallIntegerField()
    geschoss = models.CharField(max_length=4)
    kapazitaet = models.SmallIntegerField()
class Gruppe(models.Model):
    name = models.CharField(max_length=50)
    gruppenleiter_leiter = models.ForeignKey(Personal, on_delete=models.SET_NULL, null = True)        # ?
    raum = models.ForeignKey(Raum, on_delete=models.SET_NULL, null=True)

class AGZeit(models.Model):
    class WOCHENTAG(models.TextChoices):
        MONTAG = "Montag"
        DIENSTAG = "Dienstag"
        MITTWOCH = "Mittwoch"
        DONNERSTAG = "Donnerstag"
        FREITAG = "Freitag"
    
    wochentag = models.TextField(choices=WOCHENTAG.choices, default=WOCHENTAG.MONTAG, max_length=10)
    zeitraum = models.ForeignKey(Zeitraum, on_delete=models.CASCADE)

class AG(models.Model):
    name = models.CharField(max_length=50)
    beschreibung = models.CharField(max_length=500)
    max_anzahl = models.SmallIntegerField()
    offene_AG = models.BooleanField() 
    leiter = models.ForeignKey(Personal, on_delete=models.CASCADE, null=True)       # null=True entfernen
    angebots_datum_raum = models.ForeignKey(Datumsraum, on_delete=models.CASCADE, null=True)    # null=True entfernen
    ag_zeit = models.ManyToManyField(AGZeit, null=True)

class Schueler(models.Model):
    klasse = models.CharField(max_length=3)             # optional
    tag_id = models.CharField(max_length=100)          #max_length abhängig von Tags id länge
    bus_kind = models.BooleanField()
    name_eb = models.CharField(max_length=100)
    kontakt_eb = models.CharField(max_length=300)
    # angemeldet = models.BooleanField(default=FALSE)      # Ist kind überhaupt an diesem Tag in der OGS
    user_id = models.ForeignKey(Nutzer, on_delete=models.CASCADE)
    gruppen_id = models.ForeignKey(Gruppe, on_delete=models.CASCADE)
    ag_buchungen = models.ManyToManyField(AG)
class Feedback(models.Model):
    class Feedbacks(models.TextChoices):
        GOOD = "GOOD"
        MEDIUM = "MEDIUM"
        BAD = "BAD"

    feedback_wert = models.CharField(choices=Feedbacks.choices, default=Feedbacks.MEDIUM, max_length=6)
    tag = models.DateField
    schueler_id = models.ForeignKey(Schueler, on_delete=models.CASCADE)
class Raum_Belegung(models.Model):
    tablet_id = models.BigIntegerField()
    raum = models.ForeignKey(Raum, on_delete=models.CASCADE)
    aufsichtsperson = models.ForeignKey(Personal, on_delete=models.CASCADE)             # in Raum_Belegung oder AG oder beides?
    angebots_zeit = models.ForeignKey(Zeitraum, on_delete=models.CASCADE)
    angebots_zeitraum = models.ForeignKey(Datumsraum, on_delete=models.CASCADE)
    ag = models.ForeignKey(AG, on_delete=models.CASCADE)
class Aufenthalt(models.Model):                # Zuordnung wo sich Kinder befunden haben, wird mit löschen des Zeitraums auch gelöscht
    tag = models.DateField
    schueler_id = models.ForeignKey(Schueler, on_delete=models.CASCADE)
    raum_id = models.ForeignKey(Raum, on_delete=models.CASCADE)
    zeitraum = models.ForeignKey(Zeitraum, on_delete=models.CASCADE)
# class Buchung_AG(models.Model):            # Zuordunung zwischen Schüler und AGS
#     schueler_id = models.ForeignKey(Schueler, on_delete=models.CASCADE)
#     ag_id = models.ForeignKey(AG, on_delete=models.CASCADE)
    