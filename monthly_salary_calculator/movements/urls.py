from django.urls import path

from monthly_salary_calculator.movements.views import (
    MoventsView,
    movements_report
)

app_name = "movements"
urlpatterns = [
    path("", MoventsView.as_view(), name=""),
    path("report", movements_report, name="report"),

]