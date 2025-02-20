# Generated by Django 4.2.1 on 2024-02-28 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PROCEEDING.country')),
            ],
        ),
        migrations.CreateModel(
            name='Proceeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('first_last_name', models.CharField(max_length=30)),
                ('second_last_name', models.CharField(max_length=30)),
                ('dateEval', models.DateField()),
                ('dateNac', models.DateField()),
                ('language', models.CharField(max_length=30)),
                ('indigenous_language', models.CharField(max_length=30)),
                ('talk_other_language', models.BooleanField()),
                ('other_languages', models.CharField(blank=True, max_length=40, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('scholarship', models.CharField(max_length=30)),
                ('years_study', models.IntegerField()),
                ('laterality', models.CharField(max_length=12)),
                ('occupation', models.CharField(max_length=30)),
                ('instrument', models.CharField(max_length=10)),
                ('time_instrument', models.CharField(blank=True, max_length=15, null=True)),
                ('hobbies', models.CharField(max_length=24)),
                ('time_hobbies', models.CharField(blank=True, max_length=24, null=True)),
                ('civil_status', models.CharField(max_length=12)),
                ('religion', models.CharField(max_length=18)),
                ('mother_scholarship', models.CharField(max_length=30)),
                ('father_scholarship', models.CharField(max_length=30)),
                ('referred_by', models.CharField(max_length=60)),
                ('phone_number', models.CharField(max_length=14)),
                ('reason_consultation', models.CharField(max_length=60)),
                ('alert_status', models.CharField(max_length=60)),
                ('medicine', models.CharField(max_length=60)),
                ('other_exams', models.CharField(max_length=60)),
                ('medical_history', models.CharField(blank=True, max_length=400, null=True)),
                ('hyperthension', models.BooleanField()),
                ('time_hyperthension', models.CharField(blank=True, max_length=16, null=True)),
                ('pulmonary_diseases', models.BooleanField()),
                ('time_pulmonary_diseases', models.CharField(blank=True, max_length=16, null=True)),
                ('alcoholism', models.BooleanField()),
                ('time_alcoholism', models.CharField(blank=True, max_length=16, null=True)),
                ('drugs', models.BooleanField()),
                ('time_drugs', models.CharField(blank=True, max_length=16, null=True)),
                ('decrease_senses', models.BooleanField()),
                ('time_decrease_senses', models.CharField(blank=True, max_length=16, null=True)),
                ('craniocerebral_trauma', models.BooleanField()),
                ('time_craniocerebral_trauma', models.CharField(blank=True, max_length=16, null=True)),
                ('diabetes', models.BooleanField()),
                ('time_diabetes', models.CharField(blank=True, max_length=16, null=True)),
                ('hypothyroidism', models.BooleanField()),
                ('time_hypothyroidism', models.CharField(blank=True, max_length=16, null=True)),
                ('strokes', models.BooleanField()),
                ('time_strokes', models.CharField(blank=True, max_length=16, null=True)),
                ('others_diseases', models.BooleanField()),
                ('details_others_diseases', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PROCEEDING.country')),
                ('municipality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PROCEEDING.municipality')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PROCEEDING.state')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='municipality',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PROCEEDING.state'),
        ),
    ]
