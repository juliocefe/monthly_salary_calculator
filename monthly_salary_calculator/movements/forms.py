from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div
from .models import Movement


MONTH_CHOICES = [
    (1, 'Enero'),
    (2, 'Febrero'),
    (3, 'Marzo'),
    (4, 'Abril'),
    (5, 'Mayo'),
    (6, 'Junio'),
    (7, 'Julio'),
    (8, 'Agosto'),
    (9, 'Septiembre'),
    (10, 'Octubre'),
    (11, 'Noviembre'),
    (12, 'Diciembre'),
]


class MovementForm(forms.ModelForm):

    class Meta:
        model = Movement
        fields = ["employee", "deliveries", "created_at"]

        widgets = {
            "created_at": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("employee", css_class="form-group col-md-4 mb-0"),
                Column("deliveries", css_class="form-group col-md-4 mb-0"),
                Column("created_at", css_class="form-group col-md-4 mb-0"),
                css_class="form-row"
            ),
            Submit("submit", "Guardar")
        )


class MovementFilterForm(forms.Form):
    year = forms.ChoiceField(label="Año", choices=[])
    month = forms.ChoiceField(label="Mes", choices=MONTH_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        years = Movement.objects.dates('created_at', 'year').distinct().values_list('created_at__year', flat=True)
        year_choices = [(year, year) for year in years]
        self.fields['year'].choices = year_choices