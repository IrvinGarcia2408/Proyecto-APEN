from django import forms 
from .models import Country, Municipality, Proceeding, State

class ProceedingForm(forms.ModelForm):
    other_languages = forms.CharField(required=False)
    time_instrument = forms.ChoiceField(
        choices=[('', 'Seleccione opción'), ('Menor a 1 año', 'Menor a 1 año'), ('De 1 a 5 años', 'De 1 a 5 años'), ('De 5 a 10 años', 'De 5 a 10 años'), ('De 10 a 15 años', 'De 10 a 15 años'), ('Más de 15 años', 'Más de 15 años')],
        required=False
    )
    time_hobbies = forms.ChoiceField(
        choices=[('', 'Seleccione opción'), ('Diario', 'Diario'), ('Una vez a la semana', 'Una vez a la semana'), ('Dos veces a la semana', 'Dos veces a la semana'), ('Una vez al mes', 'Una vez al mes')],
        required=False
    )
    time_hyperthension = forms.ChoiceField(
        choices=[('', 'Seleccione opción'), ('Menor a 1 año', 'Menor a 1 año'), ('De 1 a 5 años', 'De 1 a 5 años'), ('De 5 a 10 años', 'De 5 a 10 años'), ('De 10 a 15 años', 'De 10 a 15 años'), ('Más de 15 años', 'Más de 15 años')],
        required=False
    )
    time_pulmonary_diseases = forms.ChoiceField(
        choices=[('', 'Seleccione opción'), ('Menor a 1 año', 'Menor a 1 año'), ('De 1 a 5 años', 'De 1 a 5 años'), ('De 5 a 10 años', 'De 5 a 10 años'), ('De 10 a 15 años', 'De 10 a 15 años'), ('Más de 15 años', 'Más de 15 años')],
        required=False
    )
    time_alcoholism = forms.ChoiceField(
        choices=[('', 'Seleccione opción'), ('Menor a 1 año', 'Menor a 1 año'), ('De 1 a 5 años', 'De 1 a 5 años'), ('De 5 a 10 años', 'De 5 a 10 años'), ('De 10 a 15 años', 'De 10 a 15 años'), ('Más de 15 años', 'Más de 15 años')],
        required=False
    )
    time_drugs = forms.ChoiceField(
        choices=[('', 'Seleccione opción'), ('Menor a 1 año', 'Menor a 1 año'), ('De 1 a 5 años', 'De 1 a 5 años'), ('De 5 a 10 años', 'De 5 a 10 años'), ('De 10 a 15 años', 'De 10 a 15 años'), ('Más de 15 años', 'Más de 15 años')],
        required=False
    )
    time_decrease_senses = forms.ChoiceField(
        choices=[('', 'Seleccione opción'), ('Menor a 1 año', 'Menor a 1 año'), ('De 1 a 5 años', 'De 1 a 5 años'), ('De 5 a 10 años', 'De 5 a 10 años'), ('De 10 a 15 años', 'De 10 a 15 años'), ('Más de 15 años', 'Más de 15 años')],
        required=False
    )
    time_craniocerebral_trauma = forms.ChoiceField(
        choices=[('', 'Seleccione opción'), ('Menor a 1 año', 'Menor a 1 año'), ('De 1 a 5 años', 'De 1 a 5 años'), ('De 5 a 10 años', 'De 5 a 10 años'), ('De 10 a 15 años', 'De 10 a 15 años'), ('Más de 15 años', 'Más de 15 años')],
        required=False
    )
    time_diabetes = forms.ChoiceField(
        choices=[('', 'Seleccione opción'), ('Menor a 1 año', 'Menor a 1 año'), ('De 1 a 5 años', 'De 1 a 5 años'), ('De 5 a 10 años', 'De 5 a 10 años'), ('De 10 a 15 años', 'De 10 a 15 años'), ('Más de 15 años', 'Más de 15 años')],
        required=False
    )
    time_hypothyroidism = forms.ChoiceField(
        choices=[('', 'Seleccione opción'), ('Menor a 1 año', 'Menor a 1 año'), ('De 1 a 5 años', 'De 1 a 5 años'), ('De 5 a 10 años', 'De 5 a 10 años'), ('De 10 a 15 años', 'De 10 a 15 años'), ('Más de 15 años', 'Más de 15 años')],
        required=False
    )
    time_strokes = forms.ChoiceField(
        choices=[('', 'Seleccione opción'), ('Menor a 1 año', 'Menor a 1 año'), ('De 1 a 5 años', 'De 1 a 5 años'), ('De 5 a 10 años', 'De 5 a 10 años'), ('De 10 a 15 años', 'De 10 a 15 años'), ('Más de 15 años', 'Más de 15 años')],
        required=False
    )
    details_others_diseases = forms.CharField(required=False)
    medical_history = forms.CharField(required=False)

    class Meta:
        model = Proceeding
        fields = ['name',
                  'first_last_name',
                  'second_last_name',
                  'dateEval',
                  'dateNac',
                  'country',
                  'state',
                  'municipality', 
                  'language',
                  'indigenous_language',
                  'talk_other_language',
                  'other_languages',
                  'gender',
                  'scholarship',
                  'years_study',
                  'laterality',
                  'occupation',
                  'instrument',
                  'time_instrument',
                  'hobbies',
                  'time_hobbies',
                  'civil_status',
                  'religion',
                  'mother_scholarship',
                  'father_scholarship',
                  'referred_by',
                  'phone_number',
                  'reason_consultation',
                  'alert_status',
                  'medicine',
                  'other_exams',
                  'medical_history',
                  'hyperthension',
                  'time_hyperthension',
                  'pulmonary_diseases',
                  'time_pulmonary_diseases',
                  'alcoholism',
                  'time_alcoholism',
                  'drugs',
                  'time_drugs',
                  'decrease_senses',
                  'time_decrease_senses',
                  'craniocerebral_trauma',
                  'time_craniocerebral_trauma',
                  'diabetes',
                  'time_diabetes',
                  'hypothyroidism',
                  'time_hypothyroidism', 
                  'strokes',
                  'time_strokes',
                  'others_diseases',
                  'details_others_diseases'                            
                ]
