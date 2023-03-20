from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Movement


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
