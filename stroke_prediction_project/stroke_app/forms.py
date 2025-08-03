from django import forms

class StrokePredictionForm(forms.Form):
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], label="Gender")
    age = forms.FloatField(min_value=0, max_value=120, label="Age")
    hypertension = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label="Hypertension")
    heart_disease = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label="Heart Disease")
    ever_married = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], label="Ever Married")
    work_type = forms.ChoiceField(choices=[
        ('children', 'Children'), ('Govt_job', 'Government Job'),
        ('Never_worked', 'Never Worked'), ('Private', 'Private'),
        ('Self-employed', 'Self-employed')
    ], label="Work Type")
    Residence_type = forms.ChoiceField(choices=[('Rural', 'Rural'), ('Urban', 'Urban')], label="Residence Type")
    avg_glucose_level = forms.FloatField(min_value=0, label="Average Glucose Level")
    bmi = forms.FloatField(min_value=0, label="BMI")
    smoking_status = forms.ChoiceField(choices=[
        ('formerly smoked', 'Formerly Smoked'), ('never smoked', 'Never Smoked'),
        ('smokes', 'Smokes'), ('Unknown', 'Unknown')
    ], label="Smoking Status")