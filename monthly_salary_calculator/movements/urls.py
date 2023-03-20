from django.urls import path

from monthly_salary_calculator.movements.views import (
    MoventsView,
    MovementReport
)

app_name = "movements"
urlpatterns = [
    path("", MoventsView.as_view(), name=""),
    path("report", MovementReport.as_view(), name="report"),

]