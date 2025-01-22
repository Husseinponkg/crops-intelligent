from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# List of regions in Tanzania
REGIONS = [
    ('Arusha', 'Arusha'),
    ('Dar es Salaam', 'Dar es Salaam'),
    ('Dodoma', 'Dodoma'),
    ('Geita', 'Geita'),
    ('Iringa', 'Iringa'),
    ('Kagera', 'Kagera'),
    ('Katavi', 'Katavi'),
    ('Kigoma', 'Kigoma'),
    ('Kilimanjaro', 'Kilimanjaro'),
    ('Lindi', 'Lindi'),
    ('Manyara', 'Manyara'),
    ('Mara', 'Mara'),
    ('Mbeya', 'Mbeya'),
    ('Morogoro', 'Morogoro'),
    ('Mtwara', 'Mtwara'),
    ('Mwanza', 'Mwanza'),
    ('Njombe', 'Njombe'),
    ('Pemba North', 'Pemba North'),
    ('Pemba South', 'Pemba South'),
    ('Pwani', 'Pwani'),
    ('Rukwa', 'Rukwa'),
    ('Ruvuma', 'Ruvuma'),
    ('Shinyanga', 'Shinyanga'),
    ('Simiyu', 'Simiyu'),
    ('Singida', 'Singida'),
    ('Tabora', 'Tabora'),
    ('Tanga', 'Tanga'),
    ('Zanzibar North', 'Zanzibar North'),
    ('Zanzibar South', 'Zanzibar South'),
    ('Zanzibar West', 'Zanzibar West'),
]

class UserRegistrationForm(UserCreationForm):
    region = forms.ChoiceField(choices=REGIONS)

    class Meta:
        model = User
        fields = ['username', 'region', 'password1', 'password2']