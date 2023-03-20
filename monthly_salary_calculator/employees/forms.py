from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'role')
        labels = {
            'name': 'Nombre',
            'role': 'Rol',
        }
        widgets = {
            'role': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save'))
        