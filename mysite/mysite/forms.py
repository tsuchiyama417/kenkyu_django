from django import forms

class AnimalChoiceForm(forms.Form):
    CHOICE = [
        ('0', 'human'),
        ('1', 'gorilla'),
        ('2', 'pygmy_chimpanzee'),
        ('3', 'common_chimpanzee'),
        ('4', 'fin_whale'),
        ('5', 'blue_whale'),
        ('6', 'rat'),
        ('7', 'mouse'),
        ('8', 'opossum')
    ]

    select = forms.MultipleChoiceField(label='', widget=forms.CheckboxSelectMultiple, choices=CHOICE)
    