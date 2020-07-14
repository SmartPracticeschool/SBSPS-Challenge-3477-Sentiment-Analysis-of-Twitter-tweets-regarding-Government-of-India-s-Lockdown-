#creating ModelForm here
from django import forms 
from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserForm(forms.ModelForm):
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    contact_number = forms.RegexField(regex=r'^[6-9]\d{9}$')

    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'email', 'contact_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-UserForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit('cancel', 'Cancel'))